from django import forms
from django.contrib.auth.models import User

from .models import Artist


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ['artist', 'album_title', 'genre', 'album_logo']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        