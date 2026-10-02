"""
Exercice 3:
Tu recois une liste d'emails de clients ayant rempl un formulaire plusieurs fois par erreur :
emails = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com", "b@mail.com"]

Écris une fonction emails_uniques(emails) qui retourne la liste des emails sans doublons, en préservant l'ordre d'apparition
(donc pas juste list(set(emails)), qui casserait l'ordre). Utilise un set pour suivre ce qui a déjà été vu, en O(n).
"""

emails = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com", "b@mail.com"]

def emails_unique(emails):
    vus = set()
    resultat = []
    for email in emails:
        if email not in vus:
            vus.add(email)
            resultat.append(email)
    return resultat

print(emails_unique(emails))