from django.urls import path
from .views import get_song_by_isrc

urlpatterns = [
    path('test-isrc/', get_song_by_isrc, name='spotify_test'),



]
