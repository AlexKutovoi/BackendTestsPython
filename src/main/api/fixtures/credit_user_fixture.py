import pytest
from src.main.api.generator.model_generator import RandomModelGenerator
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest


@pytest.fixture
def create_credit_user_request(api_manager):
    user_credit_request = RandomModelGenerator.generate(CreateCreditUserRequest)
    api_manager.admin_steps.create_user(user_credit_request)
    return user_credit_request