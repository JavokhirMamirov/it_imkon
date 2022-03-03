from django.urls import path

from bot.api.api_view import *

urlpatterns = [
    path('games/', get_games),
    path('games/<int:pk>/', get_games),
    path('viloyat/', get_viloyatlar),
    path('tuman/', get_tumanlar),
    path('rtm/', get_rtm),
    path('mahalla/', get_mahallalar),
    path('register/<int:chat_id>/', register),
    path('user/<int:chat_id>/', get_user),
    path('yetakchi/<int:pk>/', get_yetakchi),
]