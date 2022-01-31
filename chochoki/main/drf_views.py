import json

from django.contrib.auth.models import User as DUser
from django.core.handlers.wsgi import WSGIRequest
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
        if name not in json.loads(User.objects.get(username=username).games_settings):
            return Response({'detail': 'game incorrect'})
        return Response(json.loads(User.objects.get(username=username).games_settings)[name])

    def post(self, request: WSGIRequest, name, username, password):
        a = json.dumps(dict(request.POST))
        try:
            user = DUser.objects.get(username=username)
        except DUser.DoesNotExist:
            return Response({'detail': 'username incorrect'})
        user.games_settings = a
        user.save()
        return self.get(request, name, username, password)
