from django.db import models

'''

from django.utils import timezone










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


class Banner(models.Model):
    image = models.ImageField(upload_to='sliders')
    link = models.CharField(max_length=2048)
    slogan = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=70, null=True, blank=True)

    # state == 1 for banners of template
    # state == 2 for SUB-BANNER of template
    state_choice = [("sld", "slider"), ("sub", "sub banner"), ("sng", "single banner"), ("sml", "small banner")]
    state = models.CharField(max_length=3, choices=state_choice)


class Category(models.Model):  # COMM0N
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class MainCategory(Category):

    def __str__(self):
        return self.name


class SubCategory(Category):
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



'''
class Test(models.Model):

    name = models.CharField(max_length=50)
    data = models.JSONField(null=True,default={'size':[]})

    def __str__(self):
        return self.name



'''
