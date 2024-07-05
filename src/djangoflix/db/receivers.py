from django.utils import timezone
from django.utils.text import slugify

from .models import PublishStateOptions


def publish_state_pre_save(sender, instance, *args, **kwargs):
    if instance.state == PublishStateOptions.PUBLISH and instance.published_at is None:
        instance.published_at = timezone.now()
    elif PublishStateOptions.DRAFT == instance.state:
        instance.published_at = None


def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)
