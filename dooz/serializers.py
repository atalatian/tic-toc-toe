from rest_framework import serializers
from . import models


class GameHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameHistory
        fields = ["turn1", "turn2", "turn3",
                  "turn4", "turn5", "turn6",
                  "turn7", "turn8", "turn8",
                  "user",
                  "computer",
                  "row",
                  "starter",
                  "counter",
                  ]
