from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from stocks.models import Stock
from stocks.serializers import StockSerializer


class StockInformationModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


# CRUD
class StockInformationAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, version=None):
        # get all data from model
        stocks = Stock.objects.all()
        # pack data to JSON object
        serializer = StockSerializer(stocks, many=True)

        # Response JSON object to client
        return Response(data=serializer.data)

    def post(self, request, version=None):
        # Deserializer data
        serializer = StockSerializer(data=request.data)
        print(request.data)
        # check
        if serializer.is_valid():
            # save to db
            serializer.save()
            # return status of success
            return Response({'status': 200}, status=201)
        # return status of failed
        return Response({'status': 400}, status=400)

