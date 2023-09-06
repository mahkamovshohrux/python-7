from django.urls import path
from .views import ListQV5,DetailQV5

urlpatterns = [
    path("seller5/",ListQV5.as_view()),
    path('det5/<int:se5_id>',DetailQV5.as_view()),
   
]