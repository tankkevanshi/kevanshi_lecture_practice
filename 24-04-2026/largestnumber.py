# Find largest number of list

numbers = list (map (int , input ("Enter numbers:").split()))

largest = numbers [0]

for num in numbers:
    if num > largest:
        largest = num

print ("Largest:", largest)

# Find smallest number of list

numbers = list (map (int , input ("Enter numbers:").split()))

smallest = numbers [0]

for num in numbers:
    if num > smallest:
        smallest = num

print ("smallest:", smallest)
