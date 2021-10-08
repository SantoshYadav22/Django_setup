from django.urls import path
from . import views

urlpatterns = [
    path('setup/',views.starts),
    path('setups/',views.app),
]