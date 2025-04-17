from rest_framework import serializers
from ecom.models import Coupon, Product

class CouponSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(max_length=10)
    discount = serializers.IntegerField()
    active = serializers.BooleanField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields= '__all__'