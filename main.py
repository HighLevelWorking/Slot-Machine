import random

user_input_money = None
slot1 = None
slot2 = None
slot3 = None

current_balance = 0

def not_zero():
    global current_balance
    global user_input_money
    while True:
        try:
            user_input_money = int(input("Place your bet amount: "))
            if user_input_money <= current_balance:
                return user_input_money
            else:
                print(f"You can only bet amount equal to or less than your current balance which is: {current_balance}")
        except:
            print("You can only use integer values")

def zero():
    while True:
        try:
            user_input = int(input("What is the balance you would like to insert into the slot machine: "))
            return user_input
        except:
            print("Only use integers")

def spinning_gambling():
    global slot1
    global slot2
    global slot3
    symbol = ("🍒", "🍉", "🥭", "🔔", "⭐")
    print("******************************")
    slot1 = random.choice(symbol)
    slot2 = random.choice(symbol)
    slot3 = random.choice(symbol)
    print(slot1, end = " ")
    print(slot2, end = " ")
    print(slot3)
    print("******************************")

def win_loose():
    global current_balance
    global slot1
    global slot2
    global slot3
    global user_input_money
    if slot1 == "🍒" and slot2 == "🍒" and slot3 == "🍒":
        current_balance = int(current_balance * 1.25)
        print(f"You won! Your balance has been increased to {current_balance}")
    elif slot1 == "🍉" and slot2 == "🍉" and slot3 == "🍉":
        current_balance = int(current_balance * 1.51)
        print(f"You won! Your balance has been increased to {current_balance}")
    elif slot1 == "🥭" and slot2 == "🥭" and slot3 == "🥭":
        current_balance = int(current_balance * 1.766)
        print(f"You won! Your balance has been increased to {current_balance}")
    elif slot1 == "🔔" and slot2 == "🔔" and slot3 == "🔔":
        current_balance = int(current_balance * 2)
        print(f"You won! Your balance has been increased to {current_balance}")
    elif slot1 == "⭐" and slot2 == "⭐" and slot3 == "⭐":
        current_balance = int(current_balance * 5)
        print(f"You won! Your balance has been increased to {current_balance}")
    else:
        current_balance -= user_input_money
        print("Sorry, you lost this round.")

def ask_continue():
    user_answer = input("Do you want to spin again? (yes/no): ")
    return user_answer.strip().lower() == "yes"

def main():
    global current_balance
    print("******************************")
    print("Welcome to the Slot Machine")
    print("Symbols: 🍒 🍉 🥭 🔔 ⭐")
    print("******************************")
    if current_balance <= 0:
        current_balance = zero()
    while current_balance > 0:
        print(f"Current balance: {current_balance} Rs")
        not_zero()
        print("Spinning...\n")
        spinning_gambling()
        win_loose()
        if current_balance <= 0:
            print("You have run out of balance!")
            break
        if not ask_continue():
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()