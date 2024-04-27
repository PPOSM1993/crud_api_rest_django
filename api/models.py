from django.db import models

# Create your models here.


class Tasks(models.Model):
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.body
