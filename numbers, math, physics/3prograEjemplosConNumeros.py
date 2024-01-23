### 1.-Cricket Balls to Overs!
# In cricket, an over consists of six deliveries a bowler bowls from one end.
# Create a function that takes the number of balls bowled by a bowler and calculates
# the number of overs and balls bowled by him/her. Return the value as a float,
# in the format overs.balls.
# FUENTE:https://edabit.com/challenge/guR6aa2zytfZvywMS
def total_overs(balls):
    t = divmod(balls, 6) #this method takes two numbers as arguments and returns their 
                         #quotient and remainder in a tuple
    return f'{t[0]}' if  t[1] == 0 else f'{t[0]}.{t[1]}'
# print(total_overs(2400))
# print(total_overs(164))
# print(total_overs(945))
# print(total_overs(5))

### 2.-Harshad Numbers
# A number n is a Harshad (also called Niven) number if it is divisible by 
# the sum of its digits. For example, 666 is divisible by 6 + 6 + 6, so it is
# a Harshad number.
# Write a function to determine whether the given number is a Harshad number.
def is_harshad(num):
    sNum = str (num)
    suma = 0
    for i in sNum:
        suma += int(i)
    return True if num % suma == 0 else False
# FUENTE: https://edabit.com/challenge/ZDDyfBFBWMotQSYin
# print(is_harshad(23) )  


### 3.-Number Split
# Given a number, return a list containing the two halves of the number.
# If the number is odd, make the rightmost number higher.
def number_split (n):
    import math 
    return [math.floor(n/2),math.ceil(n-math.floor(n/2))]
# print(number_split(11))
# FUENTE:https://edabit.com/challenge/9f3Mi6vHNcm8vRcSh 



### 5
def solve_for_exp(b,n):
    l = []
    e = n/b
    while e >= 1:
        l.append(e)
        n = e
        e = n/b
    return len(l)
# print(solve_for_exp(4,1024))
# print(solve_for_exp(2, 1024))
# print(solve_for_exp(9, 3486784401))

#### 6.-Cricket Balls to Overs!
# In cricket, an over consists of six deliveries a bowler
# bowls from one end. Create a function that takes the number of
# balls bowled by a bowler and calculates the number of overs
# and balls bowled by him/her. Return the value as a float, in the format overs.balls.

def total_overs(balls:int):
    return balls//6 if balls%6 == 0 else float(f'{balls//6}.{balls%6}')
# FUENTE: https://edabit.com/challenge/guR6aa2zytfZvywMS
# print(total_overs(0)

l:list = ['Glucosa', 'nitrógeno ureico (BUN)', 'urea', 'creatinina', 'ácido úrico', 'calcio total', 
     'fosforo', 'sodio', 'potasio',
     'cloro', 'colesterol total', 'triglicéridos',' relación albúmina/globulina', 
    ' bilirrubina directa', 'bilirrubina indirecta', 'gamma glutamil transpeptidasa (GGT)',
     'fosfatasa alcalina', 'albúmina', 'bilirrubina total', 'lactato']
print(len(l))

