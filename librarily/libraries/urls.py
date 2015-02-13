from django.conf.urls import patterns, url
from libraries import views
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

uuid_pattern = '[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}'

urlpatterns = patterns('',
	url(r'^$', views.UserLoginView.as_view(), name='login'),
	url(r'^user/logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('libraries:login')}, name='logout'),
	url(r'^user/create/$', views.UserCreateView.as_view(), name='user_create'), 
	url(r'^library/list/$', login_required(views.LibraryListView.as_view()), name='library_list'), 
	url(r'^library/detail/(?P<pk>' + uuid_pattern + ')/$', login_required(views.LibraryDetailView.as_view()), name='library_detail'), 
	url(r'^library/create/$', login_required(views.LibraryCreateView.as_view()), name='library_create'), 
	url(r'^library/update/(?P<pk>' + uuid_pattern + ')/$', login_required(views.LibraryUpdateView.as_view()), name='library_update'), 
	url(r'^library/delete/(?P<pk>' + uuid_pattern + ')/$', login_required(views.LibraryDeleteView.as_view()), name='library_delete'), 
	url(r'^author/list/$', login_required(views.AuthorListView.as_view()), name='author_list'), 
	url(r'^author/detail/(?P<pk>' + uuid_pattern + ')/$', login_required(views.AuthorDetailView.as_view()), name='author_detail'), 
	url(r'^author/create/$',login_required(views.AuthorCreateView.as_view()), name='author_create'), 
	url(r'^author/update/(?P<pk>' + uuid_pattern + ')/$', login_required(views.AuthorUpdateView.as_view()), name='author_update'), 
	url(r'^author/delete/(?P<pk>' + uuid_pattern + ')/$', login_required(views.AuthorDeleteView.as_view()), name='author_delete'), 
	url(r'^book/list/$', login_required(views.BookListView.as_view()), name='book_list'), 
	url(r'^book/detail/(?P<pk>' + uuid_pattern + ')/$', login_required(views.BookDetailView.as_view()), name='book_detail'), 
	url(r'^book/create/$', login_required(views.BookCreateView.as_view()), name='book_create'), 
	url(r'^book/update/(?P<pk>' + uuid_pattern + ')/$', login_required(views.BookUpdateView.as_view()), name='book_update'), 
	url(r'^book/delete/(?P<pk>' + uuid_pattern + ')/$', login_required(views.BookDeleteView.as_view()), name='book_delete'), 
	url(r'^place/list/$', login_required(views.PlaceListView.as_view()), name='place_list'), 
	url(r'^place/detail/(?P<pk>' + uuid_pattern + ')/$', login_required(views.PlaceDetailView.as_view()), name='place_detail'), 
	url(r'^place/update/(?P<pk>' + uuid_pattern + ')/$', login_required(views.PlaceUpdateView.as_view()), name='place_update'), 
	url(r'^place/create/$', login_required(views.PlaceCreateView.as_view()), name='place_create'),
	url(r'^place/delete/(?P<pk>' + uuid_pattern + ')/$', login_required(views.PlaceDeleteView.as_view()), name='place_delete'), 
)