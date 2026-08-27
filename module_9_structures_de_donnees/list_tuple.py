"""
Tu gères un système de commandes pour une boutique en ligne:
Pour chaque commande, tu stockes ses coordonnées de livraison : (latitude, longitude)
Pourquoi choisirais-tu un tuple plutôt qu'une liste pour stocker cette paire?
"""

"""
Réponse:
O1. On peut itérer sur la donnée ( tuple comme sur une liste ) mais on ne peut pas
la modifier. ( contrairement aux listes ).
02. La vraie raison technique: une coordonnée (longitude, latitude) est une unité logique,
indivisible. Si on pouvait faire : coordonnees[0] = 999, on se retrouverai des données invalide.
"""

coord = (49.59303, 2.40204)
for valeur in coord:
    print(valeur)
