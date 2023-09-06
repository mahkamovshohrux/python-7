from django.shortcuts import get_object_or_404
from .models import SellerModel7
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialesers import SellerSerializer7

class ListQV7(APIView):
   
    def get(self, request):
        all_deta7 = SellerModel7.objects.all()
        result7 = SellerSerializer7(all_deta7, many=True)
        return Response(result7.data)
    
class DetailQV7(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel7 = get_object_or_404(SellerModel7, id=kwargs['se7_id'])
        seller_dada7 = SellerSerializer7(sellermodel7) 
        return Response(seller_dada7.data)

class CreateQV7(APIView):
    def post(self,request):
        user_body7 = request.data
        serializer7 = SellerSerializer7(data=user_body7)
        if serializer7.is_valid:
            serializer7.save()
            return Response(serializer7.data)
        return Response({serializer7.errors})


