from rest_framework import serializers
from .models import SellerModel8

class SellerSerializer8(serializers.ModelSerializer):
    class Meta:
        model = SellerModel8
        fields = ("seller_txt8","pub_date8")