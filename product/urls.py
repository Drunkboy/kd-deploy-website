#product/urls.py

from django.urls import path
from .views import Home, About, Timber

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/',About, name='about-page'),
    path('timber/',Timber, name='timber-page')
]