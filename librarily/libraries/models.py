from django.db import models
from django_extensions.db.fields import PostgreSQLUUIDField
from django.core.urlresolvers import reverse
from livefield import LiveField, LiveManager
import logging
from libraries.signals import post_delete

class GenericModel(models.Model):
	class Meta:
		abstract = True

	uuid = PostgreSQLUUIDField(auto=True, primary_key=True, db_column='id')
	live = LiveField()
	objects = LiveManager()
	all_objects = LiveManager(include_soft_deleted=True)

	def delete(self, using=None):
		self.live = False
		self.save(using=using)
		post_delete.send(sender=self.__class__, instance=self)

class Place(GenericModel):
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=128)
	
	class Meta:
		unique_together = ('address', 'city', 'state', 'live')

	def get_absolute_url(self):
		return reverse('libraries:place_detail', kwargs={'pk': self.uuid})

	def __str__(self):
		return self.address 

class Library(GenericModel):
	name = models.CharField(max_length=128)

	# We're not making this a OneToOne because with soft delete,
	# it is OK to have multiple soft deleted records in this table with the same
	# place ID
	place = models.ForeignKey(Place)

	# This takes care of having only one live library-place record. Needed for soft delete
	class Meta:
		unique_together = ('place', 'live')

	def get_absolute_url(self):
		return reverse('libraries:library_detail', kwargs={'pk': self.uuid})
	
	def __str__(self):
		return self.name 

class Author(GenericModel):
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	books = models.ManyToManyField('Book', through='AuthorBook')

	def get_absolute_url(self):
		return reverse('libraries:author_detail', kwargs={'pk': self.uuid})

	def __str__(self):
		return ' '.join([self.first_name, self.last_name])

class Book(GenericModel):
	title = models.CharField(max_length=128)
	pub_date = models.DateTimeField(verbose_name='date published')
	library = models.ForeignKey(Library)
	authors = models.ManyToManyField('Author', through='AuthorBook')

	def get_absolute_url(self):
		return reverse('libraries:book_detail', kwargs={'pk': self.uuid})

	def __str__(self):
		return self.title

class AuthorBook(GenericModel):
	author = models.ForeignKey(Author)
	book = models.ForeignKey(Book)
