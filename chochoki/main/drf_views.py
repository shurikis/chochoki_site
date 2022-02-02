import json

from django.contrib.auth.models import User as DUser
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class GameApiView(APIView):
    def get(self, request, game, username, password):
        try:
            user = DUser.objects.get(username=username)
        except DUser.DoesNotExist:
            return Response({'error': 'username incorrect'})
        if not user.check_password(password):
            return Response({'error': 'password incorrect'})
        if game not in json.loads(User.objects.get(username=username).games_settings):
            return Response({'error': 'game incorrect'})
        print(json.loads(User.objects.get(username=username).games_settings))
        return Response(json.loads(User.objects.get(username=username).games_settings)[game])

    def post(self, request: WSGIRequest, game, username, password):
        res = '{}'
        if 'json' in request.POST:
            res = request.POST['json']
        try:
            user = User.objects.get(username=username)
        except DUser.DoesNotExist:
            return Response({'error': 'username incorrect'})
        b = json.loads(user.games_settings)
        b[game] = dict(json.loads(res))
        user.games_settings = json.dumps(b)
        user.save()
        return self.get(request, game, username, password)
