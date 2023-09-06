from django.shortcuts import get_object_or_404
from .models import SellerModel1
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import SellerSerializer1

class ListQV(APIView):
   
    def get(self, request):
        all_deta = SellerModel1.objects.all()
        result1 = SellerSerializer1(all_deta, many=True)
        return Response(result1.data)
    
class DetailQV(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel1 = get_object_or_404(SellerModel1, id=kwargs['se_id'])
        seller_dada1 = SellerSerializer1(sellermodel1) 
        return Response(seller_dada1.data)

class CreateQV(APIView):
    def post(self,request):
        user_body = request.data
        serializer = SellerSerializer1(data=user_body)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response({serializer.errors})


