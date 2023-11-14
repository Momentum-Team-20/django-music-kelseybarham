from django.shortcuts import render

# Create your views here.
def list_albums(request):
    return render(request, 'albums/index.html')