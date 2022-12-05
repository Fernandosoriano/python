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

