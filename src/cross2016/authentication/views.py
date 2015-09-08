# encoding=utf-8

from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated

from .serializers import UserSerializer

class AuthView(APIView):

    def get(self, request, format=None):
        if not request.user.is_authenticated():
            raise NotAuthenticated()

        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request, format=None):
        return redirect("social:begin", backend="twitter")
