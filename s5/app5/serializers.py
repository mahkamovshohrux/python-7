from rest_framework import serializers
from .models import SellerModel5

class SellerSerializer5(serializers.ModelSerializer):
    class Meta:
        model = SellerModel5
        fields = ("seller_txt5","pub_date5")