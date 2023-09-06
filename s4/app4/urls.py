from django.urls import path
from .views import ListQV4,DetailQV4

urlpatterns = [
    path("seller4/",ListQV4.as_view()),
    path('det4/<int:se4_id>',DetailQV4.as_view()),
   
]