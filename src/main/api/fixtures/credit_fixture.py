import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.credit_request import CreditRequest


@pytest.fixture
def account_with_credit(api_manager: ApiManager, create_credit_user_request: CreditRequest):
    account = api_manager.user_steps.create_account(create_credit_user_request)
    credit = api_manager.user_steps.create_credit(
        create_credit_user_request,
        CreditRequest(accountId = account.id, amount = 7000, termMonths = 7))
    return account, credit