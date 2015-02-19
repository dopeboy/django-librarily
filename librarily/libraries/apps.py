from django.apps import AppConfig


class LibrariesConfig(AppConfig):
    name = 'libraries'

    def ready(self):
        import libraries.handlers
