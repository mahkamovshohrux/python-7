from django.db import models

# Create your models here.
class SellerModel3(models.Model):
    seller_txt3 = models.CharField(max_length=125)
    pub_date3 = models.DateTimeField("date published")


   
