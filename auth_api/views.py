from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from auth_api.shemas import MessageSchema, TokenSchema, UserSchema
from auth_api.token import AuthBearer, BearerToken
from budget_demo.urls import api


@api.post("/login", response={200: TokenSchema, 401: MessageSchema})
def login(request, user: UserSchema):
    user = authenticate(username=user.username, password=user.password)
    if user is None:
        return 401, MessageSchema(message="Invalid username or password")

    bearer = BearerToken(username=user.username)
    encoded_token = bearer.to_jwt_token()

    return 200, TokenSchema(token=encoded_token)


@api.post("/register", response={201: TokenSchema, 400: MessageSchema})
def register(request, user: UserSchema):
    try:
        user = User.objects.create_user(username=user.username, password=user.password)
        encoded_token = BearerToken(username=user.username).to_jwt_token()

        return 201, TokenSchema(token=encoded_token)
    except Exception as e:
        return 400, MessageSchema(message=str(e))


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth.username}
