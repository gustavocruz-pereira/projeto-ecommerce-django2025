from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('criar_conta/', views.criar_conta, name='criar_conta'),
]