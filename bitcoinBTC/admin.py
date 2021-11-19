from django.contrib import admin
from django.db.models import fields
from .models import Currency



@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):



    class Meta:
        model = Currency
        fields = '__all__'
