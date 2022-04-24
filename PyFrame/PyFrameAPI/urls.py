from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('frame', views.calcul, name='calcul'),
    path('', views.home, name='home')
]