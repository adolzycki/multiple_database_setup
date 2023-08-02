from itertools import chain

from django.db import models


class BookManager(models.Manager):
    def get_queryset(self):
        default_db = super().get_queryset().using('default')
        db_2 = super().get_queryset().using('db-2')
        db_3 = super().get_queryset().using('db-3')
        return chain(default_db, db_2, db_3)


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)

    objects = BookManager()


