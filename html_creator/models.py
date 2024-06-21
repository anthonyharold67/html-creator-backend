from django.db import models

# Create your models here.
class HtmlCreatorModel(models.Model):
    entity_id = models.PositiveIntegerField(unique=True)
    html_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    