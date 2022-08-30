class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
     return self.health > 0

class Knight(Warrior):
    def __init__(self):

        super().__init__()
        self.attack = 7

chuck = Warrior()
#bruce = Warrior()
carl = Knight()
#dave = Warrior()
#mark = Warrior()

def fight(fght_1, fght_2):
    #raund = 1
    while fght_2.health > 0:
        if fght_1.is_alive():
           fght_1.health -= fght_2.attack
           print(fght_1.health, fght_2.health)
        else: return False

        if fght_2.is_alive():
           fght_2.health -= fght_1.attack


    return True


res = fight(chuck, carl)
print(res)

'''if __name__ == '__main__':

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False'''
