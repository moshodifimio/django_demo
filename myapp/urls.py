from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('env_var_message/', views.env_var_message, name='env_var_message'),
    path('env_var_number/', views.env_var_number, name='env_var_number'),
]
