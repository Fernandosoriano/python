# 1.-Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. If 1 plus
# 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num
# is a Curzon number. Given a non-negative integer num, implement a function that
# returns True if num is a Curzon number, or False otherwise.
# FUENTE: https://edabit.com/challenge/HYjQKDXFfeppcWmLX
def is_curzon(num):
    potencia = (2**num) + 1
    multiplica =  (2*num) + 1 
    if potencia % multiplica == 0:
        return True
    return False
# print(is_curzon(5))
# print(is_curzon(10))
# print(is_curzon(14))

# 2.- Calculating Damage
# Create a function that takes damage and speed (attacks per second) and 
# returns the amount of damage after a given time.
# FUENTE:https://edabit.com/challenge/HSHHkdRYXfgfZSqri
def damage(damage, speed, time):
    if damage<0 or speed<0:
        return 'invalid'
    time_low = time.lower()
    if time_low == 'second':
        resulting_damage = damage * speed
        return resulting_damage
    elif time_low == 'minute':
        time_seconds = speed * 60
        resulting_damage = damage * time_seconds
        return resulting_damage
    time_seconds = speed*60*60
    resulting_damage = damage * time_seconds
    return resulting_damage

print(damage(40, 5, "second"))
print(damage(100, 1, "minute"))
print(damage(2, 100, "hour"))
print(damage(-2, 100, "hour"))




