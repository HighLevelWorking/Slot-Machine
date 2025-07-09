current_balance = 0

def not_zero():
    global current_balance
    current_balance -= 10

def zero():
    while True:
        try:
            user_input = int(input("What is the balance you would like to insert into the slot machine: "))
            return user_input
        except:
            print("Only use integers")

def main():
    while True:
        global current_balance
        print("******************************")
        print("Welcome to the Slot Machine")
        print("Symbols: 🍒 🍉 🥭 🔔 ⭐")
        print("******************************")
    
        if current_balance <= 0:
            current_balance = zero()
            print(current_balance)
        else:
            not_zero()
            print(current_balance)

if __name__ == "__main__":
    main()