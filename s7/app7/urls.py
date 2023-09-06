from django.urls import path
from .views import ListQV7,DetailQV7

urlpatterns = [
    path("seller7/",ListQV7.as_view()),
    path('det7/<int:se7_id>',DetailQV7.as_view()),
   
]