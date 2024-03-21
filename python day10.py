#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

#  method riding
# * ploymorphism in classes

#class bank:
#    def ratio(self):
#        print("All banks has repo rate")


#class SBI(bank):
#    def ratio(self):
#        print("SHI rate is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")
#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()


# ?  Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("Washington DC")

#class India(USA):
#    def language(self):
#        print("None")
#    def capital(self):
#         print("New delhi")
#I = India()
#I.language()
#I.capital()

# ? Eg:3
#polymorphism using object

#c1, c2 -->c1 = print(c1), print(c2)
# f1, f2

# * Eg:4
#class c1:
#    def f1(self):
#        print("class 1")
#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()
#obj2 = c1()
#obj2.f1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

#* changing the functionality of builtin function
#class shooping:
#    def item_list(self,l1):
#        self.items = l1
#    def __len__(self):
#        length = len(self.items)
#        return length*2
#s = shooping([1,2,3,4,5])
#print(len(s))



#s.item_list([1,2,3,4,5])
#a = 9
#b = 6
#print(a+b)print(a.__add__(b)) #?dunder method or mafic method

#int()
#print(a.__sub__(b))


# ! --. Method overloading
# ! Eg:1
#class suming:
#    def add (self, a, b):
#        print(a+b)
#    def add(self, a, b, c):
#         print(a+b+c)
#s = suming()
#s.add(4, 3) # ! ---> error
#s.add(4, 5, 1)


# ! Eg:2
#class suming:
#    def add (self, a=None, b=None, c=None):
#        if a!=None and  b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#             print(a+b)
#        else:
#             print(a)
#obj= suming()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)


# ! ------> Abstraction
# The process of hiding the implimentation details is abstraction

# ? Eg:1
# from abc import ABC,abstractmethod
# class shapes(ABC):
#     @abstractmethod
    
#    def sides(self):
#        print('All shapes have sides except circle')

# class triangle(shapes):
#        print("Iam triangle")

#    def sides(self):
#        pass

# class square(shapes):
#        print("4 sides")

#    def sides(self):
#        pass

# tr = triangle()
# tr.triangle_sides()
# tr.name()

# ! Eg:2
# super()
# from abc import ABC, abstractmethod
# class c1(ABC):
#    @abstractmethod
#    def m1(self):
#        print("The is abstract class")

# class c2(c1):
#    def m2(self):
#        super().m1()
#        print("Iam child 1")
        
#    def m1(self):
#        pass
# class2 = c2()
# class2.m2()

# *Eg:3
# from abc import ABC, abstractmethod
# class password(ABC):
#    @abstractmethod
#    def pwd(self):
#        pswd = "sidd1994$"
#        return pswd

# class login(password):
#    def validate(self, name, password):
#        if super().pwd() == password:
#            print("Welcome", name,'!!')
#            print("Login successful") 
#        else:
#            print("Please check the password")
#    def pwd(self):
#        pass
            
# Login = login()
# name = input("Enter the name: ")
# pwd = input("Enter the password: ")
# Login.validate(name, pwd)

# ! Encapsulation
# ----> Eg:1
# class car:
#    __name = "BMW" # private variable
#    print(__name)

# c1 = car()
# print(c1.name)
# c1.name = "Audi"
# print(c1.name)

# ----> Eg:2
# ? Accessing private data uotside the class
# class c1:
#    __phone = '7656567687'
#    def display(self):
#        print(self.__phone)

# c = c1()
# c.display()

# * -----> Eg:3
# ? declare private method
# class class1:
#    def __m1(self): # private method
#        print("Iam private method")
#    def __init__(self):
#        self.__m1()

# c= class1()
# c.__m1() # error

# ? nested class
# class class1:
#    class class2:
#        name = "sidhu"

#        def display(self):
#            print(self.name)
#    obj1 = class2()

# obj = class1()
# obj.obj1.display()




            



