age = 120
if 0 < age <= 120:
    print("Valid")
else:
    print("Invalid")

#A customer is eligible for a special offer if:
#1. Their age is at least 18, AND
#2. They are either:
#   - a premium member, OR
#   - age is at least 35
customers = [
    {"name": "Alice", "age": 25, "premium": True},
    {"name": "Bob", "age": 17, "premium": False},
    {"name": "Charlie", "age": 35, "premium": False},
    {"name": "David", "age": 42, "premium": True},
]
names = []
for i in customers:
    if i["age"] >= 18 and (i["premium"] is True or i["age"]>=35):
        names.append(i["name"])
print(names)



