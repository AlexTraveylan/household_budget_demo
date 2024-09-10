from typing import Self, TypedDict

import jwt
from ninja.security import HttpBearer

from budget_demo.settings import JWT_SECRET


class TokenContent(TypedDict):
    username: str


class BearerToken:
    def __init__(self, username: str) -> None:
        self.username = username

    def __repr__(self) -> str:
        return f"BearerToken(username={self.username})"

    def to_dict(self) -> TokenContent:
        return {"username": self.username}

    def to_jwt_token(self) -> str:
        return jwt.encode(self.to_dict(), JWT_SECRET, algorithm="HS256")

    @classmethod
    def from_jwt_token(cls, token: str) -> Self:
        data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return cls(username=data["username"])


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: str) -> BearerToken:
        try:
            token = BearerToken.from_jwt_token(token)
        except Exception as e:
            raise e

        return token
