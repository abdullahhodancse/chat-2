from django.urls import path
from rest_framework.routers import DefaultRouter
from  account.api.view.login import LoginView
from  account.api.view.reg import RegisterView



router = DefaultRouter()

urlpatterns = [

    path('reg/',RegisterView.as_view(),name = "register"),
    path('login/',LoginView.as_view(),name = "login")

]