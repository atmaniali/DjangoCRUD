from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length= 600)
    def __str__(self):
        return self.title
