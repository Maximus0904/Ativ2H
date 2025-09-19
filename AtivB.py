print("Try programiz.pro")
import random
num = random.randint(1,100)
n2 = 0
while num != n2:
    n2 = int(input("Números = "))
    if n2 < num:
        print("É maior.")
    elif n2 > num:
        print("É menor.")
    else:
        print(f"Parabéns! Você acertou!O Número era {num}")
