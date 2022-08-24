### 1.-RegEx XV: Alternation
# The vertical bar | is the equivalent to "or" in RegEx. The regular expression
# x|y matches either "x" or "y". Write the regular expression that will match
# all red flag and blue flag in a string. You must use | in your expression.
# Flags can come in any order.
# FUENTE: https://edabit.com/challenge/FF6kYPHdAcJnoosr5
import re
txt1 = "red flag blue flag"
txt2 = "yellow flag red flag blue flag green flag"
txt3 = "pink flag red flag black flag blue flag green flag red flag"
pattern = "red flag|blue flag"

print(re.findall(pattern, txt1))
print(re.findall(pattern, txt2) )
print(re.findall(pattern, txt3) )