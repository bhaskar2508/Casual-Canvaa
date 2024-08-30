from django.db import models

from django import forms
# Create your models here.

class LoginForm(forms.Form):
    username=forms.CharField(max_length=60)
    password=forms.CharField(max_length=60,widget=forms.PasswordInput())


from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=600)

    class Meta:
        db_table='Category'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='Product'

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
class Women(models.Model):
    productname=models.CharField(max_length=60)
    productprice=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='Ladies'

class WomenCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    women=models.ForeignKey(Women,on_delete=models.CASCADE)
    
class Kid(models.Model):
    name=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=10 , decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image' , default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='Kids'

class KidsCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    kid=models.ForeignKey(Kid,on_delete=models.CASCADE)

class EndSale(models.Model):
    product_name=models.CharField(max_length=60)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to='image',default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='Endsale'

class EndSaleCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    endsale=models.ForeignKey(EndSale,on_delete=models.CASCADE)

