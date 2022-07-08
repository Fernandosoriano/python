#6 ejercicio personal para practicar lo que es POO con clases
class persona:
        def __init__(self, dictionary={}):
                for key in dictionary:
                        setattr (self, key, dictionary[key])
                # self.dictionary = dictionary
        def returnDict(self):
                return self.nombre


        # def __init__(self,nombre:str, edad:int, ocupación:str):
        #         self.nombre = nombre
        #         self.edad = edad
        #         self.ocupación = ocupación
        # def habla(self):
        #         return f"Hola, mi nombre es {self.nombre} soy {self.ocupación} y tengo {self.edad} años"

# class niño(persona):
#         def hablaNiño(self):
#                 return f"Hola, soy un niño y mi nombre es {self.nombre}, tengo {self.edad} años"

persona1 = persona(
        {
         "nombre":"gabriela",
         "edad":53,
         "ocupacion":"conserje"
         }
         )
# persona1 = persona("fernando",28,"progrmador")
# print(persona1.habla())
# niño1 = niño("Aldo",7)
# print (niño1.hablaNiño())
# print(persona1.nombre)
# print(persona1.nombre)


listaNew = [
        [{
        "name1": "Fer", "apellido1":"valle",
        "name2": "Fer2", "apellido2":"valle2"
        },{
        "name1": "Fer3", "apellido1":"valle3",
        "name2": "Fer4", "apellido2":"valle4"
        }],
        
        [{
        "name1": "Fer5", "apellido1":"valle5",
        "name2": "Fer6", "apellido2":"valle6"
        },{
        "name1": "Fer7", "apellido1":"valle7",
        "name2": "Fer8", "apellido2":"valle8"
        }]
        
        ]

for i in range(len(listaNew)):
        for j in range(len(listaNew[0])):
                # print (listaNew[i][j]["name1"],i,j)
                if listaNew[i][j]["name1"] == "Fer":
                        pass
                        # print("Sí existe Fer")
 

# lista = [{
#         "name": "Fer", "apellido":"valle",
#         "name2": "Fer2", "apellido2":"valle2"
#         },{
#         "name": "Fer3", "apellido":"valle3",
#         "name2": "Fer4", "apellido2":"valle4"
#         }]

# print(lista[1])

# lista = [[1,2,3],[2,3],[1]]

# for i in range(len(lista)):
#         for j in range(len(lista[i])):
#                 print(lista[i][j])

persona = {
        'nombre': 'Fer',
        'apellido': 'Soriano'
} 

# print(len(persona))
import datetime
str_date = '24/12/1993'
date_no_str = datetime.datetime.strptime(str_date, '%d/%m/%Y')
# print(date_no_str)
# print(date_no_str.year) 
# print(datetime.date.today().year)
# print(datetime.date.today().year - date_no_str.year) - ((datetime.date.today().month, datetime.date.today().day) < (date_no_str.month, date_no_str.day))

from datetime import date
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
# print(calculate_age(datetime.datetime(2003, 12, 15, 0, 0)))

# for i in range(3):
#         print(i)
l2 = []
l = [1,2,3]

for i in l:
        l2.append(4)
# print(l2)

# print(len('Proceso de actualización de biometrías terminado con problemas'))

l_p = [(1,2), (3,4)]

l_m = []
for tup in range(len(l_p)):
        for el in range(len(l_p[0])):
                l_m.append(l_p[tup][el])

# print(l_m)

dictionary = { 1: 'one', 2:'two', 3:'three' }
dictionary['ONE'] = dictionary.pop(1)
# print(dictionary)

import random
import string
def listAlphabet():
    # con esta función generas una lista con las
    # letras del abecedario en minusculas
    return list(string.ascii_lowercase)
def listNums(n):
    # con esta función generas una lista con las
    # numeros en el rango en base al número que
    # entra a la función como parámetro
    lst = []
    for i in range(n+1):
        lst.append(str(i))
    return(lst)
def lista_concat():
    # Esta función concatena ambas listas
    # de las funciones anteriores, y te forma
    # una que contiene letras en minuscula
    # y numeros del 0 al 9 en este caso
        return listAlphabet() + listNums(9)
def bloques_aleatorios(list, num):
        list_aleatoria = random.sample(list,num)
        cadena_unida = "".join(list_aleatoria) # concatenas los elementos de una lista en una cadena, en este caso sin espacio
        return cadena_unida
def genera_trace_id():
        return f'{bloques_aleatorios(lista_concat(),8)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),12)}'
print (genera_trace_id())
##################################################################################################
# Lo mismo que el código que use para formar el trace_id, pero en tres líneas 
# usando la libreria uuid de python
import uuid
traceId = uuid.uuid4()
print(traceId)