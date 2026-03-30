class Hero:

    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.lvl}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} наносит удар! Текущая сила: {self.strength}"

    def rest(self):
        self.health += 1
        return f"{self.name} отдыхает… Здоровье героя: {self.health}"

heroes = [
    Hero("Illidan", 100, 1000, 5000),
    Hero("Arthas", 90, 800, 4000)
]

for hero in heroes:
    print(hero.greet())
    print(hero.attack())
    print(hero.rest())
    print()

