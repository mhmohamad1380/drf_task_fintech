from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Crypto(models.Model):
    coin_name = models.CharField(
        max_length=120, null=True, blank=False, verbose_name="Coin Name")
    coin_price_source = models.CharField(
        max_length=120, null=True, blank=False, verbose_name="Coin Price Source")
    coin_price = models.PositiveIntegerField(verbose_name="Coin Price")
    coin_date_added = models.DateTimeField(auto_now_add=True)
    coin_date_changed = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.coin_name}, {self.coin_price}"

    def clean(self):
        if Crypto.objects.all().count() == 5:
            raise ValidationError("Model Count can not be more than 5: Please Delete data!!!")