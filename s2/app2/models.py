from django.db import models

# Create your models here.
class SellerModel2(models.Model):
    seller_txt2 = models.CharField(max_length=125)
    pub_date2 = models.DateTimeField("date published")


   
