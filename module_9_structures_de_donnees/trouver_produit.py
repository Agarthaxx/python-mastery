"""
Exercice:
Ecrire une fonction trouver_produit qui retourne
le dictionnaire du produit correspondant, ou None si non trouvé.
"""

produits = [
    {"id": "P001", "nom": "Clavier", "prix": 45.0},
    {"id": "P002", "nom": "Souris", "prix": 15.0},
    {"id": "P003", "nom": "Ecran", "prix": 120.0},
]


def trouver_produit(produits, id_recherche):
    for i in produits:
        if i["id"] == id_recherche:
            return i
    return None


print(trouver_produit(produits, "P002"))

"""
Pourquoi une liste de 50 000 produits est un mauvais choix ?

Avec une liste, trouver_produit doit dans le pire des cas parcourir
tout les éléments un par un jusqu'à trouver une correspondance.
"""