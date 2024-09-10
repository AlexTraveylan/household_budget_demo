from auth_api.token import BearerToken


def test_token_creation():
    token = BearerToken(username="test")

    encoded_token = token.to_jwt_token()

    assert isinstance(encoded_token, str)

    decoded_token = BearerToken.from_jwt_token(encoded_token)

    assert decoded_token.username == "test"
