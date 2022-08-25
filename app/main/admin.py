from django.contrib import admin

from main.models import Crypto

# Register your models here.
@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    pass