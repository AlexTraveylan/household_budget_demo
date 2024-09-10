from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

from auth_api.views import *
from budget_api.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
