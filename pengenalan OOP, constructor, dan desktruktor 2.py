class Hero: # template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    #Desktruktor
    def __del__(self):
        class_name = self.__class__.__name__
        print("Sebuah Objek", class_name, ", yaitu", self.name, "dihapus")

#instansiasi
hero1 = Hero("snipper", 100, 10, 4)
hero2 = Hero("mirana", 100, 15,1)
hero3 = Hero("ucup", 1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

#delete

del hero1