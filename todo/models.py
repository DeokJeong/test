from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=128, default="")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
