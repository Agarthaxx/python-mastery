class OperationError(Exception):
    pass

class StringSyntaxError(Exception):
    pass

def traiter_paiement(montant, montant_paye):
    operation = None
    try:
        if not isinstance(montant_paye, (int, float)):
            raise StringSyntaxError("Le montant tapé n'est pas un nombre.")

        if montant_paye < montant:
            raise OperationError("Le montant est insuffisant.")

        operation = montant_paye - montant
    except StringSyntaxError as e:
        print(f"Erreur: {e}")
    except OperationError as e:
        print(f"Erreur: {e}")
    else:
        print(f"La monnaie est de : {operation}")
    finally:
        print("La transaction est terminée.")


traiter_paiement(100,200)
traiter_paiement(100, "abc")
traiter_paiement(200,100)