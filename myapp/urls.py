from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('message', views.env_var_message, name='env_var_message'),
    path('number', views.env_var_number, name='env_var_number'),
]
