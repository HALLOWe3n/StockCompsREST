from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloUserAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self):
        context = {'message': 'Hello!'}
        return Response(context)
