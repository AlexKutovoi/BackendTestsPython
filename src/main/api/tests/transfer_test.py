from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.transaction_crud import TransactionCrudDb
from src.main.api.db.models.account_table import Account
from src.main.api.db.crud.account_crud import AccountCrubDb
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.create_user_request import CreateUserRequest
from sqlalchemy.orm import Session


class TestTransfer:
    def test_transfer(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest, two_accounts_with_deposit):
        first_account, second_account = two_accounts_with_deposit

        resp = api_manager.user_steps.transfer(create_user_request, TransferRequest(fromAccountId=first_account.id,
                                                           toAccountId=second_account.id, amount=500))
        assert resp.fromAccountId == first_account.id
        assert resp.toAccountId == second_account.id
        assert resp.fromAccountIdBalance == 500

        first_account_from_db = AccountCrubDb.get_account_by_id(db_session, first_account.id)
        assert first_account_from_db.balance == 500, 'Balance is not decreased'

    def test_transfer_invalid(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest, two_accounts_with_deposit):
        first_account, second_account = two_accounts_with_deposit

        api_manager.user_steps.transfer_invalid(create_user_request,
                                            TransferRequest(fromAccountId=first_account.id,
                                                            toAccountId=second_account.id, amount=10))

        transaction_from_db = TransactionCrudDb.get_transaction_by_account_id(db_session, first_account.id)
        assert transaction_from_db is None, 'Transaction is created in DB'