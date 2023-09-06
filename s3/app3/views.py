from django.shortcuts import get_object_or_404
from .models import SellerModel3
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SellerSerializer3

class ListQV3(APIView):
   
    def get(self, request):
        all_deta3 = SellerModel3.objects.all()
        result3 = SellerSerializer3(all_deta3, many=True)
        return Response(result3.data)
    
class DetailQV3(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel3 = get_object_or_404(SellerModel3, id=kwargs['se3_id'])
        seller_dada3 = SellerSerializer3(sellermodel3) 
        return Response(seller_dada3.data)

class CreateQV3(APIView):
    def post(self,request):
        user_body3 = request.data
        serializer3 = SellerSerializer3(data=user_body3)
        if serializer3.is_valid:
            serializer3.save()
            return Response(serializer3.data)
        return Response({serializer3.errors})


