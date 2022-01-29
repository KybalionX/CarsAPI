from django.urls import path
from .views import *


urlpatterns = [
    path('coches/', CochesView.as_view())
]