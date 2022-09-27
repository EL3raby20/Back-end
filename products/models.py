from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify

FLAG_OPTIONS=(
    
    ("New","New"),
    ("Sale","Sale"),
    ("Feature","Feature")


)
class Products(models.Model):
    name=models.CharField(max_length=200 , verbose_name=_("Name"))
    sku=models.IntegerField(_("sku"))
    img=models.ImageField(upload_to="Products/")
    subtitle=models.CharField(_("SubTitle"), max_length=500)
    descriptin=models.TextField(_("Descriptin"), max_length=5000)
    flag=models.CharField(_("Flag"), max_length=20, choices=FLAG_OPTIONS)
    price=models.FloatField(_("Price"))
    brand=models.ForeignKey('Brand',related_name="Products_brand",on_delete=models.SET_NULL, null=True,blank=True)
    category=models.ForeignKey('Category',related_name="Products_Category",on_delete=models.SET_NULL, null=True,blank=True)
    quantity=models.IntegerField(_("Quantity"))
    tags = TaggableManager()
    slug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs) 
  








class Brand(models.Model):
    name=models.CharField(_("Name"), max_length=200)
    img=models.ImageField(_("Image"),upload_to="Brands/")
    category=models.ForeignKey('Category',related_name="Brand_Category",on_delete=models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return (self.name)

     





class ProductsImges(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="Products_image")
    img=models.ImageField(upload_to="productimg/")

    def __str__(self):
        return str(self.product)


  



class Category(models.Model):
    name=models.CharField(_("Name"), max_length=200)
    img=models.ImageField(_("Image"),upload_to="Category/")

    def __str__(self):
        return (self.name)



class Reviwes(models.Model):
    user=models.ForeignKey(User,related_name="user_review",on_delete=models.CASCADE , verbose_name="User")
    product=models.ForeignKey(Products,related_name="product_review",on_delete=models.CASCADE, verbose_name="product")
    review=models.TextField(_("Review"), max_length=500)
    rate=models.IntegerField(_("Rate"),validators=(MinValueValidator(0),MaxValueValidator(5)))
    Create_at=models.TimeField(_("Create_at"),default=timezone.now)
    


    def __str__(self):
        return str(self.user)





