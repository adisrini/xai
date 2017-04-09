from django.db import models

# Create your models here.
class Module(models.Model):
    module_title = models.CharField(max_length=200)
    module_route = models.CharField(max_length=200)
    module_description = models.CharField(max_length=200)
    module_color = models.CharField(max_length=200)

    def __str__(self):
        return self.module_title + ": " + self.module_description

class Dataset(models.Model):
    dataset_url  = models.CharField(max_length=200)

    def __str__(self):
        return self.dataset_url
