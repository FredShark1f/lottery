import random
number1 = random.randint(1,100)
number2 = random.randint(1,100)
number3 = random.randint(1,100)
for i in range(3):
    a = int(input())
    b = int(input())
    c = int(input())
    if a == number1 or a== number2 or a== number3:
        print("ты выйграл 1.000.000$")
        break
    else:
        print("X")

    if b == number1 or b == number2 or b == number3:
        print("ты выйграл 1.000.000$")
        break
    else:
        print("X")

    if c == number1 or c == number2 or c == number3:
        print("ты выйграл 1.000.000$")
        break
    else:
        print("X")
else:
    print("повезет в следующий раз ")
