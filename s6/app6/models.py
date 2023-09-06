from django.db import models

# Create your models here.
class SellerModel6(models.Model):
    seller_txt6 = models.CharField(max_length=125)
    pub_date6 = models.DateTimeField("date published")


   
