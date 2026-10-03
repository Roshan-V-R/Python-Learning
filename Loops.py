#1.Write a loop that calculates the sum of all even numbers.
numbers = [4, 7, 2, 9, 12, 5, 8]
s=0
for i in numbers:
    if i % 2 == 0:
        s=s+i
print(s)

#The number of students who passed (score >= 60)
#The average score of the students who passed
scores = [45, 72, 88, 51, 93, 67, 39, 81]
count = 0
total = 0
for score in scores:
    if score >= 60:
        count+=1
        total+=score
avg = total/count
print("Number passed: ",count)
print("Average: ",avg)

#Using only a for loop and conditions:
#1. Count how many valid readings there are.
#2. Calculate the average of the valid readings.
#3. Print both.
readings = [23, 25, -2, 31, None, 28, 105, 30, -5, 27, None, 32]
count = 0
total = 0
for i in readings:
    if i is not None:
        if 0< i< 100:
            count+=1
            total+=i
average = total/count
print('Valid Readings: ',count)
print("Average",average)