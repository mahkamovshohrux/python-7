from rest_framework import serializers
from .models import SellerModel3

class SellerSerializer3(serializers.ModelSerializer):
    class Meta:
        model = SellerModel3
        fields = ("seller_txt3","pub_date3")