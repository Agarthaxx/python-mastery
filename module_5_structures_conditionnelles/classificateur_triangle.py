"""a = 10

b = 20 

c = 30

if a == b and a == c:
    print("Le triangle est équilatéral")
elif a == b or b == c or a == c:
    print("Le triangle est isocèle")
else:
    print("Le triangle est un scalène")
"""
resultat_1 = 0 if True else "erreur"
resultat_2 = True and 0 or "erreur"

print(resultat_1,resultat_2)