class SalleIndisponibleError(Exception):
    def __init__(self, message="Désolé, la salle est déjà réservée."):
        self.message = message
        super().__init__(self.message)


def reserver_salle(salle, creneau, reservations_existantes):
    for reservations in reservations_existantes:
        if reservations["salle"] == salle and reservations["creneau"] == creneau:
            raise SalleIndisponibleError(
                f"La salle {salle} est déjà prise sur le créneau {creneau}."
            )

    reservations_existantes.append(
        {
            "salle": salle,
            "creneau": creneau,
        }
    )
    print(f"Réservation confirmée: salle {salle}, creneau: {creneau}.")


reservations_existantes = [
    {"salle": "A1", "creneau": "10h-11h"},
    {"salle": "B2", "creneau": "14h-15h"},
]

tests = [("A1", "10h-11h"), ("A1", "11h-12h"), ("B2", "10h-11h")]

for salle, creneau in tests:
    try:
        reserver_salle(salle, creneau, reservations_existantes)
    except SalleIndisponibleError as e:
        print(f"Erreur: {e}")
