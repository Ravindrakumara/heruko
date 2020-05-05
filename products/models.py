
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.shortcuts import reverse
from django.urls import reverse
# Create your models here.


class Brands(models.Model):
   Brand_Name = models.CharField(max_length=100)
  

class Categories(models.Model):
   Category_Name = models.CharField(max_length=100)

class item(models.Model):

    Item_Name = models.CharField(max_length=80)
    Image = models.ImageField(upload_to='pics')
    Price = models.DecimalField(max_digits=100,decimal_places=2)
    Discount = models.DecimalField(max_digits=100,decimal_places=2)
    slug = models.SlugField(max_length=80)
    #Brand_Name = models.CharField(max_length=80)
    #Category_Name = models.CharField(max_length=80)
    Colour = models.CharField(max_length=80)
    Size = models.CharField(max_length=80)
    Weight = models.FloatField()
    Discription = models.TextField(max_length=80)
    Modify_date = models.DateTimeField()
    Expiry_date = models.DateTimeField()
    Create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.Item_Name

    def get_absolute_url(self):
        return reverse("products:pro", kwargs={
            'slug': self.slug
        })
#def get_absolute_url(self):
        #return reverse("products:pro", kwargs={
            #'slug': self.slug
        #})

#def get_absolute_url(self):
	#return reverse("products:pro", kwargs={"id": self.id})

def get_add_to_cart_url(self):
  return reverse("products:add-to-cart", kwargs={"slug": self.slug})


class Registration(models.Model):

   # Logo = models.ImageField(upload_to='pics')
    Sitemoto = models.CharField(max_length=100)
    Phonenumber = models.CharField(max_length=100)
    Email = models.EmailField()
    Address = models.TextField(max_length=150)
    Facebook = models.URLField()
    Twitter = models.URLField()
    Googlepls = models.URLField()
    linkedin = models.URLField()

class User(models.Model):
   FirstName = models.CharField(max_length=100)
   LastName = models.CharField(max_length=100)
   UserName = models.OneToOneField(
       settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   Email = models.EmailField()
   Phonenumber = models.TextField()
   Password = models.CharField(max_length=50)
   RePassword = models.CharField(max_length=50)

class Address(models.Model):
   UserName = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
   street_address = models.CharField(max_length=100)
   apartment_address = models.CharField(max_length=100)
   country = CountryField(multiple=True)
   zip = models.CharField(max_length=100)
   address_type = models.CharField(max_length=10)
   default = models.BooleanField(default=False)

class Cart(models.Model):
  Item_Name = models.ForeignKey(item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  Total_Price = models.DecimalField(decimal_places = 2, max_digits = 1000)

class OrderItem(models.Model):
    UserName = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    Item_Name = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
  """docstring for Oder"""
  items = models.ManyToManyField(OrderItem)
  start_date = models.DateTimeField(auto_now_add=True)
  ordered_date = models.DateTimeField()
  ordered = models.BooleanField(default=False)
    

