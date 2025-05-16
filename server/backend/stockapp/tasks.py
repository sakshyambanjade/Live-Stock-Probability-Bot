from celery import shared_task
import requests
from .models import StockData

API_KEY = 'd0j2rbhr01ql09hpr0s0d0j2rbhr01ql09hpr0sg'  # replace with your actual API key
SYMBOL = 'NVDA'

@shared_task
def fetch_stock_data():
    url = f'https://finnhub.io/api/v1/quote?symbol={SYMBOL}&token={API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Basic prediction logic (example):
    high = data.get('h')
    low = data.get('l')
    current = data.get('c')

    if current >= high * 0.95:
        prediction = 'High'
    elif current <= low * 1.05:
        prediction = 'Low'
    else:
        prediction = 'Stable'

    # Save to DB
    StockData.objects.create(
        symbol=SYMBOL,
        current_price=current,
        high=high,
        low=low,
        prediction=prediction
    )
