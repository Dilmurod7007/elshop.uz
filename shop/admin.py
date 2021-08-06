from django.contrib import admin
from .models import Mahsulot, Toifa

# Register your models here.

# admin.site.register(Mahsulot)
# admin.site.register(Toifa)


class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narx', 'soni',)


class ToifaAdmin(admin.ModelAdmin):
    list_display = ('nomi',)

admin.site.register(Mahsulot, MahsulotAdmin)
admin.site.register(Toifa, ToifaAdmin)