from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
