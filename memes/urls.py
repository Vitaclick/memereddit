from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_memes, name='memes'),
    path('meme/<str:pk>', views.show_memes, name='memes')
]
