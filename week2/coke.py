coins = [25, 10, 5]
amount = 0

while amount < 50:
    print(f"Amount Due: {50 - amount}")
    coin = int(input("Insert Coin: "))

    if coin in coins:
        amount += coin

print(f"Change Owed: {amount - 50}")