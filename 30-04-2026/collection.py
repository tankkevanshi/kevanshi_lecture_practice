# Python Collection

print ("====== python collection datatype======")

# -------- list ----------

print ("List Examples")

my_list = [10,20,30,40]

print ("Original List :" , my_list)

# Mulability

my_list [0] = 100

print ("After Mutability  List :" , my_list)

# Append()

my_list.append(50)

print ("After use buil-in function List:" , my_list)

# max () and min ()

print ("Max :" , max (my_list))
print (" Min :" , min (my_list))

# Remove dublicates meanully

unique = []
for i in my_list :
    if i not in unique:
        unique.append (i)

print ("Unique list:",unique)

#-------tuple--------

print ("Tuple examples")

my_tuple = (1,2,3,4)

print ("Tuple : ", my_tuple)

# Immutable

# count occurrence

print ("count of 2:" , my_tuple.count (2))

# Swapping using tuple

a,b = 10,20
a,b = b,a

print ("Value :",a,b)

# -------set------

print ("set examples")

dataset = [1,2,3,4,5,6]

setdata = set (dataset)

print ("set values  :" ,  setdata)

# set operator

a = {1,2,3}
b ={3,4,5}

print ("Union :" , all)

# ------- Dictionary---------

print ("Dict Examples")

students = {
    "name" : "ved",
    "Marks" : 85
    }

print ("students:", students)

students ["marks"] = 90

print ("students:", students)

# Throught loop create dictionary

for key , value in students.items():

    print (key,":", value)

# Find topper

students = {"A":80 , "B":90 , "C" :89 , "D" : 45}

topper = max (students , key = students . get)

print ("topper :" . upper)

# ------- List Comprehension----------

print ("List comprenension examples:")

numbres = [i for i in range (10) if i %2 != 0]

print ("Odd numbers :", numbers)

#  ----Type Casting ------

print ("type casting Examples:")

t = (1,2,3)

list_1= list(t)

print ("List:" , list_1)

    




