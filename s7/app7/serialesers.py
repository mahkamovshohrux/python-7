from rest_framework import serializers
from .models import SellerModel7

class SellerSerializer7(serializers.ModelSerializer):
    class Meta:
        model = SellerModel7
        fields = ("seller_txt7","pub_date7")