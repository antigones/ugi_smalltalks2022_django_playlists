"""myplaylistsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myplaylists.views import ArtistCreateView, ArtistDeleteView, ArtistListView, ArtistUpdateView, PlaylistCreateView, PlaylistDeleteView, PlaylistListView, PlaylistUpdateView, SongCreateView, SongListView, SongUpdateView, SongDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('artist/add/', ArtistCreateView.as_view(), name='artist-add'),
    path('artist/<int:pk>/', ArtistUpdateView.as_view(), name='artist-update'),
    path('artist/<int:pk>/delete/', ArtistDeleteView.as_view(), name='artist-delete'),

    path('songs/', SongListView.as_view(), name='song-list'),
    path('song/add/', SongCreateView.as_view(), name='song-add'),
    path('song/<int:pk>/', SongUpdateView.as_view(), name='song-update'),
    path('song/<int:pk>/delete/', SongDeleteView.as_view(), name='song-delete'),

    path('', PlaylistListView.as_view(), name='playlist-list'),
    path('playlist/add/', PlaylistCreateView.as_view(), name='playlist-add'),
    path('playlist/<int:pk>/', PlaylistUpdateView.as_view(), name='playlist-update'),
    path('playlist/<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist-delete'),
]
