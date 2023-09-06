from django.shortcuts import get_object_or_404
from .models import SellerModel5
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SellerSerializer5

class ListQV5(APIView):
   
    def get(self, request):
        all_deta5 = SellerModel5.objects.all()
        result5 = SellerSerializer5(all_deta5, many=True)
        return Response(result5.data)
    
class DetailQV5(APIView):
    def get(self,request, *args, **kwargs):
        sellermodel5 = get_object_or_404(SellerModel5, id=kwargs['se5_id'])
        seller_dada5 = SellerSerializer5(sellermodel5) 
        return Response(seller_dada5.data)

class CreateQV5(APIView):
    def post(self,request):
        user_body5 = request.data
        serializer5 = SellerSerializer5(data=user_body5)
        if serializer5.is_valid:
            serializer5.save()
            return Response(serializer5.data)
        return Response({serializer5.errors})


