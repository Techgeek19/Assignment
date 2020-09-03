from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.decorators import login_required

app_name = "main"

urlpatterns = [
    path('api/v1/calculate', login_required(views.calc), name='Calc'),
    path('api/v1/sol', login_required(views.sol), name='home'),
    path('', views.home, name='home')
]
