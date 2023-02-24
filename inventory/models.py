from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):

    NEW = 'new'
    REFURB = 'refurb'
    STATE = [
       (NEW, ('new')),
       (REFURB, ('refurb')),
   ]


    HP = 'hp'
    SAMSUNG = 'samsung'
    APPLE= 'apple'
    DELL = 'dell'
    LENOVO = 'lenovo'
    ACCESORY = 'accessory'
    TAG = [
        (HP,('hp')),
        (SAMSUNG, ('samsung')),
        (APPLE,('apple')),
        (DELL,('dell')),
        (LENOVO, ('lenovo')),
        (ACCESORY, ( 'accessory')),
   ]


    item_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    item_state = models.CharField(max_length=32,choices=STATE,default= NEW)
    item_category = models.ForeignKey(Category, related_name='items_cat', on_delete=models.CASCADE, null=True)
    item_image = models.ImageField(upload_to='images')
    item_tag =  models.CharField(max_length=32,choices=TAG,default= HP) 


    def __str__(self):
        return self.item_name


