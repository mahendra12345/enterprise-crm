from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [

    path("admin/", admin.site.urls),

    path(
        "api/v1/auth/",
        include("accounts.urls"),
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path(
        "api/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),

]