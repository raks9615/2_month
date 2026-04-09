# Наследование

# Родительский / Супер класс
class Hero:
    #Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты класса (динамические переменные)
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f"{self.name} hero base action!"


# Дочерний класс
class MageHero(Hero):

    def action(self):
        return f"{self.name} this is my base action!"


asuna = Hero("Asuno", 100,1000)

print(asuna.action())

