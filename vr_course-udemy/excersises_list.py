# Begining of  excersisies from Victor Robles's course (udemy)
# 1.-
def multiply_table(num: int) -> str:
    """Function that receives a number
    and returns a string in  format that
    lists the multiplication of this number from
    1 to 10

    Args:
        num (int): number of which this
        function calculatees their multiplication

    Returns:
        str: a string with a format
        to see a list of the multiplication
        of the received number from 1 to 10
    """
    res = f'Tabla del número {num}: \n'
    for multiplier in range (1,11):
        res += f'{num} X {multiplier} = {num * multiplier}\n'
    return res
# print(multiply_table(4))

# 2.- Es palindromo?
str_1:str = 'Oso'
# print(str_1 == str_1[::-1].capitalize())

# 3.-Excersise to count the number of times that one word appears
# in a given text,

from typing import List
def coincidence_counter (txt:str, word:str):
    """
    Function that receives one text and a word as a
    prameters, and returns the total number of times that
    the word appears in the text
    """
    valid_coincideneces:List = ['can,', 'can;','can.', 'can']
    coincidence_ls:List = [coincidence for coincidence in txt.split() if coincidence in valid_coincideneces]
    return len(coincidence_ls)

txt = """In this text i'm writting the word: can many times because i can, i can, i can do anything
that i want, come on you can do it Fer, don't lose the hope, hope hope dear Fer"""

word = 'can'

print(coincidence_counter(txt, word))

def coincidence_counter(txt: str, word: str) -> int:
    import re
    pattern = fr'\b{re.escape(word)}\b[.,;:?!]?'
    return len(re.findall(pattern, txt))