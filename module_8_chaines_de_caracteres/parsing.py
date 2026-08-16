def parser_log(ligne):
    morceaux = ligne.split("|")
    date = morceaux[0]
    niveau = morceaux[1]
    message = morceaux[2]
    user_id_brut = morceaux[3]
    cle, valeur = user_id_brut.split("=")
    return {
        "date": date,
        "niveau": niveau,
        "message": message,
        "user_id": valeur
    }

ligne = "2026-08-03|ERROR|Connexion refusee|user_id=4521"
print(parser_log(ligne))