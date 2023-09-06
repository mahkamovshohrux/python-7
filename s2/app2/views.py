from django.shortcuts import get_object_or_404
from .models import SellerModel2
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers1 import SellerSerializer2

class ListQV2(APIView):
   
    def get(self, request):
        all_deta = SellerModel2.objects.all()
        result1 = SellerSerializer2(all_deta, many=True)
        return Response(result1.data)
    
class DetailQV2(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel2 = get_object_or_404(SellerModel2, id=kwargs['se2_id'])
        seller_dada2 = SellerSerializer2(sellermodel2) 
        return Response(seller_dada2.data)

class CreateQV2(APIView):
    def post(self,request):
        user_body2 = request.data
        serializer2 = SellerSerializer2(data=user_body2)
        if serializer2.is_valid:
            serializer2.save()
            return Response(serializer2.data)
        return Response({serializer2.errors})


