from django import forms
from .models import Album

import datetime


class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = ('artist_name', 'title')