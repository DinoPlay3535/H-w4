coin_a = int(input("Перша монета:"))
coin_b = int(input("Друга монета:"))
number = int(input("Число:"))
a = coin_a
b = coin_b
amount_1 = 0
amount_2 = 0
amount = 0

if coin_a >= coin_b:
    while coin_a <= number:
        number -= a
        amount_1 += 1
    while number > 0:
        number -= b
        amount_2 =+ 1
    amount = amount_1 + amount_2
    print(amount)

if coin_b >= coin_a:
    while coin_b <= number:
        number -= b
        amount_1 += 1
    while number > 0:
        number -= a
        amount_2 =+ 1
    amount = amount_1 + amount_2
    print(amount)