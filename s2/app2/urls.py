from django.urls import path
from .views import ListQV2,DetailQV2

urlpatterns = [
    path("seller2/",ListQV2.as_view()),
    path('det2/<int:se2_id>',DetailQV2.as_view()),
   
]