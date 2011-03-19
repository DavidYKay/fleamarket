from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Seller (models.User):
#    pass
#class Staff (models.User):
#    pass

#class SellerProfile(models.Model):
#    seller = models.ForeignKey(User, unique=True)
#    email = models.CharField(max_length=200)
#    phone_number = models.CharField(max_length=200)

class Item(models.Model):
    seller = models.ForeignKey(User)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    on_hand  = models.BooleanField()
    was_sold = models.BooleanField()
    def __unicode__(self):
        return self.description[:40]
