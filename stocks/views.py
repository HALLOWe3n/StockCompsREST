from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from stocks.models import Stock
from stocks.serializers import StockSerializer


# CRUD
class StockInformationModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
