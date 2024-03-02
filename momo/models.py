from django.db import models

# Create your models here.


class Product(models.Model):
    title=models.CharField(max_length=50,default="")
    price=models.BigIntegerField(default="")
    category= models.ForeignKey('ProductCategory', on_delete=models.CASCADE,default="") 
    description=models.CharField(max_length=100,default="")
    slug= models.CharField(max_length=100,unique=True,default="")
    image=models.ImageField(upload_to='media',default="")
     
    def __str__(self):
        return "Message from " + self.title 
        
class ProductCategory(models.Model):
    name = models.CharField(max_length=50, default="")
    
    def __str__(self):
        return self.name
  