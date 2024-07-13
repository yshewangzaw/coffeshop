from django.contrib import admin
from .models import Coffee

# Register your models here.
class coffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image')
admin.site.register(Coffee, coffeeAdmin)
