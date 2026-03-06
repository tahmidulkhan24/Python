class dog:
    def sound(self):
        print("dog bark")
class cat:
    def sound(self):
        print("cat mew mew")

def make_sound(animal):
    animal.sound()

dog = dog()
cat = cat()

make_sound(dog)
make_sound(cat)