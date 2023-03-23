from rest_framework import serializers
from .models import User,UserProfile,UserLogin,CartModel,CartProduct

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number','email']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = "__all__"

class CartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = "__all__"

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = "__all__"



