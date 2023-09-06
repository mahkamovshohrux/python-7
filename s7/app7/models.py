
from django.db import models

# Create your models here.
class SellerModel7(models.Model):
    seller_txt7 = models.CharField(max_length=125)
    pub_date7 = models.DateTimeField("date published")


   
