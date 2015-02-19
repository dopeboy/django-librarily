# django-librarily
This is a proof-of-concept reference project that I (1) used to learn Django and (2) will base future projects off of. Special care was taken to do things the right way as opposed to the quick way. All code should be [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant (thanks [vim-flake8](https://github.com/nvie/vim-flake8)).

## Concepts & technologies covered

* One to one relationships
* One to many relationships
* Many to many relationships
* Signals
* Model based forms
* Logging
* Soft delete
* Cascading deletes under soft delete
* Tests
* Class based views
* UUID keys 
* Overloaded operators
* Fixtures
* Templates with hierarchy
* AJAX calls
* Django debug toolbar
* Responding in JSON
* User login, logout, signup
* Static files
* Usage of 3rd party django libraries
* Virtualenv

## Entity diagram

The application replicates the classic library data model.  

![Image](http://i.imgur.com/rhAGAUU.png)

## Delete behavior
(Soft) delete rules are as follows:

1. Deleting a place also deletes the associated library.
2. Deleting a library also deletes the associated place.
3. Deleting a library also deletes any books it has.
4. Deleting a book also deletes any author-book associations (but not the author).
5. Deleting an author also deletes any author-book associations (but not the book).

## Usage

You'll need python 3.4.

`pip install -r requirements.txt`

## Shoutouts

Official django documentation, stackoverflow, and [mkolodny](https://github.com/mkolodny). 
