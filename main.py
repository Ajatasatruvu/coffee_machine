from coffee_machine import CoffeeMachine

def main():
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        choice = input()
        if choice == "exit":
            break
        else:
            machine.input_machine(choice)
            if machine.state == "Buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                choice = input()
                machine.input_machine(choice)
            elif machine.state == "Fill":
                print("Write how many ml of water do you want to add:")
                choice = input()
                machine.input_machine(choice)
                print("Write how many ml of milk do you want to add:")
                choice = input()
                machine.input_machine(choice)
                print("Write how many grams of coffee beans do you want to add:")
                choice = input()
                machine.input_machine(choice)
                print("Write how many disposable cups of coffee do you want to add:")
                choice = input()
                machine.input_machine(choice)
                       
                       
if __name__ == "__main__":
    main()
