#coding: utf-8
from django.db import models
from clausula.models import Condition

class Beverage(models.Model):
    name = models.CharField(max_length=30)
    normal_price = models.DecimalField(max_digits=7, decimal_places=2)


class Redeem(models.Model):
    value = models.DecimalField(max_digits=7, decimal_places=2)
    beverage = models.ForeignKey(Beverage, related_name='redeems')
    condition = models.ForeignKey(Condition)
