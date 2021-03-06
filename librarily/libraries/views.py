from django.http import HttpResponseRedirect
from libraries.models import Library, Book, Author, Place, AuthorBook
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from libraries.forms import (PlaceCreateUpdateForm, LibraryCreateUpdateForm,
                             BookCreateUpdateForm, AuthorCreateUpdateForm,
                             UserCreateForm)
from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from jsonview.decorators import json_view
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)


class LibraryListView(generic.ListView):
    template_name = 'libraries/library/list.html'
    context_object_name = 'latest_library_list'

    def get_queryset(self):
        return Library.objects.order_by('name')


class LibraryDetailView(generic.DetailView):
    model = Library
    template_name = 'libraries/library/detail.html'


class LibraryLikeView(generic.base.View):
    template_name = None

    @method_decorator(json_view)
    def post(self, request, *args, **kwargs):
        library = get_object_or_404(Library, pk=self.kwargs['pk'])
        library.likes += 1
        library.save()

        response_data = {}
        response_data['likes'] = library.likes
        return response_data


class LibraryUpdateView(generic.edit.UpdateView):
    model = Library
    form_class = LibraryCreateUpdateForm
    template_name = 'libraries/library/update.html'


class LibraryCreateView(generic.edit.CreateView):
    template_name = 'libraries/library/create.html'
    form_class = LibraryCreateUpdateForm


class LibraryDeleteView(generic.edit.DeleteView):
    model = Library
    success_url = reverse_lazy('libraries:library_list')


class AuthorListView(generic.ListView):
    template_name = 'libraries/author/list.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.order_by('first_name')


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'libraries/author/detail.html'


class AuthorCreateView(generic.edit.CreateView):
    form_class = AuthorCreateUpdateForm
    template_name = 'libraries/author/create.html'


class AuthorUpdateView(generic.edit.UpdateView):
    model = Author
    form_class = AuthorCreateUpdateForm
    template_name = 'libraries/author/update.html'


class AuthorDeleteView(generic.edit.DeleteView):
    model = Author
    success_url = reverse_lazy('libraries:author_list')


class BookListView(generic.ListView):
    template_name = 'libraries/book/list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.order_by('title')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'libraries/book/detail.html'


class BookCreateMixin(object):
    class Meta:
        abstract = True

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            for author in form.cleaned_data['authors']:
                book_author = AuthorBook(book=book, author=author)
                book_author.save()

            return HttpResponseRedirect(book.get_absolute_url())

        return render(request, self.template_name, {'form': form})


class BookCreateView(BookCreateMixin, generic.edit.CreateView):
    form_class = BookCreateUpdateForm
    template_name = 'libraries/book/create.html'


class BookUpdateView(BookCreateMixin, generic.edit.UpdateView):
    model = Book
    form_class = BookCreateUpdateForm
    template_name = 'libraries/book/update.html'


class BookDeleteView(generic.edit.DeleteView):
    model = Book
    success_url = reverse_lazy('libraries:book_list')


class PlaceListView(generic.ListView):
    template_name = 'libraries/place/list.html'
    context_object_name = 'place_list'

    def get_queryset(self):
        return Place.objects.order_by('address')


class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'libraries/place/detail.html'


class PlaceCreateView(generic.edit.CreateView):
    template_name = 'libraries/place/create.html'
    model = Place
    form_class = PlaceCreateUpdateForm


class PlaceUpdateView(generic.edit.UpdateView):
    template_name = 'libraries/place/update.html'
    form_class = PlaceCreateUpdateForm
    model = Place


class PlaceDeleteView(generic.edit.DeleteView):
    model = Place
    success_url = reverse_lazy('libraries:place_list')


class UserLoginView(generic.edit.FormView):
    template_name = 'libraries/user/login.html'
    form_class = AuthenticationForm

    # If the user is already logged in, redirect them away
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return super(generic.edit.FormView, self).get(request, *args,
                                                          **kwargs)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {'form': form})


class UserCreateView(generic.edit.CreateView):
    template_name = 'libraries/user/create.html'
    form_class = UserCreateForm

    # If the user is already logged in, redirect them away
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return super(generic.edit.CreateView, self).get(request, *args,
                                                            **kwargs)

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {'form': form})
