from unittest import TestCase
import game

class GameTest(TestCase):
    
    def test_join(self):
        """Players may join a game of Pig"""
        
        pig = game.Pig