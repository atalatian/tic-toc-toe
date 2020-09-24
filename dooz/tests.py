from django.test import TestCase
from .models import GameHistory


class GameHistoryTestCase(TestCase):
    def test_setUp(self):
        history = GameHistory.objects.create(turn1=[1,1],turn2=[1,2],turn3=[1,3],turn4=[2,1]
                                   ,turn5=[2,2],turn6=[2,3],turn7=[3,1],turn8=[3,2]
                                   ,turn9=[3,3])
        self.assertEqual(history.turn1, [1, 1])
