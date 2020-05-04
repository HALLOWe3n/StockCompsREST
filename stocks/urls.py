from django.urls import path
from rest_framework import routers

from stocks.views import StockInformationModelViewSet, StockInfoExportAPIView

route = routers.SimpleRouter()
route.register('', StockInformationModelViewSet, basename='list_urls')

urlpatterns = route.urls
urlpatterns += [
    path('export/data/', StockInfoExportAPIView.as_view())
]
