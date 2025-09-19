print("Exercício 5")
v_Acumuladora = 0
for _ in range(3):
    nota = float(input("Nota = "))
    v_Acumuladora += nota
media_final = v_Acumuladora/3
if media_final >= 7.0:
   print("Aprovado!")
elif media_final >= 5.0:
    print("Recuperação.")
else:
    print("Reprovado.")
