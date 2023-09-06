from django.shortcuts import get_object_or_404
from .models import SellerModel6
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizers import SellerSerializer6

class ListQV6(APIView):
   
    def get(self, request):
        all_deta6 = SellerModel6.objects.all()
        result6 = SellerSerializer6(all_deta6, many=True)
        return Response(result6.data)
    
class DetailQV6(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel6 = get_object_or_404(SellerModel6, id=kwargs['se6_id'])
        seller_dada6 = SellerSerializer6(sellermodel6) 
        return Response(seller_dada6.data)

class CreateQV(APIView):
    def post(self,request):
        user_body6 = request.data
        serializer6 = SellerSerializer6(data=user_body6)
        if serializer6.is_valid:
            serializer6.save()
            return Response(serializer6.data)
        return Response({serializer6.errors})


