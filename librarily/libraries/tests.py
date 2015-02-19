from django.test import TestCase
from libraries.models import Place, Library, Book, Author, AuthorBook
from django.utils import timezone


class PlaceTestCase(TestCase):
    def setUp(self):
        Place.objects.create(address='68 Jay St', city='Brooklyn',
                             state='New York')

    def test_place_print(self):
        """Places are printed correctly by their address"""
        p = Place.objects.get(address='68 Jay St')
        self.assertEqual(str(p), '68 Jay St')


class LibraryTestCase(TestCase):
    def setUp(self):
        p = Place.objects.create(address='68 Jay St', city='Brooklyn',
                                 state='New York')
        Library.objects.create(name='DUMBO Library', place=p,
                               likes=0)

    def test_library_print(self):
        """Libraries are printed correctly by their name"""
        l = Library.objects.get(name='DUMBO Library')
        self.assertEqual(str(l), 'DUMBO Library')

    def test_place_cascade_delete(self):
        """If a place gets deleted, so should the library that is attached
        to it"""
        p = Place.objects.get(address='68 Jay St')
        p.delete()
        l = Library.all_objects.get(name='DUMBO Library')
        self.assertEqual(l.live, None)


class BookTestCase(TestCase):
    def setUp(self):
        p = Place.objects.create(address='68 Jay St', city='Brooklyn',
                                 state='New York')
        l = Library.objects.create(name='DUMBO Library', place=p,
                                   likes=0)
        Book.objects.create(title='Great Gatsby', pub_date=timezone.now(),
                            library=l)

    def test_book_print(self):
        """Books are printed correctly by their title"""
        b = Book.objects.get(title='Great Gatsby')
        self.assertEqual(str(b), 'Great Gatsby')

    def test_library_cascade_delete(self):
        """If a library gets deleted, so should the books attached
        to it"""
        l = Library.objects.get(name='DUMBO Library')
        l.delete()
        b = Book.all_objects.get(title='Great Gatsby')
        self.assertEqual(b.live, None)

    def test_place_cascade_delete(self):
        """If a place gets deleted, so should the library attached
        to it and the books attached to the library"""
        p = Place.objects.get(address='68 Jay St')
        p.delete()
        b = Book.all_objects.get(title='Great Gatsby')
        self.assertEqual(b.live, None)


class AuthorTestCase(TestCase):
    def setUp(self):
        p = Place.objects.create(address='68 Jay St', city='Brooklyn',
                                 state='New York')
        l = Library.objects.create(name='DUMBO Library', place=p,
                                   likes=0)
        b = Book.objects.create(title='Great Gatsby', pub_date=timezone.now(),
                                library=l)
        a = Author.objects.create(first_name='Francis', last_name='Fitzgerald')
        AuthorBook.objects.create(author=a, book=b)

    def test_author_print(self):
        """Authors are printed correctly by their full name"""
        a = Author.objects.get(first_name='Francis')
        self.assertEqual(str(a), 'Francis Fitzgerald')

    def test_place_cascade_delete(self):
        """If a place gets deleted, so should the library attached
        to it and the books attached to the library and any author
        book records. The author should still be there though."""
        p = Place.objects.get(address='68 Jay St')
        b = Book.objects.get(title='Great Gatsby')
        a = Author.objects.get(first_name='Francis')

        p.delete()
        ab = AuthorBook.all_objects.get(author=a, book=b)
        a = Author.all_objects.get(first_name='Francis')

        self.assertEqual(ab.live, None)
        self.assertEqual(a.live, True)
