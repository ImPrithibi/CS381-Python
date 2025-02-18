def get_change(amount):
    coins = {
        "Half-dollars": 50,
        "Quarters": 25,
        "Dimes": 10,
        "Nickels": 5,
        "Pennies": 1
    }
    
    amount_in_cents = round(amount * 100)  # Convert dollars to cents
    change = {}
    
    for coin, value in coins.items():
        count = amount_in_cents // value
        if count > 0:
            change[coin] = count
        amount_in_cents %= value
    
    return change

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount of money: "))
        if amount < 0:
            print("Please enter a non-negative amount.")
        else:
            change = get_change(amount)
            print("Minimum number of coins required:")
            for coin, count in change.items():
                print(f"{coin}: {count}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
