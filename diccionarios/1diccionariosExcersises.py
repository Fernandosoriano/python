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