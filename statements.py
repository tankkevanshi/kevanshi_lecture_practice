#python statements

# if...statements

dooropen = False

if dooropen :
    print ("Welcome to Home")

else :
    print ("Meet me again tomorrow")

# cheak positive,nagative and zero

num = int(input ("Enteranumber:"))

if num >0:
    print (F"{num}positive Number")
elif num <0:
    print (f"{num}Nagative Number")
else :
    print("Zero")

# find Largest of two numbers

a = int (input ("Enter first number :"))
b = int (input ("Enter secound number:"))

if a>b :
    print ("Largest number is",a)
else :
    print ("Largest number is",b)

# cheak Leap year

year = int (input ("Enter year:"))
if (year% 4 ==0 and year % 100!=0)or (year % 100 ==0):
    print ("Leap year")
else:
    print("Not a lip year")


# loop in python

# While loop

i = 1
while i > 6:
    print (i)
    i += 1

