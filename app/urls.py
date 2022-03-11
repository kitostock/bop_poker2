from django.conf.urls import include
from django.urls import path
# from rest_framework import routers
from .views import BopInfoRegisterView, BopInfoFindView, BopInfoFindDateView
# from . import CreateUserView, UserView

urlpatterns = [
    path('bop_info/register/', BopInfoRegisterView.as_view()),
    path('bop_info/find/', BopInfoFindView.as_view()),
    path('bop_info/find-date/', BopInfoFindDateView.as_view()),
]

