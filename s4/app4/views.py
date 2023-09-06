from django.shortcuts import get_object_or_404
from .models import SellerModel4
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SellerSerializer4

class ListQV4(APIView):
   
    def get(self, request):
        all_deta4 = SellerModel4.objects.all()
        result4 = SellerSerializer4(all_deta4, many=True)
        return Response(result4.data)
    
class DetailQV4(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel4 = get_object_or_404(SellerModel4, id=kwargs['se4_id'])
        seller_dada4 = SellerSerializer4(sellermodel4) 
        return Response(seller_dada4.data)

class CreateQV4(APIView):
    def post(self,request):
        user_body4 = request.data
        serializer4 = SellerSerializer4(data=user_body4)
        if serializer4.is_valid:
            serializer4.save()
            return Response(serializer4.data)
        return Response({serializer4.errors})


