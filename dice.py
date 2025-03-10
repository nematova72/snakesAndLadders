import random

class Dice:
    @staticmethod
    def roll():
        """Tasodifiy 1 dan 6 gacha zar tashlaydi"""
        return random.randint(1, 6)
