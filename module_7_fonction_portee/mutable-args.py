def ajouter_au_panier(article, panier=None):
    if panier is None:
        panier = []
    panier.append(article)
    return panier

panier_client_1 = ajouter_au_panier("clavier")
panier_client_2 = ajouter_au_panier("souris")

print(panier_client_1)
print(panier_client_2)