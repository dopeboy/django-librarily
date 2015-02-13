from django.dispatch import Signal

post_delete = Signal(['sender', 'instance'])
