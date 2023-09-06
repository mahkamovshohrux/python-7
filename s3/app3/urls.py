from django.urls import path
from .views import ListQV3,DetailQV3

urlpatterns = [
    path("seller3/",ListQV3.as_view()),
    path('det3/<int:se3_id>',DetailQV3.as_view()),
   
]