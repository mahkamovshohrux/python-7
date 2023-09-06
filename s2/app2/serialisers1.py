from rest_framework import serializers
from .models import SellerModel2

class SellerSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SellerModel2
        fields = ("seller_txt2","pub_date2")