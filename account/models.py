from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

''' 
class AddressModel(models.Model):
    full_name = models.CharField(max_length=)
    email = models.CharField(max_length=100)
    call_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=)
    address = models.CharField(max_length=)
    State_id = models.IntegerField()
    cities_id = models.IntegerField()

    class Meta:
        abstract =True
'''


class ProfileModel(models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربری', related_name='profile')
    mobile = models.CharField(max_length=30, null=True, blank=True, verbose_name='شمار همراه')
    address = models.JSONField(null=True, default={"address": [{"title": "خانه",
                                                                "full_name": "عمران بلوری",
                                                                "email": "em@gmail.com",
                                                                "call_number": "09372115747",
                                                                "company_name": "namava",
                                                                "address": "مرزداران پشت قنادی ماهبانو",
                                                                "adder_address": "پلاک ۳ واحد ۷",
                                                                "State_id": "",
                                                                "cities_id": ""},
                                                               {"title": "خانه",
                                                                "full_name": "رضا بلوری",
                                                                "email": "fsa@gma.com",
                                                                "call_number": "0932214214",
                                                                "company_name": "ارشان",
                                                                "address": "اتوبان حکیم ",
                                                                "adder_address": "بن بست بهار",
                                                                "State_id": "",
                                                                "cities_id": ""}]})

    def __str__(self):
        return "{0}".format(self.user.profile.user.username)


class citiesModel(models.Model):
    id = models.IntegerField(primary_key=True)
    province_id = models.IntegerField()
    name = models.CharField(max_length=191)
    slug = models.CharField(max_length=191)
    active = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'cities'


class provincesModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=191)
    slug = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'provinces'

    '''
            def __str__(self):
            return "{0}".format(self.user.email)

        @receiver(post_save, sender=User)
        def user_is_created(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)
            else:
                instance.profile.save()
    '''
