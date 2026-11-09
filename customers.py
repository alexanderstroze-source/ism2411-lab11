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

# --------Exercise 5--------
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount_rate)
print(f"Tier: {tier}, discount: {discount_rate:.0%}, final price: ${final_price:.2f}")

# --------Exercise 6--------
customers = [
    customer,
    {"name": "Ben", "tier": "silver"},
    {"name": "Maya", "tier": "gold"},
]
for record in customers:
    tier = record["tier"]
    discount_amount = 300 * tier_discounts.get(tier, 0)
    print(f"{record['name']}, {tier}, discount: ${discount_amount:.2f}")

# --------Exercise 7--------
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} ({details['stock']} left)")

# --------Exercise 8--------
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + transaction["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
