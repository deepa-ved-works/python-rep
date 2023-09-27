class Car():
    def __init__(self):
        self.speed = 0
        self.running = False
    def start(self):
        self.running= True
    def drive(self):
        if self.running:
            print('Car is moving')
        else:
            print('Start the car first')

 class Taxi(Car):
    def __init__(self):
        Car.__init__(self)
        self.passenger  = None
        self.balance   = 0.0
    def drive(self):
        print('Honk honk, out of the way')
        Car.drive(self)
    def hire(self, passenger):
        print('Hired by', passenger)
        self.passenger = passenger
    def pay(self, amount):
        print('Paid', amount)
        self.balance = self.balance + amount
        self.passenger = None
class Limo(Taxi):
    def __init__(self):
        Taxi.__init__(self)
        self.sunroof = 'closed'
    def drive(self):
        print('Limo driving in luxury')
        Car.drive(self)
    def pay(self, amount, big_tip):
        print('Paid', amount, 'Tip', big_tip)
        Taxi.pay(self, amount + big_tip)
    def pour_drink(self):
        print('Pouring drink')
    def open_sunroof(self):
        print('Opening sunroof')
        self.sunroof = 'open'
    def close_sunroof(self):
        print('Closing sunroof')
        self.sunroof = 'closed'
car = Car
taxi = Taxi
limo = Limo
car.start()
car.drive()
taxi.start()
taxi.hire('Kim')
taxi.drive()
taxi.pay(5.0)
limo.start()
limo.hire('Jenn')
taxi.drive()
limo.pour_drink()
limo.pay(10.0, 5.0)