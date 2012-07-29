#coding: utf-8
"""
`django-conditions` is a pluggable app to allow adding various conditions
via Django's admin site. Abstracts for these conditions are defined in source
code and registered in similar fashion as admin models.

  .. moduleauthor:: Dominik Kozaczko <dominik@kozaczko.info>
"""
from .base import clauses