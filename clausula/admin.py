#coding: utf-8

from django.contrib import admin
from .models import Condition

class ConditionAdmin(admin.ModelAdmin):
    list_display_links = ['clause']
    list_display = ('name', 'clause', 'param')
    list_editable = ('name', 'param')
    save_on_top = True
    search_fields = ['name', 'clause']

admin.site.register(Condition, ConditionAdmin)