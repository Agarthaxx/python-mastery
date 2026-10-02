def parser_liste(lignes):
    commandes_valides = []

    for i, ligne in enumerate(lignes, start=1):
        champs = ligne.split(";")

        if len(champs) != 3:
            print(f"Ligne {i} ignorée: champ de texte manquant. ({ligne!r})")
            continue

        id_cmd, produit, quantite_str = champs

        try:
            quantite = int(quantite_str)
        except ValueError:
            print(f"Ligne {i} ignorée: quantité non numérique. ({quantite_str!r})")
            continue

        commandes_valides.append({
            "id": id_cmd,
            "produit": produit,
            "quantite": quantite,
        })

    return commandes_valides

lignes = [
    "1;Casque;5",
    "2;Ecouteurs;abc",
    "3;Clavier;13",
    "4;Ecran;",
]

result = parser_liste(lignes)
print(result)