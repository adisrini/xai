from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your models here.
class Module(models.Model):
    module_title = models.CharField(max_length=200)
    module_route = models.CharField(max_length=200)
    module_description = models.CharField(max_length=200)
    module_color = models.CharField(max_length=200)

    def __str__(self):
        return self.module_title + ": " + self.module_description

class Dataset(models.Model):
    dataset_url = models.CharField(max_length=200)

    def __str__(self):
        return self.dataset_url

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class ExplainableModel(models.Model):
    model_name = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name
