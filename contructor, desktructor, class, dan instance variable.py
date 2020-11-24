class Hero: # template
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print ("membuat hero dengan nama " + inputName)
    #Desktruktor
    def __del__(self):
        class_name = self.__class__.__name__
        print("Sebuah Objek", class_name, ", yaitu", self.name, "dihapus")
#instansiasi
hero1 = Hero("snipper", 100, 10, 4)
print("Jumlah Hero :", Hero.jumlah)
hero2 = Hero("mirana", 100, 15,1)
print("Jumlah Hero :", Hero.jumlah)
hero3 = Hero("ucup", 1000, 100, 0)
print("Jumlah Hero :", Hero.jumlah)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

#delete

del hero1
print("jumlah Hero",Hero.jumlah)