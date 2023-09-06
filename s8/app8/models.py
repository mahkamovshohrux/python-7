from django.db import models

# Create your models here.
class SellerModel8(models.Model):
    seller_txt8 = models.CharField(max_length=125)
    pub_date8 = models.DateTimeField("date published")


   
