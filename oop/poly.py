class Animal:
    def sound(self):
        print("animal sound")
class dog(Animal):
    def sound(self):
        print("dog bark")
class cat(Animal):
    def sound(self):
        print("cat meu")

def make_sound(Animal):
    Animal.sound()

dog=dog()
cat=cat()
make_sound(dog)
make_sound(cat)
