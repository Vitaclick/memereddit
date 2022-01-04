from enum import unique
from django.db import models
import uuid

# Create your models here.
class Subreddit(models.Model):
  title = models.CharField(max_length=200)
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

  def __str__(self):
    return self.title