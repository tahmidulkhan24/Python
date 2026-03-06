class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)

s1=student("labib",22)
s1.display()