from django.conf import settings as django_settings
from django.db import models

User = django_settings.AUTH_USER_MODEL

CREATE_BY_UPDATE_BY_FIELDS = ('created_by', 'updated_by', 'created_at', 'updated_at')


class CreatedByUpdateByMixin:
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_created_by', null=True,
                                   blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(class)s_updated_by', null=True,
                                   blank=True)
    created_at = models.DateTimeField("Created date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated date", auto_now=True)
