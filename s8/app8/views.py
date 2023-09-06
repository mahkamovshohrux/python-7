from django.shortcuts import get_object_or_404
from .models import SellerModel8
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SellerSerializer8

class ListQV8(APIView):
   
    def get(self, request):
        all_deta8 = SellerModel8.objects.all()
        result8 = SellerSerializer8(all_deta8, many=True)
        return Response(result8.data)
    
class DetailQV8(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel8 = get_object_or_404(SellerModel8, id=kwargs['se8_id'])
        seller_dada8 = SellerSerializer8(sellermodel8) 
        return Response(seller_dada8.data)

class CreateQV8(APIView):
    def post(self,request):
        user_body8 = request.data
        serializer8 = SellerSerializer8(data=user_body8)
        if serializer8.is_valid:
            serializer8.save()
            return Response(serializer8.data)
        return Response({serializer8.errors})


