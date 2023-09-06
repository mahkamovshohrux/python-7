from django.db import models

# Create your models here.
class SellerModel5(models.Model):
    seller_txt5 = models.CharField(max_length=125)
    pub_date5 = models.DateTimeField("date published")


   
