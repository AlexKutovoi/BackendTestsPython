from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_responce import CreditResponse
from src.main.api.requests.requester import Requester
from requests import Response
import requests


class CreditRequester(Requester):
    def post(self, credit_request: CreditRequest) -> CreditRequest | Response:
        url = f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=credit_request.model_dump(),
            headers=self.headers
        )
        self.responce_spec(response)
        return CreditResponse(**response.json())