from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create your models here.
class C_InnerMaster(models.Model):
    Id = models.AutoField(auto_created=True, primary_key=True, serialize=False),
    InnerName = models.CharField(max_length=50, blank=False, default='', unique=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    CreatedBy = models.CharField(max_length=50, blank=False, default='')
    ModifiedOn = models.DateTimeField(null=True, blank=True)
    ModifiedBy = models.CharField(max_length=50, blank=False, default='')

    class Meta:
        db_table = 'C_InnerMaster'
