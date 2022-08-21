class Fighter:
    health = 50
    is_alive = True

    def __init__(self, health, attack, is_alive):
        self.health = health
        self.attack = attack
        self.is_alive = is_alive


warrior = Fighter(Fighter.health, 5, Fighter.is_alive)
knight = Fighter(Fighter.health, 7, Fighter.is_alive)


def fight():
    raund = 1
    while knight.is_alive or warrior.is_alive:

        if knight.health <= 0:
            knight.is_alive = False
            break
        if warrior.is_alive:
            knight.health = knight.health - warrior.attack
        if warrior.health <= 0:
            warrior.is_alive = False
            break
        if knight.is_alive:
            warrior.health = warrior.health - knight.attack

        print(raund, knight.health, warrior.health)

        raund += 1


fight()

print(warrior.is_alive, knight.is_alive)

if warrior.is_alive == False and knight.is_alive == True:
    print("Warrior is the loser and Knight is the winner")
if warrior.is_alive == True and knight.is_alive == False:
    print("Warrior is the winner and Knight is the loser")
