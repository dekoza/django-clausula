#coding: utf-8
"""
At the moment there is but one template tag to resolve a `Condition`.
"""

from django import template
from copy import copy

register = template.Library()

@register.assignment_tag(takes_context=True)
def check(context, clause, *args, **kwargs):
    """
    This tag resolves given `Condition` feeding it with args, kwargs
    and template's context. Params passed via kwargs override their
    context counterparts if any.
    """
    kw = copy(context)
    kw.update(kwargs)
    return clause(*args, *kw)
