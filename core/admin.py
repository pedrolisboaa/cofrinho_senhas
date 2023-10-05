from django.contrib import admin
from .models import Cofre

# Register your models here.
@admin.register(Cofre)
class CofreAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'site', 'senha']