class People:
    def __init__(self, age:int):
        self.__age = age
        print(dir(self))

    # def __del__(self):
    #     print('Django')

    def sex(self, agePartner):
        if self.__age < 18 and agePartner - self.__age > 2:
            return "Pedophilia"
        return "Allow"
    @staticmethod
    def passportCheck():
        print("Privet")


    # def __str__(self):
    #     print("call str function")
    #     return f"{self}, info about class"

p = People(10)
# print(p._People__age)
# print(p.sex(20))
print(People.sex(p, 18))
People.passportCheck()
# print(p.passportCheck(1))