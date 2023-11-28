from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path("<str:chat_room>/", room, name="room"),
]
