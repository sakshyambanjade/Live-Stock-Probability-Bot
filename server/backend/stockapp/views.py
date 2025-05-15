from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StockData
from .serializers import StockDataSerializer

@api_view(['GET'])
def get_latest_stock_data(request):
    latest_data = StockData.objects.last()
    serializer = StockDataSerializer(latest_data)
    return Response(serializer.data)
