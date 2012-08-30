from django.contrib import admin
from .models import (Beverage, Redeem)

class RedeemInline(admin.TabularInline):
    model = Redeem


class BeverageAdmin(admin.ModelAdmin):
    inlines = [RedeemInline]


admin.site.register(Beverage, BeverageAdmin)
