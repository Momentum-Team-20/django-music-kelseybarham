from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='home'),
    path('album_detail/<int:pk>', views.album_detail, name='album-details')
]