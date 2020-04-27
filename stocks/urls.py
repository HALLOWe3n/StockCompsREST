from rest_framework import routers

from stocks.views import StockInformationModelViewSet

route = routers.SimpleRouter()
route.register('', StockInformationModelViewSet, basename='list_urls')

urlpatterns = route.urls
