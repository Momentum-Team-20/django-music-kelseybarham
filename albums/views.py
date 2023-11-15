from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', context={'album': album})


def create_new_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'albums/new_album.html', {'form': form})