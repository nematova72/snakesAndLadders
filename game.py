from board import Board
from player import Player
from dice import Dice

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = [Player(name) for name in players]
        self.winner = None

    def play(self):
        """O‘yinni boshlaydi va davom ettiradi"""
        while not self.winner:
            for player in self.players:
                input(f"{player.name}, zarni tashlash uchun Enter bosing...")
                dice_value = Dice.roll()
                print(f"{player.name} {dice_value} tashladi.")
                player.move(dice_value)
                player.position = self.board.check_snake_or_ladder(player.position)
                
                if player.position >= self.board.size:
                    self.winner = player.name
                    player.won = True
                    print(f"🎉 {player.name} g'olib bo'ldi! 🎉")
                    return
