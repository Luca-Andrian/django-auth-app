# -*- encoding: utf-8 -*-

from .views import LoginViews, LogoutView
from django.urls import path

urlpatterns = [
    path(
        "login/",
        LoginViews.as_view(),
        name="login"
        ),
    path("logout/",
        LogoutView.as_view(),
        name='logout'
        ),
    ]