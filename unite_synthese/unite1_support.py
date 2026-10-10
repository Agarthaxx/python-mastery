from decimal import Decimal, InvalidOperation

VENTES_BRUTES = """burger,2,9.50,carte
frites,1,3.50,especes
burger,1,9.50,especes
boisson,3,2.00,carte
frites,2,3.50,carte
burger,abc,9.50,carte
wrap,1,8.00,especes
boisson,2,2.00
burger,-1,9.50,carte
wrap,2,8.00,cheque
frites,4,3.50,especes

boisson,1,2.00,carte
burger,3,9.50,especes"""

MOYENS_VALIDES = {"carte", "especes"}
FOND_DE_CAISSE = "50.00"
ESPECES_COMPTEES = "111.50"


def lignes_non_vides(texte):
    resultat = []

    for ligne in texte.splitlines():
        if ligne:
            resultat.append(ligne)
    return resultat


def lire_vente(ligne):
    champs = ligne.split(",")

    if len(champs) != 4:
        raise ValueError("Champs manquants.")

    article, quantite_txt, prix_txt, paiement = champs

    try:
        quantite = int(quantite_txt)
    except ValueError:
        raise ValueError(f"Quantité non numérique. ({quantite_txt!r})")

    try:
        prix = Decimal(prix_txt)
    except InvalidOperation:
        raise ValueError(f"Le prix est non numérique. ({prix_txt!r})")

    if quantite <= 0:
        raise ValueError(f"Quantité <= 0. ({quantite!r})")
    if paiement not in MOYENS_VALIDES:
        raise ValueError(f"Le moyen de paiement est inconnu. ({paiement!r})")
    return {
        "article": article,
        "quantite": quantite,
        "prix": prix,
        "paiement": paiement,
    }


def agreger(texte):
    ca_total = Decimal("0")
    ca_par_paiement = {}
    ca_par_article = {}
    quantites = {}
    rejets = []

    for ligne in lignes_non_vides(texte):
        try:
            vente = lire_vente(ligne)
        except ValueError as erreur:
            rejets.append((ligne, str(erreur)))
            continue

        article = vente["article"]
        paiement = vente["paiement"]
        montant = vente["quantite"] * vente["prix"]

        ca_total += montant
        ca_par_paiement[paiement] = (
            ca_par_paiement.get(paiement, Decimal("0")) + montant
        )
        ca_par_article[article] = ca_par_article.get(article, Decimal("0")) + montant
        quantites[article] = quantites.get(article, 0) + vente["prix"]

    return {
            "ca_total": ca_total,
            "ca_par_paiement": ca_par_paiement,
            "ca_par_article": ca_par_article,
            "quantites": quantites,
            "rejets": rejets,
        }

def verdict_caisse(ca_especes):
    attendu = Decimal(FOND_DE_CAISSE) + ca_especes
    ecart = Decimal(ESPECES_COMPTEES) - attendu

    if ecart == 0:
        message = "Caisse juste, vous pouvez la cloturer."
    elif ecart > 0:
        message = f"Excédent de caisse: {ecart:,.2f}€"
    else:
        message = f"Trou de caisse, écart de: {ecart:,.2f}€"
    return attendu, message


def afficher_rapport(r):
    print("=== CLOTURE DE CAISSE ===")

    print(f"{'Article':<10}{'Qté':>5}{'CA':>10}")
    for article in sorted(r["ca_par_article"]):
        qte = r["quantites"][article]
        ca = r["ca_par_article"][article]
        print(f"{article:<10}{qte:>5}{ca:>10.2f}")

    print(f"\n{'Paiement':<10}{'CA':>15}")
    for paiement in sorted(r["ca_par_paiement"]):
        print(f"{paiement:<10}{r['ca_par_paiement'][paiement]:<15.2f}")

    print(f"\n{'TOTAL':<10}{r['ca_total']:>15.2f}")

    ca_especes = r["ca_par_paiement"].get("especes", Decimal("0"))
    attendu, message = verdict_caisse(ca_especes)
    print(f"Espèces attendues: {attendu:,.2f}€")
    print(f"Espèces comptées:  {Decimal(ESPECES_COMPTEES):,.2f}€")
    print('\n')
    print(message)
    
    print(f"\n{len(r['rejets'])} ligne(s) rejetée(s)")
    for ligne, raison in r["rejets"]:
        print(f" {ligne!r} --> {raison}")

rapport = agreger(VENTES_BRUTES)
afficher_rapport(rapport)
