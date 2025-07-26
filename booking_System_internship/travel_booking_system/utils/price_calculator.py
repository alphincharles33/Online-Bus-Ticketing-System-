# price_calculator.py
prices = {
    "Karwar": {"Karwar": 200, "Ankola": 150, "Mysore": 100},
    "Ankola": {"Bangalore": 200, "Ankola": 180, "Mysore": 120},
    "Bangalore": {"Bangalore": 150, "Karwar": 180, "Mysore": 80},
    "Mysore": {"Mysore": 100, "Ankola": 120, "Karwar": 80}
}

def calculate_price(source, destination):
    if source in prices and destination in prices[source]:
        return prices[source][destination]
    else:
        return None
