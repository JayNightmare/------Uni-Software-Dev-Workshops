import json

with open('Epic 4/Workshop 8/Excersies/Exercise 3/rates.json') as file:
    data = json.load(file)

rates = data['rates']
gbp_to_target = {currency: (100 * rates[currency] / rates['GBP']) for currency in ['USD', 'EUR', 'JPY', 'CNY', 'BRL', 'SAR']}

for currency, amount in gbp_to_target.items():
    print(f"GBP 100 = {amount:.2f} {currency}")
