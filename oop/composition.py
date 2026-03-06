class Engine:
    def start(self):
        print("engine start")

class car:
    def __init__(self):
        self.engine = Engine()   # composition

    def start_car(self):
        self.engine.start()
        print("Car started")

c=car()
c.start_car()