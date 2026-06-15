# python modules and functions

#1. Math module

# math modules is use for mathematical calculation.

print("\n======Math module======")

import math

#1. sqrt()

# sqrt() is used find the square root of a number.

# Syntax
# math.sqrt(number)

number = 36

result = math.sqrt(number)

print("Square.root of",number,"=",result)

#2. pow()

# pow() is used to calculate power.

base = 2
power = 5

result = math.pow(base,power)

print("base","power","=",result)

#3. ceil()

# ceil() rounds the numberr up to nearest integer

number = 4.2
result = math.ceil(number)

print(result)

#4. floor()

# floor() rounds the number down to nearest integer.

numbers = 4.9

result = math.floor(number)

print(result)

#5. factoraial()

# factoraial() calculat factorial of a nearest number.

number = 5

result = math.factorial(number)

print(result)

#6.gcd()

# gcd() finds greatest common devision.

num1 = 12
num2 = 18

result =  math.gcd(num1,num2)

print(result)

#12:1,2,3,4,6,12
#18:1,2,3,6,9,18

#7.sin()

#sin() calculate sine value.

result = math.sin(1)

print(result)

#8.cos()

# cos() calculate(0)

print(result)

#9.tan()

# tan() calculate tenget value

result = math.tan(1)

print(result)

#10. log()

# log() calculate logerithm value.

number = 10

result = math.log(number)

print(result)

#11. pi

print(math.pi)

#12. e

#1. math e gives Euler's number.

print(math.e)

#2. Random module

# Random() module is used to genrete random values.

# It is useful for gemes OTP genretion, password genration
# random selections,and many more applications.

import random

print("/n==== Random Module ====")

#1. rendiant()

# randiant() generatte a random integer between two number.

# random randiant(start,end)

result = random.randint(1,10)

print(result)

#2. random()

# random() genreate a random float number
# between 0 to 1

# random.random()

result = random.random()
print(result * 10,"math floor (result*10000)")

#3. choice

# choice() selects a random item from a list

# random.choice()

colour = ["Blue","Orange","Red","Yellow"]

result = random.choice(colour)

print(result)

#4. shuffle()

# shuffle() mixes the element of a list

# random.shuffle()

numbers = [1,2,3,4,5,]

print(numbers)

random.shuffle(numbers)

print(numbers)

#5.Uniform()

# uniform() genrate a random desimal number

# between two value

# random uniform(start,end)

result = random.uniform(1,100)

print(result)

#6. randrnge()

# randerange() genrate a random numbewr

# from a given range

# random randrange(start,stop,step)

print(result)

#7.sample

# sample() selects multiple unique random items

# random sample(list,count)

numbwers = [10,20,30,40]

result = random.sample (numbers,2)

print(result)

#3. UUID module

# uuid() genrate a unique ID
# uuid() genarate unique multiple ID
# using current time and IP/MAC address.
# uuid.uuid1()

print("\n ======UUID Module=========")
import uuid

result = uuid.uuid1()

print(result)

# uuid4()

# uuid4() genrate a random unique ID

result = uuid.uuid4()

print(result)

# uuid3()
#uuid3() genrate with name speace,name

# It uses MDS hasing

result = uuid.uuid3(uuid.NAMESPACE_DNS,"example.com")

print(result)















