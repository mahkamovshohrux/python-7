from rest_framework import serializers
from .models import SellerModel1

class SellerSerializer1(serializers.ModelSerializer):
    class Meta:
        model = SellerModel1
        fields = ("seller_txt","pub_date")