class Person:
    # definirea de atribute
    def __init__(self, name, age, city):  # initializez orice fel de atribute specifice
        self.name = name
        self.age = age
        self.location = city  # nu e obligatoriu ca denumirea de pe self sa fie egala cu denumirea param
        self._secret = (
            "secret"  # nu ar fi bine sa modific, e o conventie #var protejata
        )
        self.__really_secret = (
            "really secret"  # var cu doua underscoreuri in fata #var privata
        )

    def whoami(self):
        print(f"I am {self.name}")

    def present(self):
        print("Allow me to introduce myself.")
        self.whoami()

    def changename(self, newname):
        self.name = newname
        self.whoami()

    @staticmethod
    def st():
        print("ss")

    @classmethod
    def cls_meth(cls, a):
        print(cls)  # se pot folosi fara a instantia un obiect, doar avand clasa in sine


# pass nu are nimic de executat, sare peste tot, nu face nimic special


p1 = Person("andrei", 32, "tgjiu")  # o instanta a clasei, e un obiect
p1.present()
p1.changename("Robert")
p1.whoami()


# incapsulare, abstractizare, mostenire, polimorfism

# incap = aleg ce prop si ce metode sunt disp catre ext, aleg sa expun doar anumite date catre un consumator, iar altele sa le tin pt mine
# in python

# ABSTRACTIZARE =un mod de a crea tempalteuri cu anumite metode pe care suntem fortati sa le implementam

# mostenire, plec de la o clasa, pot crea o clasa care sa contina tot ce are vechea clasa +alte functionalitati noi


class Adult(Person):
    def __init__(self, name, age, city, address):
        super().__init__(name, age, city)
        self.address = address


a1 = Adult("Robert", 21, "Olt", "Acasa")
a1.whoami()
print(a1.address)


Person.cls_meth("string")
Person.st()
p1.cls_meth("string")


p2.Person("")
