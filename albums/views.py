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

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', pk=pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/edit_album.html', {'form': form})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('home')