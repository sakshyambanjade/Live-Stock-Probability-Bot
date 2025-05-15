from django.db import models

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    current_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    prediction = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} @ {self.current_price}"