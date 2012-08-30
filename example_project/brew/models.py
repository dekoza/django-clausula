from django.db import models
from clausula.models import Condition

class Beverage(models.Model):
    name = models.CharField(max_length=30)
    normal_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return self.name


class Redeem(models.Model):
    value = models.DecimalField(max_digits=7, decimal_places=2)
    beverage = models.ForeignKey(Beverage)
    condition = models.ForeignKey(Condition)

    def __unicode__(self):
        return "%s %s %s" % (self.value, self.beverage, self.condition)