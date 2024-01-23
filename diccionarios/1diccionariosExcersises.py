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