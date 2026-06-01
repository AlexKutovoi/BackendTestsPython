import requests
from src.main.api.models.create_account_responce import CreateAccountResponse
from src.main.api.requests.requester import Requester


class CreateAccountRequester(Requester):
    def post(self, model = None) -> CreateAccountResponse:
        url = f"{self.base_url}/account/create"
        response = requests.post(
            url = url,
            headers = self.headers
        )
        self.responce_spec(response)
        return CreateAccountResponse(**response.json())