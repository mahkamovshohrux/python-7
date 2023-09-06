from django.urls import path
from .views import ListQV8,DetailQV8

urlpatterns = [
    path("seller8/",ListQV8.as_view()),
    path('det8/<int:se8_id>',DetailQV8.as_view()),
   
]