from django.contrib import admin
from libraries.models import Place, Author, Book, Library

# Register your models here.
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Place)
admin.site.register(Author)
