# 1.-Simple OOP Calculator
# Create methods for the Calculator class that can do the following:
# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers.
class Calculator:
    """class that is used to create the model 
    of a calculator that does the basic 
    operations 
    """
    def add(self,a,b):
        return a+b
    def subtract(slef,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a//b
    
#instance of the class:
calculator = Calculator() 
# print(calculator.add(10,5))
# print(calculator.subtract(10,5))
# print(calculator.multiply(10,5))
# print(calculator.divide(10,5))


# 2.-Ones, Threes and Nines (Version #1)

class Ones_threes_nines:
    def __init__(self,number):
        self.number = number  
    def nines(self):
        print( self.number//9)
    def ones(self):
        print ((self.number//self.number) * self.number)
    def threes(self):
        print( (self.number//3))

n1 = Ones_threes_nines(9)
# n1.nines()
# n1.ones()
# n1.threes()       

#3.-Classes For Fetching Information on a Sports Player
# Create a class that takes the following four arguments for
# a particular football player:
# name
# age
# height
# weight
# Also, create three functions for the class that returns the following strings:
# get_age() returns "name is age age"
# get_height() returns "name is heightcm"
# get_weight() returns "name weighs weightkg"
# LINK: https://edabit.com/challenge/pa65DgwG5HMbtf6iY

class Player:
    def __init__(self, name, age, height, weight):
        self.name   = name
        self.age    = age
        self.height = height
        self.weight = weight
        
    def get_age (self):
        return f'{self.name} is age {self.age}'
    def get_height (self):
        return f'{self.name} is {self.height}cm'
    def get_weight(self):
        return f'{self.name} weighs {self.weight}kg'
    
# p1 = Player("David Jones", 25, 175, 75)
# print(p1.get_age())
# print(p1.get_height())
# print(p1.get_weight() )


# 4.-Fullname and Email
class Employee:
    def __init__ (self, name, lastname):
        self.name     = name
        self.lastname = lastname
        
    def fullname (self):
        print(f'Full name: {self.name} {self.lastname}')
    
    def email (self):
        print(f'Email: {self.name.lower()}.{self.lastname.lower()}@company.com')
        
# emp_1 = Employee("John", "Smith")
# emp_1.fullname()
# emp_1.email()



