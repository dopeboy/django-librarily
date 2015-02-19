from django.forms import ModelForm
from libraries.models import Library, Place, Author, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlaceCreateUpdateForm(ModelForm):
    class Meta:
        model = Place
        exclude = ['live']
        fields = '__all__'


class LibraryCreateUpdateForm(ModelForm):
    class Meta:
        model = Library
        exclude = ['live', 'likes']
        fields = '__all__'


class BookCreateUpdateForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['live']
        fields = '__all__'


class AuthorCreateUpdateForm(ModelForm):
    class Meta:
        model = Author
        exclude = ['live', 'books']
        fields = '__all__'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
