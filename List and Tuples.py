#Create a new list containing only the valid readings.
readings = [23, 25, -1, 27, None, 30, -5, 28, None, 31]
new = []
for r in readings:
    if r is not None and r > 0:
        new.append(r)
print(new)

#A collection containing all temperatures above 30
#For each valid temperature, store its temperature and its position/index together.
temp = []
temperatures = [28, 31, 29, 35, 27]
for index, t in enumerate(temperatures):
    if t > 30:
        temp.append((t,index))
print(temp)

