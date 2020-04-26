from django.urls import path

from stocks.views import HelloUserAPIView

urlpatterns = [
    path('hello/', HelloUserAPIView.as_view(), name='hello_path')
]
