billets = ["valide", "valide", "annulé", "erreur", "valide", "valide"]

for x in billets:
    if x == "valide":
        print(x)
        continue
    elif x == "annulé":
        print(x)
        continue
    else:
        break
else:
    print("Traitement terminé sans incident.")

# Alternative Booléen

billets = ["valide", "valide", "annulé", "erreur", "valide", "valide"]

erreur_rencontree = False

for x in billets:
    if x == "valide":
        print(x)
        continue
    elif x == "annulé":
        print(x)
        continue
    else:
        erreur_rencontree = True
        break

if not erreur_rencontree:
    print("Traitement terminé sans incident.")