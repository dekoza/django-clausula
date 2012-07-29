#coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .base import conditions

FUNCTION_CHOICES = (
    # to trzeba zastąpić wylistowaniem wsztstkich zgromadzonych funkcji.
    ('a','a'),
)

class Condition(models.Model):
    name = models.CharField(_('name'), max_length=250)
    function = models.CharField(_('function'), max_length=250, choices=conditions.choices())
    param = models.CharField(_('param'), max_length=250, help_text=_('Param to feed the function'))

    class Meta:
        verbose_name = _('condition')
        verbose_name_plural = _('conditions')

    def __unicode__(self):
        """
        Preferably object name should be resolved using its `function`'s helper
        """
        return self.name

    def resolve(self):
        """
        This is used to call linked function and pass it the object as parameter.
        It's up to programmer to do with the object whatever is needed
        (eg. get. `param` value or *_set relations).
        Function should return boolean value indicating whether the condition
        is met or not.
        """
        # return call_function(self.function, self)
        pass