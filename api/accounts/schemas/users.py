from pydantic import BaseModel, EmailStr, field_validator
from typing import  Optional
from core.helper import get_password_hash

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: Optional[str]
    is_super_admin: bool = False
    is_active: bool = True

    @field_validator("password")
    def encrypt_password(cls, value: str) -> str:
        return get_password_hash(value)
