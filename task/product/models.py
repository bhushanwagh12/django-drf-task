from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    unique_id = models.IntegerField(unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product"

class ProductImage(models.Model):
    product =  models.ForeignKey(Product,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_image/')