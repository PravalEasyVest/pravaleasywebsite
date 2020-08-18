from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexfunc, name='indexfunc'),
]