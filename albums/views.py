from django.shortcuts import render, get_object_or_404
from .models import Album


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', context={'album': album})

