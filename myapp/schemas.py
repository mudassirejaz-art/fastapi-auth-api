from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LoginRequest(BaseModel):
    client_key: str
    secret_key: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    user_id: Optional[int]

class UserOut(BaseModel):
    id: int
    client_key: str
    created_at: datetime
