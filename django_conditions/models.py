#coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_conditions.base import clauses

FUNCTION_CHOICES = clauses.choices()

print FUNCTION_CHOICES

class Condition(models.Model):
    """
    This a concrete condition that will be stored in the database.
    """
    name = models.CharField(_('name'), max_length=250)
    clause = models.CharField(_('clause'), max_length=250, choices=clauses.choices())
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
        This is used to import linked class and pass its `resolve` method
        the object as parameter. It's up to programmer to do with the object
        whatever is needed (eg. get. `param` value or *_set relations).
        `resolve` should return boolean value indicating whether the condition
        is met or not.
        """
        from django.utils.importlib import import_module

        s = self.clause.split('.')
        mod, cls = '.'.join(s[:-1]), s[-1]
        mod = import_module(mod)
        cls = getattr(mod, cls)
        # raise exception if cls has no resolve or fail silently?
        return cls.resolve(self)
