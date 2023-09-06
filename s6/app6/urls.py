from django.urls import path
from .views import ListQV6,DetailQV6

urlpatterns = [
    path("seller6/",ListQV6.as_view()),
    path('det6/<int:se6_id>',DetailQV6.as_view()),
   
]