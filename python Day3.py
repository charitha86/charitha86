# ! Eg:3
# ? Take the value of length and breadth of a
#  ? from the user and check if it is square or not.

# length = int(input())
# breadth = int(input())
# if length==breadth:
#    print("its a square")
# else:
#    print("its not square")
    
# ! Eg:4
# python program to check whether the
# given integer is a multiple of both 5 and 7

# n = int(input("enter the number: "))
# if n%5==0 and n%7==0:
#    print("yes")
# else:
#    print("no")
    
# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to the paid
# according to the following criteria :
#
#        cost price (in Rs)
#        > 100000
#        < 100000

# price = int(input("Enter the price: "))
# amount = 0
# if price>=100000:
#    discount = 100000*(6/100)
#    value = price-discount
#    amount=value*(15/100)
#    total=value+amount
# else:
#    tax = price*(5/100)
#    total = price+tax
# print("The onreoad cost of bike is:  ",total)

# if elif
# Eg:1
# a = 7
# b = 9
# c = 3

# if a>b and a>c:
#    print("A is greater")
# elif b>a and b>c:
#    print("B is greater")
# elif c>a and c>b:
#    print("c is greater")

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - c
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# m=int(input("enter marks"))
# if(m<25):
#    print(" Grade F")
# elif(m>=25 and m<45):
#    print(" Grade E")
# elif(m>=45 and m<50):
#    print(" Grade D")
# elif(m>=50 and m<60):
#    print(" Grade C")
# elif(m>=60 and m<80):
#    print(" Grade B")
# elif(m>=80):   #else:
#    print(" Grade A")
# else:
#    print("Fail")

# ! Eg:6
# ? Accept the age of 4 people and display the oldest one

# ! --> short hand if else
# Eg:1
# a = 9
# b = 6
# if a>b:
#    print("A")
# else:
#      print("B")
#? --> using short hand if else
# * Rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) Always it have to end with else

# print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent
# cchar= input("Enter the char: ")
# if char=="a" or char =='e' or char =='i' or char =='0' or char == 'u':
#    print("is a vowel")
# else:
#      print("its consonent")

# ? or

# str1 = "aeiouAEIOU"
# if char in str1:
#    prinr("vowel")
# else:
#    print("consonnt")

# ! shorthand if  else
# char = input("Enter the char: ")
# str1 = "aeiouAEIOU"
# print("vowels") if char in str1 else print("consonent")

# ! ---> elif ladder using short hand if else
# Eg:1
# ? Find greater among 3 variables using short hand if else
# a = 8
# b = 5
# c = 9

# print("A is greater") if a>b and a>c else print("B is greater")if b>a and b>c else print("c is greater")

# ! -----------> looping

# looping can be implimented using
# for loop
# while loop
# ! ---> for loop
# ? for loop is used for iteartion, if we know the number of times the loop have to run
# ? Is used to iterate the iterables eg(string, list, tuple, etc...)

# todo --> syntax for loop

# ! for syntax in c
# for(i=0:i<10:i++){
#     print("hello");
# }

# ! for syntax in python
# for userdefined_variable in range(start, end, step): default setp value is 1
#     statement
#     statement
#     statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

# for i in range(0, 10): #(n, n-1)
#    print(i)
#   print("hello")

#  ? Eg:2
# for val in range(1, 15, -1):
#     print(val)
    
# for val in range(1, 15, -2):
#    print(val)

# ? Eg:3
# to decrement the value

# for val in range(10, 0, 1):
#    print(val) # no output

# ? Eg:4
# ! print the output of 7th multiplication table from 21to 43
# for val in range(1, 10+1):
#    print('7','x', val,'=',val*7) --> method:1

# --> method:2
#   ans="7x{}={}"
#   print(ans.format(val, val*7))

# --> method:3
 #    print(f"7 x {val}={val*7}")

# ?Eg:5
# break --> used to teerminate the loop

# for val in range(1, 10):
#    if val ==6:
#        break
#    print(val)

# Eg:6
# for val in range(1, 10):
#    if val ==6:
#        print(val)
#        break
# ? Eg:7
# for val in range(1, 10):
#    if val ==6:
#        print(val)
#        break

# ! continue
# Eg:1
# for val in range(1, 10):
#  if val ==6:
#        continue
#    print(val)

# for val in range(1,30):
#    if val ==6 and val ==8 or val ==21:
#       continue
#    print(val)

# ! Practise problems
# ? Print the even number between 20 to 40
# for val in range(20, 41):
#    if val %2==0:
#        print(val)

#!---------> While loop
# ? while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable elements while loop is used

# todo syntax

# initialisation
# while condition:
#     statement
#     incre or decre

#! Eg:1
# to iterate number from 1 to 10

# i = 0
# while i<11:
#     print(i)
#     i=i+1 # OR I+=1

# Eg:2
# to decrement using while loop
# i=10
# while i>0:
#    print(i)
#      i-=1

# ! ----> 1-4+9-16+25=15
# n =int(input("enter number: "))
 sum=0
 for val in range(1, n+1):
    sq=val*val
    if val %2!=0:
        sum=sum+sq
    else:
        sum=sum-sq
print(sum)






# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432






























