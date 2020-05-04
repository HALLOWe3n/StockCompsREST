from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.export_temp import export_data
from stocks.models import Stock
from stocks.serializers import StockSerializer


# CRUD
class StockInformationModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class StockInfoExportAPIView(APIView):
    def get(self, request, version):
        return Response({'status': 'success'}, status=200) if export_data() else Response({'status': 'fail'}, status=400)
