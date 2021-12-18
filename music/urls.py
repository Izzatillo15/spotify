from django.urls import path
from django.urls.conf import include
from .views import ArtistList, SongList,AlbumList


urlpatterns = [
    path('artist/',ArtistList.as_view()),
    path('songs/',SongList.as_view()),
    path('album/',AlbumList.as_view()),
]