def calculer_frais_livraison(poids, **options):
    frais = poids * 2
    if options.get("express"):
        frais = frais + 5
    if options.get("assurance"):
        frais = frais + 5
    if options.get("zone") == "internationale":
            frais = frais + 5
    return frais

print(calculer_frais_livraison(5, express=True, zone="internationale"))
print(calculer_frais_livraison(2))
print(calculer_frais_livraison(10, assurance=True))