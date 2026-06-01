from src.main.api.faundation.endpoint import Endpoint
from typing import Dict, Callable

class HttpRequester:
    def __init__(self, request_spec: Dict[str, str], endpoint: Endpoint, responce_spec: Callable):
        self.request_spec = request_spec
        self.endpoint = endpoint
        self.responce_spec = responce_spec
