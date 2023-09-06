from django.urls import path
from .views import ListQV,DetailQV

urlpatterns = [
    path("seller1/",ListQV.as_view()),
    path('det/<int:se_id>',DetailQV.as_view()),
   
]