class CoffeeMachine:
    
    def __init__(self, water, milk, beans, cups, money, state="main_menu"):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = state
    
    def input_machine(self, option):
        if self.state == "main_menu":
            self.main_menu(option)
        elif self.state == "Buy":
            self.buy(option)
        elif self.state == "Fill":
            self.fill_water(int(option))
        elif self.state == "fill_milk":
            self.fill_milk(int(option))
        elif self.state == "fill_beans":
            self.fill_beans(int(option))
        else:
            self.fill_cups(int(option))
        
    def main_menu(self, option):
        if option == "buy":
            self.state = "Buy"
        elif option == "fill":
            self.state = "Fill"
        elif option == "take":
            self.take()
        elif option == "remaining":
            self.print_resources()
    
    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        self.state = "main_menu"
        
    def print_resources(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        self.state = "main_menu"
        
    def buy(self, option):
        if option == "1":
            not_enough = self.check([250, 0, 16, 1])
            if not not_enough:
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif option == "2":
            not_enough = self.check([350, 75, 20, 1])
            if not not_enough:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif option == "3":
            not_enough = self.check([200, 100, 12, 1])
            if not not_enough:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
        else:
            self.state = "main_menu"
            return
        
        if not_enough:
            print(f"Sorry, not enough {not_enough}!")
        else:
            print("I have enough resources, making you a coffee!")
        self.state = "main_menu"
            
    def check(self, cup_coffee_list):
        resources = [self.water, self.milk, self.beans, self.cups]
        index = 0
        result = None
        while index < len(resources):
            if resources[index] - cup_coffee_list[index] < 0:
                break
            index += 1
        if index == 0:
            result = "water"
        elif index == 1:
            result = "milk"
        elif index == 2:
            result = "beans"
        elif index == 3:
            result = "cups"
        return result
        
    def fill_water(self, quantity):
        self.water += quantity
        self.state = "fill_milk"
        
    def fill_milk(self, quantity):
        self.milk += quantity
        self.state = "fill_beans"
        
    def fill_beans(self, quantity):
        self.beans += quantity
        self.state = "fill_cups"
        
    def fill_cups(self, quantity):
        self.cups += quantity
        self.state = "main_menu"
