import json

class Board:
    def __init__(self, config_file="config.json"):
        self.size = 100  # O'yin maydoni 100 ta katak
        self.snakes, self.ladders = self.load_board_config(config_file)

    def load_board_config(self, config_file):
        """JSON fayldan ilon va narvonlar joylashuvini yuklaydi"""
        try:
            with open(config_file, "r") as file:
                config = json.load(file)
                return config["snakes"], config["ladders"]
        except FileNotFoundError:
            print("⚠️ Config fayli topilmadi, standart sozlamalar yuklanmoqda...")
            return {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}, \
                   {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def check_snake_or_ladder(self, position):
        """O'yinchining yangi joyini tekshirib, agar ilon yoki narvon bo‘lsa, o‘zgartiradi"""
        if position in self.snakes:
            print(f"🐍 Oh yo‘q! {position}-maydonda ilon bor! {self.snakes[position]}-maydonga tushib qoldingiz!")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"🪜 Ajoyib! {position}-maydonda narvon bor! {self.ladders[position]}-maydonga ko‘tarildingiz!")
            return self.ladders[position]
        return position
