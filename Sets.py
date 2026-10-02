#Create a set containing only the unique email addresses.
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com",
    "d@gmail.com"
]
emails = set(emails)
c = 0
for email in emails:
    c+=1
print(emails)
print(c)

#2.Which customers appear in BOTH groups?
group_a = {"Alice", "Bob", "Charlie", "David"}
group_b = {"Charlie", "David", "Emma", "Frank"}
common = []
for i in group_a:
    if i in group_b:
        common.append(i)
print(set(common))

#3.Customers who are in Group A but NOT in Group B.
group_a = {"Alice", "Bob", "Charlie", "David"}
group_b = {"Charlie", "David", "Emma", "Frank"}
not_in = []
for i in group_a:
    if i not in group_b:
        not_in.append(i)
print(set(not_in))

