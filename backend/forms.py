from django.forms import ModelForm
from backend.models import Image, Image2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', }),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', }),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


class ImageForm2(ModelForm):
    class Meta:
        model = Image2
        fields = "__all__"
