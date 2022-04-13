from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Playlist, Song, Artist

class ArtistListView(ListView):
    model = Artist

class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name']
    success_url = reverse_lazy('artist-list')

class ArtistUpdateView(UpdateView):
    model = Artist
    fields = ['name']
    success_url = reverse_lazy('artist-list')

class ArtistDeleteView(DeleteView):
    model = Artist
    success_url = reverse_lazy('artist-list')

class SongListView(ListView):
    model = Song

class SongCreateView(CreateView):
    model = Song
    fields = ['name', 'artist']
    success_url = reverse_lazy('song-list')


class SongUpdateView(UpdateView):
    model = Song
    fields = ['name', 'artist']
    success_url = reverse_lazy('song-list')

class SongDeleteView(DeleteView):
    model = Song
    success_url = reverse_lazy('song-list')

class PlaylistListView(ListView):
    model = Playlist

class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['name', 'songs']
    success_url = reverse_lazy('playlist-list')

class PlaylistUpdateView(UpdateView):
    model = Playlist
    fields = ['name', 'songs']
    success_url = reverse_lazy('playlist-list')

class PlaylistDeleteView(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist-list')