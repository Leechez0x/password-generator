import json

customer= {
    "id": 1,
    "name": "Leechez Ogo",
    "phone": "08136445689",
    "is_vip": True,
    "email": None,
    "purchases": [
        {"product": "A bag of Garri", "amount": 80000},
        {"product": "A dozen of drinks", "amount": 79000},
    ],
}

 
print(json.dumps(customer, indent =2))


text = '{"shop": "Ade Electronics", "sales": [{"amount": 1200}, {"amount": 800}]}'

data = json.loads(text)

total = 0
for sale in data["sales"]:
    total = total + sale["amount"]


print(f"The Total sales for {data["shop"]} is: {total} ")