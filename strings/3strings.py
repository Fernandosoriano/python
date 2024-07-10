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