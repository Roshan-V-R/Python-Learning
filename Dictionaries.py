#1. Create a new list containing the names of people whose sales are greater than 1000.
sales = {
    "Alice": 1200,
    "Bob": 800,
    "Charlie": 1500,
    "David": 600,
    "Emma": 1100
}
result = []
for person in sales:
    if sales[person] > 1000:
        result.append(person)
print(result)

#2. Frequency Counting
numbers = [10, 15, 10, 20, 15, 10, 25, 20]
dict = {}
for i in numbers:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1
print(dict)

#3.Create a dictionary called results containing only students who passed.A student passes if their score is 60 or higher.
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91},
    {"name": "David", "score": 48},
    {"name": "Emma", "score": 76}
]

results = {}
for student in students:
    if student["score"] >= 60:
        results[student["name"]] = student["score"]
print(results)

