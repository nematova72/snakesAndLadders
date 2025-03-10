class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1  # O'yinchi 1-maydondan boshlaydi
        self.won = False

    def move(self, steps):
        """O'yinchini berilgan qadamga siljitish"""
        self.position += steps
        print(f"{self.name} {steps} ta qadam tashladi va {self.position}-maydonga o'tdi.")
