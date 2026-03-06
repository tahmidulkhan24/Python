from abc import ABC,abstractmethod

class payment(ABC):
    def pay(self):
        pass
    
class credic(payment):
     def pay(self):
        print("Paid with credit card")

class PayPal(payment):

    def pay(self):
        print("Paid with PayPal")

p=credic()
p.pay()