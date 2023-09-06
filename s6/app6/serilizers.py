from rest_framework import serializers
from .models import SellerModel6

class SellerSerializer6(serializers.ModelSerializer):
    class Meta:
        model = SellerModel6
        fields = ("seller_txt6","pub_date6")