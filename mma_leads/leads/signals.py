from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Stage

@receiver(post_migrate)
def create_default_stages(sender, **kwargs):
    if sender.name == 'leads':
        stages = [
         
        ]

        for stage in stages:
            Stage.objects.get_or_create(
                title=stage["title"],
                defaults=stage
            )
