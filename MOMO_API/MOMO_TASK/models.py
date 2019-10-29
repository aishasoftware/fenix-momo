import datetime
from django.db import models


class MRequest(models.Model):  
        rid = models.CharField(max_length=50)  
        ramount = models.CharField(max_length=100)  
        rcurrency = models.CharField(max_length=50) 
        rexternalId = models.CharField(max_length=50)  
        rpartyIdType = models.CharField(max_length=50)
        rpartyId = models.CharField(max_length=50)
        rpayerMessage = models.CharField(max_length=50)
        rpayeeNote = models.CharField(max_length=50) 
        rstatus = models.CharField(max_length=50) 
        rtype = models.CharField(max_length=50)
        rcreationTime = models.DateTimeField(blank=True, null=True)
        rcompletionTime = models.DateTimeField(blank=True, null=True)

        class Meta:  
            db_table = "MRequest"  
