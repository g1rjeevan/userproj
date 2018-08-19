# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True,verbose_name="Payment ID")
    payment_date = models.DateField(blank=True, default=datetime.date.today, verbose_name="Payment Date")
    amount = models.PositiveIntegerField(blank=True,verbose_name="Amount")
    b_id = models.ForeignKey('payments.Contract', related_name='B_Id_Payment', on_delete=models.CASCADE, null=False )

    def __getitem__(self, key):
        return getattr(self, key)

class Contract(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="B_Id")
    name = models.CharField(blank=False, max_length=50)

class Service(models.Model):
    service_name = models.CharField(blank=False, max_length=50, verbose_name="Service Name")
    price = models.PositiveIntegerField(blank=True,verbose_name="Price")
    b_id = models.ForeignKey('payments.Contract', related_name='B_Id_Service', on_delete=models.CASCADE, null=False)
