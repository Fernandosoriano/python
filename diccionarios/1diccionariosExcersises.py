#1.-Luke, I Am Your ...
# Luke Skywalker has family and friends. Help him remind them
# who is who. Given a string with a name, return the relation
# of that person to Luke.
# url: https://edabit.com/challenge/8pDH2SRutPoaQghgc
familyLuke = {
    "Darth Vader": "father",
    "Leia":"sister",
    "Han":"brother in law",
    "R2D2":"droid"
}
def relation_to_luke(name="porDefecto"):
    if name == "porDefecto":
         return "ingresa una cadena"
    if type(name)!= str:
        return "sólo se aceptan cadenas"
    else:
     name2 = familyLuke[name] if name in familyLuke else "indefinido"
     msg = f"Luke, I am your {name2}"
     return msg
# print(relation_to_luke("Darth Vader"))
# print(relation_to_luke("Leia"))
# print(relation_to_luke("Han") )
# print(relation_to_luke(2))

#2.-Frequency Distribution
# Create a function that returns the frequency distribution of a list.
# This function should return an object, where the keys are the unique elements
# and the values are the frequency in which those elements occur.
get_frequencies = lambda l: {i: l.count(i) for i in l}
# print(get_frequencies(["A", "B", "A", "A", "A"]))
# print(get_frequencies([1, 2, 3, 3, 2]))
# print(get_frequencies([True, False, True, False, False]))
# print(get_frequencies([]))

# Fuente:https://edabit.com/challenge/KKmM4ob5wwPwf8kgS

#3.-Calculate the Profit
# You work for a manufacturer, and have been asked to calculate the total profit made
# on the sales of a product. You are given a dictionary containing the cost price
# per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
# Return the total profit made, rounded to the nearest dollar.

def profit(info:dict)  -> int:
    """Function that receives a dictionary
    with info of costs and sells of a determinated inventory
    and returns the total profit

    Args:
        info (dict): dictionary with three keys:cost_price, sell_price
        and inventory
    Returns:
        int: tht total profit
    """
    profit = info['sell_price']*info['inventory'] - info['cost_price']* info['inventory']
    return round(profit)  
# print(profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }))

# 3.-Get Students with Names and Top Notes
# def top_note(student:dict) -> dict:
#     return {'name': student['name'], 'top_note':max(student['notes'])}
top_note = lambda student: {'name':student['name'],'top_note':max(student['notes'])}  
# print(top_note({ "name": "John", "notes": [3, 5, 4] }))
# print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
# print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))

# 4.-Invert Keys and Values
# Write a function that inverts the keys and values of a dictionary.
# LINK:https://edabit.com/challenge/Axim3Ld5zu9RFLZKr

invert = lambda dct: {v:k for (k,v) in dct.items()} 
# TESTS:
# print(invert({ "z": "q", "w": "f" }))
# print(invert({ "a": 1, "b": 2, "c": 3 }))
# print(invert({ "zebra": "koala", "horse": "camel" }))

# 5.-encode_morse
# create a function that takes a string as an argument and 
# returns the Morse code equivalent.
def encode_morse(message:str) -> str:
    """function that receives a string, and
    translate this to morse code

    Args:
        message (str): text to be translated

    Returns:
        str: text translated to morse code
    """
    char_to_dots:dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    message_w_o_s_u:str = message.replace(' ', '').upper()
    list_of_simbols:list = [simbol for simbol in message_w_o_s_u]
    list_of_morse:list = [char_to_dots[simbol] for simbol in list_of_simbols]
    res:str = ''.join(list_of_morse)
    return res

# print(encode_morse("sos"))
