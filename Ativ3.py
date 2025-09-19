print("Exercício 3")
numero_tabuada = int(input("Número para a tabuada = "))
i = 0
print(f"Tabuada do {numero_tabuada}:")
for _ in range(1,11):
    i += 1
    print(f" . {numero_tabuada} x {i} = {numero_tabuada*i}")
