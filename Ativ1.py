print("EXercício 1")
impar = 0 
par = 0
for _ in range(10):
    i = int(input(" Número = "))
    if i%2 == 0:
        par += 1
    else: 
        impar += 1
print(f"Números pares:{par}")
print(f"Números impares:{impar}")
