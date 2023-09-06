from django.db import models

# Create your models here.
class SellerModel4(models.Model):
    seller_txt4 = models.CharField(max_length=125)
    pub_date4 = models.DateTimeField("date published")


   
