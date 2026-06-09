import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_request import DepositRequest


@pytest.fixture
def two_accounts_with_deposit(api_manager: ApiManager, create_user_request: CreateUserRequest):
    first_account = api_manager.user_steps.create_account(create_user_request)
    second_account = api_manager.user_steps.create_account(create_user_request)
    api_manager.user_steps.account_deposit(create_user_request, DepositRequest(accountId=first_account.id, amount=1000))
    return first_account, second_account