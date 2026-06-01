from collections.abc import Callable
from typing import Optional

from src.main.api.configs.config import Config
from src.main.api.faundation.endpoint import Endpoint
from src.main.api.faundation.http_reuester import HttpRequester
from src.main.api.faundation.requesters.crud_requester import CrudRequester
from src.main.api.models.base_model import BaseModel
import allure

class ValidateCrudRequester(HttpRequester):
    def __init__(self, request_spec: str, endpoint: Endpoint, responce_spec: Callable ):
        super().__init__(request_spec, endpoint, responce_spec)
        self.crud_requester = CrudRequester(
            request_spec=request_spec,
            endpoint=endpoint,
            responce_spec=responce_spec,
        )

    def post(self, model: Optional[BaseModel] = None) -> Optional[BaseModel]:
        responce = self.crud_requester.post(model)

        with allure.step(f"POST {Config.fetch('backenUrl')}{self.endpoint.value.url} and Validated Model"):
            allure.attach(
                f"Validated Model response: {self.endpoint.value.responce_model.__name__}" if self.endpoint.value.responce_model else "No response model")
        self.responce_spec(responce)

        if self.endpoint.value.responce_model and responce.ok:
            return self.endpoint.value.responce_model.model_validate(responce.json())
        return None

    def delete(self, user_id: int) :
        responce = self.crud_requester.delete(user_id)
        self.responce_spec(responce)
        return self.endpoint.value.responce_model.model_validate(responce.json())