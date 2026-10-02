"""
def diviser_stock(quantite_totale, nb_lots):
    return quantite_totale / nb_lots

print(diviser_stock(100,4))
print(diviser_stock(100,0))
print("Fin de programme")

Le programme plante car on effectue une division par 0,
je vous propose un programme fonctionnel en fonction des calculs demandés.
"""

def diviser_stock(quantite_totale, nb_lots):
    try:
        calcul = quantite_totale / nb_lots
        return calcul
    except ZeroDivisionError:
        print("\n")
        return "Fin du programme, on ne divise jamais par 0."

print(diviser_stock(100,4))
print(diviser_stock(100,0))