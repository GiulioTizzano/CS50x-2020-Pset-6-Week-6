from cs50 import get_float

# prompting user to ask for change due,which must be greater than 0. Else, user is re-prompted
while True:
    price = get_float("Change owed: ")

    if price >= 0:
        break

coins = 0
price = round(price * 100)

while price >= 25:
    price -= 25
    coins += 1

while price >= 10:
    price -= 10
    coins += 1

while price >= 5:
    price -= 5
    coins += 1

while price >= 1:
    price -= 1
    coins += 1

print(coins)