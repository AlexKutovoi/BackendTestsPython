import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request import CreditRequest


@pytest.mark.api
class TestCreateCreditForUser:
    def test_credit_for_user(self, db_session: Session, api_manager: ApiManager, create_credit_user_request: CreditRequest):
        res = api_manager.user_steps.create_account(create_credit_user_request)

        responce = api_manager.user_steps.create_credit(
            create_credit_user_request,
            CreditRequest(accountId=res.id, amount=7000, termMonths=8))
        assert responce.id == res.id
        assert responce.amount == 7000
        assert responce.termMonths == 8
        assert responce.balance == 7000

        credit_from_user_db = CreditCrudDb.get_credit_by_id(db_session, responce.creditId)
        assert credit_from_user_db.amount == 7000, 'Credit amount is wrong in DB'

    def test_invalid_credit_for_user(self, db_session: Session,
                                     api_manager:ApiManager, create_credit_user_request: CreditRequest):
        res = api_manager.user_steps.create_account(create_credit_user_request)

        api_manager.user_steps.create_credit_invalid(
            create_credit_user_request,
            CreditRequest(accountId=res.id, amount=1000, termMonths=8))

        credit_from_user_db = CreditCrudDb.get_credit_by_account_id(db_session, res.id)
        assert credit_from_user_db is None, 'Credit is created in DB'

    def test_credit_repay(self, db_session: Session, api_manager: ApiManager,
                          create_credit_user_request: CreditRequest, account_with_credit):
        account, credit = account_with_credit

        respon = api_manager.user_steps.credit_repay(
            create_credit_user_request,
            CreditRepayRequest(creditId=credit.creditId, accountId=account.id, amount=credit.amount))
        assert respon.creditId == credit.creditId
        assert respon.amountDeposited == credit.amount

        repay_credit_for_user_db = CreditCrudDb.get_credit_by_id(db_session, credit.creditId)
        assert repay_credit_for_user_db.balance == 0, 'Credit balance is not 0 after repay'

    def test_invalid_credit_repay(self, db_session: Session, api_manager: ApiManager,
                                  create_credit_user_request: CreditRequest, account_with_credit):
        account, credit = account_with_credit

        api_manager.user_steps.credit_repay_invalid(
            create_credit_user_request,
            CreditRepayRequest(creditId=credit.creditId, accountId=account.id, amount=500))

        repay_credit_for_user_db = CreditCrudDb.get_credit_by_id(db_session, credit.creditId)
        assert repay_credit_for_user_db.balance == -7000, 'Credit balance has not changed'