from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # blank is about necessity. Necessary if False
    time_create = models.TimeField(auto_now_add=True)
    date_create = models.DateField(auto_now_add=True)
    time_update = models.TimeField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    # for some reasons DateTimeField refuse to work properly with PostGRE SQL database,
    # so they are put into the model separately
    status = models.ForeignKey('Status',
                               on_delete=models.PROTECT,
                               null=False,  # null is about necessity
                               default=1)
    user = models.ForeignKey(User, verbose_name='E-mail', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Status(models.Model):
    name = models.CharField(max_length=20)
    # todo: The table todoapp_status.csv with 3 items inside is placed into the root directory,
    #  needs to be imported to your database after migration

    def __str__(self):
        return self.name
