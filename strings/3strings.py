# 1.-C*ns*r*d Str*ngs
# Someone has attempted to censor my strings by replacing every
# vowel with a *, l*k* th*s. Luckily, I've been able to find the
# vowels that were removed.

# Given a censored string and a string of the censored vowels,
# return the original uncensored string.
# Link = https://edabit.com/challenge/ehyZvt6AJF4rKFfXT

# def uncensor(txt:str, vowel:str) -> str:
#     return txt.replace('*', '{}').format(*vowel)
uncensor = lambda txt, vowel: txt.replace('*', '{}').format(*vowel)
# NOTES:
# the key in this excercise is the use of 
# destructuring with *, because in this way i can do a 
# destructuring in the vowel string, and pass each letter as an
# argument to the format function 
# TESTS
# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
# print(uncensor("abcd", ""))
# print(uncensor("*PP*RC*S*", "UEAE"))
# print(uncensor('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee'))
# print(uncensor('*l*ph*nt', 'Eea'))


# 2.-Censor Words from List
# Create a function that takes a string txt and censors any word from
# a given list lst. The text removed must be replaced by the given character char.
# Link: https://edabit.com/challenge/zJSF5EfPe69e9sJAc

def censor_string(txt:str, lst:list, char:str) -> str:
    """Function that receives a text (txt argument) in which
    the words that are cointained in the list lst are replaced by the
    character char (this char argument will appear
    the same number of times that the length of the origianal
    word)

    Args:
        txt (str): text to be analized
        lst (list): list of words to be replaced
        char (str): character that replaces the word

    Returns:
        str: the text with the indicated words censored
    """
    censor_ls:list = [char*len(ori_word) if ori_word in lst else ori_word for\
        ori_word in txt.split()]
    return ' '.join(censor_ls)
    
# censor_string_lam = lambda txt, lst, char: ' '.join([char*len(ori_word) if ori_word in lst else ori_word for ori_word in txt.split()])
# TESTS:
# print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
# print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
# print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
# print(censor_string("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!"))
# print(censor_string("How do I stop myself from using python!?", ["do", "stop", "using"], "-"))
# print(censor_string("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~"))
# print(censor_string("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?"))
# print(censor_string("I should be doing work but I am doing this instead.", ["should", "but", "this"], "*"))