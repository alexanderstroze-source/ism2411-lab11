# Reflection
# 1. I would use .get() for an optional field like email because a customer
# can still place an order without it. I would use brackets for a required
# field like an order ID so I can catch a missing ID before processing the order.
#
# 2. This reminds me of an Excel PivotTable with region in Rows and sales
# in Values. With Python, I can run the same loop on a new batch of sales
# and keep just one running total per region as I go.

# --------Exercise 1--------
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# --------Exercise 2--------
customer["phone"] = "555-0101"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# --------Exercise 3--------
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error}")

# --------Exercise 4--------
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over the dictionary gives only keys. Using .items() gives both
# the key and its value on each pass.
for key in customer:
    print(key)
