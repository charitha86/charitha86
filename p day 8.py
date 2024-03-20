# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

#def gracemark(object):
#    print(object+4)
#gracemark(obj)
#gracemark(obj1)
#print(txt.format(name, age, place))
#profile("janu",20,"pulivendula")    

# ! Eg:4
# ? function with return statement
#def f1():
#    z = 8
#f1()
#print(z) #error ---->cannot use outside the function

#def f1(a,b):
#    c = a*b
#    return c
#print(f1(6,8))
#obj=f1(6,8)
#obj1=f1(4,6)


#def gracemark():
#    print(output+4)
#gracemark()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

#def f1(a,b):
#    c = a*b
#obj=f1(6,8)
#obj1=f1(4,6)

#def gracemark(object):
#    print(object+4)
#gracemark(abj)
#gracemark(abj1)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# ? problem:1
#def palindrome(n):
#    string = str(n)
#    rev = str(n)[::-1]
#    if string==rev:
#        print(n, "palindrome")
#    else:
#        print("not palindrome")
#a = int(input("Enter the value: "))        
#palindrome(a)    


#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args


# * Positional args
# ? the position of parameter ahve to be same as position os arguments
# | Eg:1
#def profile(name, phone, mark):
#    txt = "My name is {}. My phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))
#profile(9878776767, "sidhu", 97) # unexpected output    

# * keywords args
# | Eg:1
# ? to overcome the disadvantage of position args, we use keyword args
# ? it is the process of initializing the parameter with the args while calling
# ? the function

#def profile(name,phone,mark):
#    txt="My name is {}. My phone number is {}. I got s{} marks."
#    print(txt.format(name,phone,mark))
#profile(name="janu",mark=100,phone=1234567890)

# todo ---> Exception of keyword args function
#def profile (name, phone, mark):
#    txt = "My name is {}. I got {} marks."
#    print(txt.format(name, phone, mark))

# profile(name="sid", 123445567, mark=98) #error -->positional arsg follow keywordargs
# profile(123445567, name = "sid", mark=98) # error --> name has multipe values
# profile("janu", mark=98, phone=1234567890)

# * Default args
# | Eg:1
#def profile(name, phone, place="kadapa"):
#    txt -"My name is {}. My phone number is {}. I am from {}."
#    print(txt.format(name, phone, place))

#profile("janu", 6758931250)    

# Eg:2
#def profile(name, phone, place="kadapa"):
#    txt = "My name is {}. My phone number is {}. I am from {}."
#    print(txt.format(name, phone, place))

#profile("janu", 6758931250, "pulivendula")


# * keyword variable length args
# Kwargs --> which is used to provide the args in the form of key
# ! Eg:1
#def price(price_list):
#    print(price_list)

#price(shirt=1000, iphone=80000)

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}

#def dict1(n):
#    d1 = {}
#    for val in range(1, n+1):
#        d1[val] = val**2
#    print(d1)
#dict1(5)

# ! ----> object oriented programming
# The paradigms of object oriented programing are

#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation

# ! Class is a blue print of an object
# l1 = [1,2,3,4,5,6]


# ? Eg:1
# class c1:
#    name = "sidhu"

# ? Eg:2
# c = person() # c os object
# print(c.name)

# ? Eg:3
# create of a method
# When the function is created with a class is called as method
#class person:
#    def display():
#        print("Hello welcome to classes")
#p = person()
#p.display()


# Eg:5
#class person:
#    female = "sidhu"
#    lname = "T"

#    def first_name(self):
#        print(self.fname)
#    def full_name(person):
#        print(self.fname+" "+self.lname)

#p = person1()
#p.first_name()
#p.full_name()
   
   
# ? EG:6
#class profile:
#    def __init__(self): # constructor method
#        print("hey")

#p = profile() #execution
# p.__init__()
   







   





#d1 = {"a":100, "b":200, "c":300}
#d1 = dict(a=100, b=200, c=300)
#

