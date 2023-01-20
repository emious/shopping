
from django.db import models

'''

from django.utils import timezone



class Category(models.Model):

    name = models.CharField(max_length=50)








class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    Summary = models.CharField(max_length=100)
    Type = models.IntegerField()
    price = models.DecimalField()
    discount = models.DecimalField()
    Quantity = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    size = mode
    rate = models.IntegerField(default=0)
    desc = models.CharField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='دسته بندی')




'''




class Test(models.Model):

    name = models.CharField(max_length=50)
    data = models.JSONField(null=True,default={'size':[]})

    def __str__(self):
        return self.name



