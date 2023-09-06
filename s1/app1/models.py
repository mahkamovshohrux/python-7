from django.db import models

# Create your models here.
class SellerModel1(models.Model):
    seller_txt = models.CharField(max_length=125)
    pub_date = models.DateTimeField("date published")


   
