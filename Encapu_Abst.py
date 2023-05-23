class Phone:
    def __init__(self,brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        
    def make_a_call(self,ph_no):
        print(f"calling {ph_no} ... ")


    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass

p1=Phone('Apple','13promax',175000)
# print(p1.price)
# print(p1.full_name)
# print(p1.make_a_call)
# print(p1.send_message)

print(p1.__dict__)