from src.main.api.faundation.endpoint import Endpoint
from src.main.api.faundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.responce_specs import ResponceSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponceSpecs.request_created()
        ).post()
        return response

    def create_credit(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponceSpecs.request_created()
        ).post(credit_request)
        return response

    def create_credit_invalid(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponceSpecs.request_bad()
        ).post(credit_request)

    def credit_repay(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponceSpecs.request_ok()
        ).post(credit_request)
        return response

    def credit_repay_invalid(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponceSpecs.request_error()
        ).post(credit_request)

    def account_deposit(self, create_user_request: CreateUserRequest, deposit_request: DepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_DEPOSIT,
            ResponceSpecs.request_ok()
        ).post(deposit_request)
        return response

    def account_deposit_invalid(self, create_user_request: CreateUserRequest, deposit_request: DepositRequest):
        ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_DEPOSIT,
            ResponceSpecs.request_bad()
        ).post(deposit_request)

    def transfer(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest):
        resp = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_TRANSFER,
            ResponceSpecs.request_ok()
        ).post(transfer_request)
        return resp

    def transfer_invalid(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest):
        ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_TRANSFER,
            ResponceSpecs.request_bad()
        ).post(transfer_request)
