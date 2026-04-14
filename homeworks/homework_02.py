import random

class Hero:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("Герой атакует!")


class Warrior(Hero):
    def __init__(self):
        super().__init__("Warrior")

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self):
        super().__init__("Mage")

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self):
        super().__init__("Assassin")

    def attack(self):
        print("Ассасин атакует из-под тишка!")



warrior = Warrior()
mage = Mage()
assassin = Assassin()

heroes = [warrior, mage, assassin]


choice = input("Выбери: warrior / mage / assassin\n").lower()

if choice == "warrior":
    player = warrior
elif choice == "mage":
    player = mage
elif choice == "assassin":
    player = assassin
else:
    print("Ошибка")
    exit()

enemy = random.choice(heroes)

print("Ты выбрал:", player.name)
print("Противник:", enemy.name)


if player.name == enemy.name:
    print("Ничья")
elif (
    (player.name == "Warrior" and enemy.name == "Assassin") or
    (player.name == "Assassin" and enemy.name == "Mage") or
    (player.name == "Mage" and enemy.name == "Warrior")
):
    print("Ты победил!")
else:
    print("Ты проиграл!")

