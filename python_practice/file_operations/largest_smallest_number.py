l = [34,2,3,78,21,45,19,10,67,4]

# finding largest number in the list
largest_number = l[0]
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        temp = l[i]
    else:
        temp = l[i+1]
    if temp > largest_number:
        largest_number = temp

print(largest_number)

smallest_number = l[0]
#smallest number
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        temp = l[i]
    else:
        temp = l[i+1]
    if temp < smallest_number:
        smallest_number = temp
print(smallest_number)

