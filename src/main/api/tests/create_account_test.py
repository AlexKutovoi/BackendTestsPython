import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.transaction_crud import TransactionCrudDb
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.db.crud.user_crud import UserCrudDb
from src.main.api.db.crud.account_crud import AccountCrubDb as Account


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest):
        responce = api_manager.user_steps.create_account(create_user_request)

        assert responce.balance == 0

        account_from_db = Account.get_account_by_id(db_session, responce.id)
        assert account_from_db.balance is not None, 'Balance is not created in DB'

    def test_create_account_credit_user(self, db_session: Session, api_manager: ApiManager, create_credit_user_request: CreateCreditUserRequest):
        res = api_manager.user_steps.create_account(create_credit_user_request)

        assert res.balance == 0

        Account.get_account_by_id(db_session, res.id)
        user_from_db = UserCrudDb.get_user_by_username(db_session, create_credit_user_request.username)
        assert user_from_db.role == 'ROLE_CREDIT_SECRET', 'Role is not ROLE_CREDIT_SECRET'

    def test_account_deposit(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest):
        responce = api_manager.user_steps.create_account(create_user_request)

        assert responce.balance == 0

        res = api_manager.user_steps.account_deposit(create_user_request, DepositRequest(accountId=responce.id, amount = 1000))

        assert res.id == responce.id
        assert res.balance == 1000

        account_deposit_from_db = TransactionCrudDb.get_transaction_by_to_account_id(db_session, responce.id)
        assert account_deposit_from_db.transaction_type == 'deposit', 'Transaction type is not deposit'

    def test_account_deposit_invalid(self, db_session:Session, api_manager: ApiManager, create_user_request: CreateUserRequest):
        responce = api_manager.user_steps.create_account(create_user_request)

        assert responce.balance == 0

        api_manager.user_steps.account_deposit_invalid(create_user_request, DepositRequest(accountId=responce.id, amount = 190000))

        account_deposit_from_db = TransactionCrudDb.get_transaction_by_to_account_id(db_session, responce.id)
        assert account_deposit_from_db is None, 'Deposit transaction is created in DB'

