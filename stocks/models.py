from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    information = models.CharField(max_length=255)
    last_refresh = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Stock Model'


class StockPart(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    open = models.PositiveIntegerField(default=0)
    high = models.PositiveIntegerField(default=0)
    low = models.PositiveIntegerField(default=0)
    close = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Stock Part Model'
