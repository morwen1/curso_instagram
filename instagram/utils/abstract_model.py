from django.db import models


class AbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(blank=True , null=True)

    class Meta:
        abstract=True