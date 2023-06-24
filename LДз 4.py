import random
import time


class Players:
    def __init__(self, player_name, player_hp, player_damage):
        self.name = player_name
        self.damage = player_damage
        self.hp = player_hp
        self.lvl = 1
        self.exp = 0

    @staticmethod
    def create_heal():
        heal_type = {
            20: "Малая аптечка 🩹",
            40: "Аптечка 💊",
            60: "Большая аптечка 💉"
        }
        key_heal = random.choice(list(heal_type.keys()))
        hero.hp += key_heal
        return heal_type[key_heal]
    @staticmethod
    def create_weapon():
        weapon_type = ["АК-47","КВ-2","Пистолет-пулемёт","Миниган","Топор","Мачете","Селфи палка","Сковородка"]
        weapon_rare = {
            1: "Обычная",
            1.4: "Редкая",
            1.9: "Cупер редкая",
            2.4: "Мифическая",
            3.1: "Эпическая",
            4.8: "Легендарная",
            5.96: "Хроматическая"
        }
        weapon = random.choice(weapon_type)
        rare = random.choice(list(weapon_rare.keys()))
        if weapon == weapon_type[0]:
            hero.damage += 12 * rare
        elif weapon == weapon_type[1]:
            hero.damage += 123 * rare
        elif weapon == weapon_type[2]:
            hero.damage += 10 * rare
        elif weapon == weapon_type[3]:
            hero.damage += 42 * rare
        elif weapon == weapon_type[4]:
            hero.damage += 8 * rare
        elif weapon == weapon_type[5]:
            hero.damage += 9.5 * rare
        elif weapon == weapon_type[6]:
            hero.damage += 3.9 * rare
        elif weapon == weapon_type[7]:
            hero.damage += 9.7 * rare
        return weapon, weapon_rare[rare]



    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Вы нанесли {self.damage} урона!")
        time.sleep(0.7)
        if victim.hp <= 0:
            print(f"Победа над врагом! {victim.name} повержен.")
            time.sleep(0.7)
            item = random.randint(1,3)
            if item == 1:
                print(f"Вам выпала {self.create_heal()}\n"
                      f"ваше хп:{self.hp}")
            elif item == 2:
                weapon = self.create_weapon()
                print(f"Вам выпало оружие:{weapon[0]} редкости {weapon[1]}\n"
                      f"Урон:{self.damage}")
            elif item == 3:
                print(f"Вам ничего не выпало, повезёт в следуйщий раз. \n"
                      f"Ваш урон:{self.damage}, ваше здоровье:{self.hp}")

            return False

        elif victim.hp > 0:
            print(f"{victim.name}, осталось здоровья: {victim.hp}.")
            time.sleep(0.7)
            return True

    @staticmethod
    def create_player(player_name, player_race, player_class):
        hp = damage = 0
        player_name = player_name
        if player_race == races_list[0]:
            hp += 125
            damage += 100
        elif player_race == races_list[1]:
            hp += 55
            damage += 10
        elif player_race == races_list[2]:
            hp += 70
            damage += 35
        elif player_race == races_list[3]:
            hp += 100
            damage += 45
        else:
            print("Ошибка такой расы нету")
            quit()
        if player_class == class_list[0]:
            hp -= 15
            damage += 17
        elif player_class == class_list[1]:
            hp += 35
            damage += 6
        elif player_class == class_list[2]:
            hp -= 30
            damage += 37
        elif player_class == class_list[3]:
            hp += 70
            damage += 55
        elif player_class == class_list[4]:
            hp -= 40
            damage -= 5
        elif player_class == class_list[5]:
            hp += 100
            damage += 40
        else:
            print("Ошибка! Нет класса.")
            quit()
        return Players(player_name, hp, damage)


class Enemy:
    def __init__(self, enemy_name, enemy_hp, enemy_damage):
        self.name = enemy_name
        self.damage = enemy_damage
        self.hp = enemy_hp

    @staticmethod
    def create_enemy():
        enemy_names = ["Скелет", "Варден", "Вампир", "Стив", "Зоглин", "Оборотень", "Орк"]
        enemy_name = random.choice(enemy_names)
        enemy_hp = random.randint(10, 215)
        enemy_damage = random.randint(10, 105)
        return Enemy(enemy_name, enemy_hp, enemy_damage)

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Вы получили {self.damage} урона!")
        time.sleep(0.7)
        if victim.hp <= 0:
            print(f"Вы проиграли {victim.name}! {self.name} победил.")
            quit()
        elif victim.hp > 0:
            print(f"{victim.name}, у вас осталось: {victim.hp} здоровья.")
            time.sleep(0.7)


races_list = ["эльф", "гном", "хоббит", "человек"]
class_list = ["лучник", 'рыцарь', 'маг', 'копьетон', 'шахтер', 'гигант']

print("Здраствуй! Как вас зовут?")
name = input()

print("Какой расы будет твой персонаж?")
for race in races_list:
    print(race, end=" ")
print()
race = input().lower().replace(" ", "")

print("Какого класса будет твой персонаж?")
for x in class_list:
    print(x, end=" ")
print()
class_player = input().lower().replace(" ", "")

print(race, class_player)
hero = Players.create_player(name, race, class_player)
print(f"Ваше имя: {hero.name}\n"
      f"Хп персонажа: {hero.hp}\n"
      f"Урон героя: {hero.damage}")


def feh():
    answer = int(input(f"attack(1) run(2)\n"))
    if answer == 1:
        result_attack = hero.attack(enemy)
        if result_attack:
            enemy.attack(hero)
            feh()

    elif answer == 2:
        run = random.randint(1, 2)
        if run == 1:
            print("Побег удался")
            time.sleep(0.7)
        elif run == 2:
            print("Вас поймали")
            time.sleep(0.7)
            enemy.attack(hero)
            time.sleep(1)
            feh()


while True:
    event = random.randint(0, 3)
    if event == 0 or event == 2 or event == 3:
        print("Вы никого не встретили. Идем дальше...")
        time.sleep(0.75)
    elif event == 1:
        enemy = Enemy.create_enemy()
        print(f"Вас заметил {enemy.name}\n"
              f"Здоровье врага: {enemy.hp}\n"
              f"Урон врага: {enemy.damage}")
        feh()
