# Eg:2
#a=a+b
#b=a-b #b=12-7=5
#a=a-b #a=12-5=7

# print(a,b)

# a, b=b, a # only in python
#print(a,b)

# a=a*b #a=35
# b=a/b #b=35/7 = 5.0
# a=a/b #a=35/5= 7.0
# print(int(a), int(b))

#a = 7
#b = 8
#print(a)
#print(id(a))
#print(id(b))

# -----> keywords
# keywords are reserved words which provides special meaning to
# compiler or interpretor

# import keyword
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))

# To check if the string is keyword or not
# print(keyword.iskeyword("sid")) # False

#if = 8
# print(if) # error coz if it is a keyword
# !----> literals
# Lireral is the constant value assigned to a variable
# A variable is considers to be constant when it is defines
# in caps

# a= 78 # a is variable
# A=78 # A is constant
# hash() --> it creats a hash value for constant dataty
# provides error for non constant datatypes
# n1 = 89+7j
# print(hash(n1))

# f1 = [7, 8, 9]
# print(hash(f1)) # error --> list is non-constant or mutable dataty

# a = 9
# b = 90
# print(id(a))
# print(id(b))

#! ----> operators
# ? operators are symbols which is used to perform various opearions
# ? between 2 or more operands

# Arithematic
# Assignment
# Logical
# Relational or comparison
# Bitwise
# Identity
# Membership

# todo ----> Arithmatic --> +,*,/,%,//,**
# Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c)

# input() --> used to get the runtime input
# n1 =int(input("Enter the value: "))
# print(type(n1))
# a = 4
# b = 2
# print(a/b) # is used to get the quotient value
# print(a%b) # is used to get the remainder value

# ! // --> floor devision

# a = 765433
# b = 19

# print(a/b) # -> the output will be inn integer & the output
# based on floot value

#! **--> used for power of a number
# print(2**4) # --> 16

# ! Assigment --> +-=, -=, /=, *=, //=, **=, &=, |=
# a= 8
# a+=2
# print(a)

# a=30
# a-=5
# print(a)
# ! comparison --> ==, >, <, !=, <=, >=
# a = 8
# b = 7
# print(a>b) # True

# a = 9
# b = 5
#print(a==b)

# ! Bitwise operator --> &, |,^,~, <<,>>
# a = 7
# b = 4
# print(a+b)

# ! Logical
# and, or , not
# a = 6
# print(a>3 and a<10)
# print(a>7 or a<30)
# print(not(a>8 and a<10))

#! Identity operator
# is, is not
# a = 8
# b = 8
# print(a is b)
# print(a==b)

# a = (1,2,3)
# b = (1,2,3)
# print(a is not b)

# ! Membership operator
# in, not in
# 11 = [7,8,9,0,6,5]
# num = 55
# print(num in 11)
# print(num not in 11)

# num = 678
# print(8 in num)# error


# Eg:1
# --> c syntax
#if (condition){
#   statement;
#    statement;
#    statement;
#   }
# statement

#eg:1
#a = 6
# if a:
#     print("hello")

# Eg:2
#a = 6
#if a>3:
#   print("hey")
#else:
#    print("no")
# Eg:3
# if 7>8:
#    print("hello")
# print("no")

# Eg:4
# a = 0
# a = None
# a=False
# a=""
# if a:
#    print("yes")
# else:
#    print("no")

# a number is even or odd
# n = int(input("enter the number: "))
# if n %2==0:
#    print(n, "is even")
# else:
#    print(n, "is odd")











 
