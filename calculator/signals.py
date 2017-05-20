from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Calculator


@receiver(post_save, sender=User)
def create_calc_on_user_creation(sender, instance, **kwargs):
    if kwargs["created"]:
        calc = Calculator.objects.create(user=instance)
        calc.save()
