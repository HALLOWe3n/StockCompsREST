from rest_framework import routers

from stocks.views import StockInformationAPIView, StockInformationModelViewSet

route = routers.SimpleRouter()
route.register('list', StockInformationModelViewSet, basename='list_urls')

urlpatterns = route.urls

