from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book


@receiver(post_save, sender=Book)
def model_post_save(sender, **kwargs):
    print('Saved: {}'.format(kwargs['instance'].__dict__))
 
 
@receiver(post_delete, sender=Book)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))
 
 
class ReadOnlyException(Exception):
    pass
