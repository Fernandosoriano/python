# Flip the Boolean
# Create a function that reverses a boolean value and returns the string 
# "boolean expected" if another variable type is given.
def reverse(arg):
    if type(arg) == bool and arg == True:
        return False
    elif type(arg) == bool and arg == False:
        return True
    else:
        return "boolean expected"
#  La más votada:
#     def reverse(arg=None):
# 	return "boolean expected" if not isinstance(arg, bool) else not arg
# print(reverse(True)) 
# print(reverse(False))
# print(reverse(0))
# print(reverse(None))
# print (type(True))
# FUENTE: https://edabit.com/challenge/NLY7zGMYocsTbeS6n