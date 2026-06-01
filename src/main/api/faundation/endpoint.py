from dataclasses import dataclass
from typing import Optional, Type
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_responce import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_responce import CreateUserResponse
from enum import Enum
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_responce import CreditRepayResponse
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_responce import CreditResponse
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_responce import DepositResponce
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_responce import LoginUserResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.transfer_responce import TransferResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    responce_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequest,
        url = "/admin/create",
        responce_model=CreateUserResponse
    )

    ADMIN_UPDATE_USER = EndpointConfiguration(
        request_model = None,
        url = "/admin/users",
        responce_model = None
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        url="/admin/users",
        responce_model=None
    )

    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        url = "/auth/token/login",
        responce_model = LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        request_model = None,
        url = "/account/create",
        responce_model = CreateAccountResponse
    )

    CREDIT_REQUEST = EndpointConfiguration(
        request_model = CreditRequest,
        url = "/credit/request",
        responce_model = CreditResponse
    )

    CREDIT_REPAY = EndpointConfiguration(
        request_model = CreditRepayRequest,
        url = "/credit/repay",
        responce_model= CreditRepayResponse
    )

    ACCOUNT_DEPOSIT = EndpointConfiguration(
        request_model = DepositRequest,
        url = "/account/deposit",
        responce_model = DepositResponce
    )

    ACCOUNT_TRANSFER = EndpointConfiguration(
        request_model= TransferRequest,
        url = "/account/transfer",
        responce_model = TransferResponse
    )