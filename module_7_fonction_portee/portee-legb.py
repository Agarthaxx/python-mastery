stock_global = {"tshirt": 50}

def applique_promo():
    stock_global = {"tshirt": 999}
    print(stock_global["tshirt"])

applique_promo()
print(stock_global["tshirt"])