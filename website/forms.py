from django.forms import ModelForm, ImageField
from .models import Room, Post, User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User

        labels = {
            'username': 'Nazwa użytkownika',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ApplyTeacherForm(UserCreationForm):
    class Meta:
        model = User

        labels = {
            'username': 'Nazwa użytkownika',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ApplyStudentForm(UserCreationForm):
    class Meta:
        model = User

        labels = {
            'username': 'Nazwa użytkownika',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

    image = ImageField(required=False)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class PostForm(forms.ModelForm):
    event_datetime = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label='Data',  # You can customize the label here
        input_formats=['%Y-%m-%dT%H:%M'],  # Define the input format (adjust it to your needs)
    )

    class Meta:
        model = Post
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'course': 'Kurs',
        }
        fields = ['title', 'description', 'course', 'event_datetime']