#coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .base import clauses, autodiscover

autodiscover()
FUNCTION_CHOICES = clauses.choices()

class Condition(models.Model):
    """
    This is a concrete condition that will be stored in the database.

    .. py:attribute:: name
       Name of the condition.

    .. py:attribute:: clause
       The function that will be invoked to resolve the condition.

    .. py:attribute:: param
       Parameter that will be passed to the function to make it concrete.

    """
    name = models.CharField(_('name'), max_length=250)
    clause = models.CharField(_('clause'), max_length=250, choices=FUNCTION_CHOICES, blank=True)
    param = models.CharField(_('param'), max_length=250, help_text=_('Param to feed the function'), blank=True)

    class Meta:
        verbose_name = _('condition')
        verbose_name_plural = _('conditions')
        ordering = ['clause', 'param']

    def __unicode__(self):
        return self.name

    def resolve(self, *args, **kwargs):
        """
        This is used to import linked function and pass it the object.
        It's up to programmer to do with the object whatever is needed
        (eg. get. `param` value or *_set relations or work with concrete objects
        passed via kwargs).

        Function should return boolean value indicating whether the condition
        is met or not.
        """
        from django.utils.importlib import import_module

        s = self.clause.split('.')
        mod, f = '.'.join(s[:-1]), s[-1]
        mod = import_module(mod)
        f = getattr(mod, f)  # lambda: False to fail silently
        return f(self, *args, **kwargs)
