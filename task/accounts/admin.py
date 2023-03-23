from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserLogin)
admin.site.register(CartProduct)
admin.site.register(CartModel)




