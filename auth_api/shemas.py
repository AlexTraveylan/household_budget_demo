from ninja import Schema


class MessageSchema(Schema):
    message: str


class UserSchema(Schema):
    username: str
    password: str


class TokenSchema(Schema):
    token: str
