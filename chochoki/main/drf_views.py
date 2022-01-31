import json

from django.contrib.auth.models import User as DUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class GameApiView(APIView):
    def get(self, request, name, username, password):
        try:
            user = DUser.objects.get(username=username)
        except DUser.DoesNotExist:
            return Response({'detail': 'username incorrect'})
        if not user.check_password(password):
            return Response({'detail': 'password incorrect'})
        return Response(json.loads(User.objects.get(username=username).games_settings)[name])
