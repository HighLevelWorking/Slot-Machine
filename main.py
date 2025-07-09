import random


current_balance = 0

def not_zero():
    global current_balance
    while True:
        try:
            user_input = int(input("Place your bet amount: "))
            if user_input <= current_balance:
                return user_input
            else:
                print(f"You can only bet amount equal to or less then your current balance which is: {current_balance}")
        except:
            print("YOu can only use integer values")

def zero():
    while True:
        try:
            user_input = int(input("What is the balance you would like to insert into the slot machine: "))
            return user_input
        except:
            print("Only use integers")

def spinning_gambling():
    symbol = ("🍒", "🍉", "🥭", "🔔", "⭐")
    print("******************************")
    print(random.choice(symbol), end = " ")
    print(random.choice(symbol), end = " ")
    print(random.choice(symbol))
    print("******************************")


def main():
    while True:
        global current_balance
        print("******************************")
        print("Welcome to the Slot Machine")
        print("Symbols: 🍒 🍉 🥭 🔔 ⭐")
        print("******************************")
    
        if current_balance <= 0:
            current_balance = zero()
            print(f"Current balance: {current_balance} Rs")
            value_to_bet = not_zero()
            print("Spinning...")
            print()
            spinning_gambling()
            input()
        else:
            print(f"Current balance: {current_balance} Rs")
            value_to_bet = not_zero()
            print("Spinning...")

if __name__ == "__main__":
    main()