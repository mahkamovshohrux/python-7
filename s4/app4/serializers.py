from rest_framework import serializers
from .models import SellerModel4

class SellerSerializer4(serializers.ModelSerializer):
    class Meta:
        model = SellerModel4
        fields = ("seller_txt4","pub_date4")