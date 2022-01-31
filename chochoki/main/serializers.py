from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'desc', 'img', 'time_create', 'time_update', 'is_published', 'html')
