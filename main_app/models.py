from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True)
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None, blank=True)

    def __str__(self):
        return self.name
