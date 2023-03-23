from django.db import models

from product.models import Product

# Create your models here.



class User(models.Model):
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=20)
    is_customer = models.BooleanField()
    is_admin = models.BooleanField()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "User"

class UserProfile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    male = 'M'
    female = 'F'
    Others = 'Other Category'
    GENDER_CHOICES = [
        (male,'Male'),
        (female,'Female'),
        (Others,'Other Category')
    ]

    gender_choice = models.CharField(
        max_length=14,
        choices = GENDER_CHOICES,
        
    )

    image_field = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "User Profile"
    
class UserLogin(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        verbose_name_plural = "User Login"


class CartProduct(models.Model):
    owner =  models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    pending = 'pending'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (pending,'Pending'),
        (COMPLETED,'Completed'),
    ]
    status_choice = models.CharField(
        max_length=14,
        choices = STATUS_CHOICES,

        
    )
    class Meta:
        verbose_name_plural = "Cart Product"

class CartModel(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    products = models.ManyToManyField(CartProduct)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = "Cart"