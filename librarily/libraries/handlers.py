from django.dispatch import receiver
from libraries.signals import post_delete
from libraries.models import Place, Library, Book, Author

# When a place gets deleted, the associated
# library (if one exists) gets deleted
@receiver(post_delete, sender=Place)
def delete_library(sender, **kwargs):
    try:
        kwargs.get("instance").library_set.all()[0].delete()
    except AttributeError:
        pass

# When a library gets deleted, the associated
# books gets deleted
@receiver(post_delete, sender=Library)
def delete_book(sender, **kwargs):
    try:
        for book in kwargs.get("instance").book_set.all():
            book.delete()
    except AttributeError:
        pass

    # Important: you CANNOT do the following because
    # it does not call the signal handler with the right 
    # sender
    # kwargs.get("instance").book_set.all().delete()

# When a book gets deleted, the associated
# authorbook records (in the join table) get deleted
@receiver(post_delete, sender=Book)
def delete_authorbook_book(sender, **kwargs):
    try:
        kwargs.get("instance").authors.clear()
    except AttributeError:
        pass


# When a author gets deleted, the associated
# authorbook records (in the join table) get deleted
@receiver(post_delete, sender=Author)
def delete_authorbook_author(sender, **kwargs):
    try:
        kwargs.get("instance").books.clear()
    except AttributeError:
        pass
