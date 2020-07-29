from django.db import models

# Create your models here.
class Article(models.Model):
    date = models.DateTimeField()
    title = models.CharField(default='Untitled', max_length=120)
    content = models.TextField()
    index = models.DecimalField(decimal_places=2, max_digits=100, default=0)