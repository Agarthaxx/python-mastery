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
    