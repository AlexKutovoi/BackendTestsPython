from typing import Annotated
from src.main.api.generator.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel

class CreateCreditUserRequest(BaseModel):
    username: Annotated[str, CreationRule(regex=r"^[a-zA-Z0-9]{3,15}$")]
    password: Annotated[str, CreationRule(regex=r"^[a-z]{1}[A-Z]{3}[0-9]{2}[!$]{4}$")]
    role: Annotated[str, CreationRule(regex=r"^ROLE_CREDIT_SECRET$")]