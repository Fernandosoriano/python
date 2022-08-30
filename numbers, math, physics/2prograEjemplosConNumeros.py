### 1.-FizzBuzz Interview Question
# Create a function that takes a number as an argument and returns "Fizz",
# "Buzz" or "FizzBuzz".

# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output
# on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.

# def fizz_buzz(num):
fizz_buzz = lambda num:"FizzBuzz" if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num)
# print(fizz_buzz(15))

### 2.-Count Ones in Binary Representation of Integer

# Count the amount of ones in the binary representation of an integer. For example,
# since 12 is 1100 in binary, the return value should be 2.
# FUENTE : https://edabit.com/challenge/GbyPdqNnp75Wci7Cn
# def count_ones(num):
#     num_binary = format(num, "b")
#     return num_binary.count('1')
count_ones = lambda num: format(num, "b").count('1')
# print(count_ones(999))



