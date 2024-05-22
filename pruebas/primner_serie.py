# 6 ejercicio personal para practicar lo que es POO con clases
import uuid
import string
import random
from datetime import date
import datetime


class persona:
    def __init__(self, dictionary={}):
        for key in dictionary:
            setattr(self, key, dictionary[key])
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
        "nombre": "gabriela",
        "edad": 53,
        "ocupacion": "conserje"
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
        "name1": "Fer", "apellido1": "valle",
        "name2": "Fer2", "apellido2": "valle2"
    }, {
        "name1": "Fer3", "apellido1": "valle3",
        "name2": "Fer4", "apellido2": "valle4"
    }],

    [{
        "name1": "Fer5", "apellido1": "valle5",
        "name2": "Fer6", "apellido2": "valle6"
    }, {
        "name1": "Fer7", "apellido1": "valle7",
        "name2": "Fer8", "apellido2": "valle8"
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
str_date = '24/12/1993'
date_no_str = datetime.datetime.strptime(str_date, '%d/%m/%Y')
# print(date_no_str)
# print(date_no_str.year)
# print(datetime.date.today().year)
# print(datetime.date.today().year - date_no_str.year) - ((datetime.date.today().month, datetime.date.today().day) < (date_no_str.month, date_no_str.day))


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
# print(calculate_age(datetime.datetime(2003, 12, 15, 0, 0)))


# for i in range(3):
#         print(i)
l2 = []
l = [1, 2, 3]

for i in l:
    l2.append(4)
# print(l2)

# print(len('Proceso de actualización de biometrías terminado con problemas'))

l_p = [(1, 2), (3, 4)]

l_m = []
for tup in range(len(l_p)):
    for el in range(len(l_p[0])):
        l_m.append(l_p[tup][el])

# print(l_m)

dictionary = {1: 'one', 2: 'two', 3: 'three'}
dictionary['ONE'] = dictionary.pop(1)
# print(dictionary)


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
    return (lst)


def lista_concat():
    # Esta función concatena ambas listas
    # de las funciones anteriores, y te forma
    # una que contiene letras en minuscula
    # y numeros del 0 al 9 en este caso
    return listAlphabet() + listNums(9)


def bloques_aleatorios(list, num):
    list_aleatoria = random.sample(list, num)
    # concatenas los elementos de una lista en una cadena, en este caso sin espacio
    cadena_unida = "".join(list_aleatoria)
    return cadena_unida


def genera_trace_id():
    return f'{bloques_aleatorios(lista_concat(),8)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),12)}'


# print (genera_trace_id())
##################################################################################################
# Lo mismo que el código que use para formar el trace_id, pero en tres líneas
# usando la libreria uuid de python
traceId = uuid.uuid4()
# print(traceId)


# for i in lista_devuelta:
#         for j in lista_a_considerar:
#                 if i == j:
#                         lista_a_sellar.append(i)
# print(lista_a_sellar)

# def documentos_a_sellar(lista_idDocs_deben_sellarse, lista_docs_creditkit):
#         lista_con_idDocs_a_sellar = []
#         for id_doc_creditkit in lista_docs_creditkit:
#                 for id_doc_a_sellar in lista_idDocs_deben_sellarse:
#                         if id_doc_creditkit == id_doc_a_sellar:
#                                 lista_con_idDocs_a_sellar.append(id_doc_creditkit)
#         return lista_con_idDocs_a_sellar

def documentos_a_sellar(lista_docs_creditkit):
    lista_idDocs_deben_sellarse = [121, 137, 120, 136, 135, 149, 182, 183]
    lista_con_idDocs_a_sellar = []
    for id_doc_creditkit in lista_docs_creditkit:
        for id_doc_a_sellar in lista_idDocs_deben_sellarse:
            if id_doc_creditkit == id_doc_a_sellar:
                lista_con_idDocs_a_sellar.append(id_doc_creditkit)
    return lista_con_idDocs_a_sellar


# lista_a_considerar_p = [121,137,120,136, 135, 149, 182, 183]
lista_devuelta_p = [127, 140, 137, 182]
# print(documentos_a_sellar(lista_devuelta_p))


var_global = ""
lista_por_recorrer = [1, 2, 3, 4, 5, 6]


# for num in lista_por_recorrer:
#         var_global = "33"
#         num = num + 1
#         print (num)
# print(var_global)

data = [
    {
        "id_proceso_venta": 6691697,
        "id_individuo": 201777968,
        "id_funcion_participante": 1.0,
        "id_tipo_proceso_venta": "A01",
        "id_oferta_fabrica": 13027,
        "id_tipo_punto_venta": 1,
        "id_punto_venta": 242,
        "id_macro_proceso": "MPC01",
        "id_proceso": "PC002",
        "id_canal": "C01",
        "id_medios_digitales": 'null',
        "id_esquema": "ECDCT",
        "id_estatus_esquema": "EC200",
        "estatus_esquema_descripcion": "Solicitante con oferta confirmada",
        "id_motivo_estatus": 'null',
        "descripcion_motivo_estatus": "",
        "agrupador": 1,
        "fechas": [],
        "preferencia_atencion": [],
        "fecha_creacion": "2022-07-15 17:19:31",
        "fecha_modificacion": "2022-07-23 02:03:26",
        "id_oferta_fabrica_general": 3171,
        "id_oferta_fabrica_persona": 13027,
        "id_promocion": 'null',
        "id_pais": 1.0,
        "id_empresa": 2.0,
        "id_canal_entrada": 7.0,
        "id_tipo_estrategia": 'null',
        "id_destino": 11,
        "otro_destino": 'null',
        "id_tipo_ciclo": 'null',
        "valor_ciclo": 'null',
        "id_tipo_participante": 2.0,
        "id_tipo_renovacion": 'null',
        "id_estado_proceso_venta": "E001"
    },
    {
        "id_proceso_venta": 6691698,
        "id_individuo": 201777968,
        "id_funcion_participante": 1.0,
        "id_tipo_proceso_venta": "A01",
        "id_oferta_fabrica": 13027,
        "id_tipo_punto_venta": 1,
        "id_punto_venta": 242,
        "id_macro_proceso": "MPC01",
        "id_proceso": "PC002",
        "id_canal": "C01",
        "id_medios_digitales": 'null',
        "id_esquema": "ECDCT",
        "id_estatus_esquema": "EC200",
        "estatus_esquema_descripcion": "Solicitante con oferta confirmada",
        "id_motivo_estatus": 'null',
        "descripcion_motivo_estatus": "",
        "agrupador": 1,
        "fechas": [],
        "preferencia_atencion": [],
        "fecha_creacion": "2022-07-15 17:19:31",
        "fecha_modificacion": "2022-07-23 02:03:26",
        "id_oferta_fabrica_general": 3171,
        "id_oferta_fabrica_persona": 13027,
        "id_promocion": 'null',
        "id_pais": 1.0,
        "id_empresa": 2.0,
        "id_canal_entrada": 7.0,
        "id_tipo_estrategia": 'null',
        "id_destino": 11,
        "otro_destino": 'null',
        "id_tipo_ciclo": 'null',
        "valor_ciclo": 'null',
        "id_tipo_participante": 2.0,
        "id_tipo_renovacion": 'null',
        "id_estado_proceso_venta": "E001"
    }
]
lista_procesos_venta = []

if len(data) == 1:
    pass  # hacer proceso de sellado normal, pero no habria el segundo for de recorrer todos los individuos
else:
    for soli_obj in data:  # Quizá este for ya NO deba ir, porque se haria el proceso de sellado para tooodos los individuos que vengan en el arrary data, y esto sólo se debe hacecr para el padre
        solicitante = soli_obj  # almacenar en memoria el soli para el proceso de venta
        id_proceso_venta = solicitante.get('id_proceso_venta')
        lista_procesos_venta.append(id_proceso_venta)

# print (lista_procesos_venta)


def identifica_pv_padre(proceso_venta):
    if proceso_venta == 6691698:
        return proceso_venta


list_proceso_venta_padre = list(
    filter(identifica_pv_padre, lista_procesos_venta))

# print(list_proceso_venta_padre[0])
padre = 3
lista = [1, 2, 3, 4, 5]
lista.append(padre)
lista_completa = lista
# print(lista)

lista_docs_sellados = []
lista_id_clients = [124, 123, 345, 1234]
lista_docs_ya_sellados = [123, 127]

for id_doc in lista_docs_ya_sellados:
    id_plantilla = 3
    base64 = 64
    file_name = "doc_name"
    lista_docs_sellados.append({
        'id_plantilla': id_plantilla,
        'base64': base64,
        'file_name': file_name
    })

# print(lista_docs_sellados)

lista_content = []
for doc_sellado in lista_docs_sellados:
    for id_cliente in lista_id_clients:
        lista_content.append(doc_sellado)

# print(lista_docs_sellados)
# print(lista_content)


# print('hola ')

# def suma (n):
#         suma = 0
#         for i in n:
#                 suma = suma + int(i)
#         return str(suma)
#         if len (suma) > 2:
#                 pass

# print(suma ('16'))

# def suma(n):
# #     x = str(n)
#     s = 0
#     while len(n) > 1:
#         s = 0
#         for i in range(len(n)):
#             s = s + int(n[i])
#             x = str(s)
#     return x

# print(suma ('132189'))


def sum(n):
    while len(n) > 1:
        suma = 0
        for i in range(len(n)):
            suma = suma + int(n[i])
        n = str(suma)
    return suma

# print(sum('942'))

# print (abs(-3))
# circlePairsIn = ['12 0 21 14 0 23', '0 45 8 0 94 9', '35 0 13 10 0 38', '0 26 8 0 9 25']
#    print(i.split()[5])
# l = []
# for cadena in circlePairs:
#         l.append(cadena.split())
# print(l)


def relativePositions(circlePairs):
    l = []
    lstResponse = []
    for cadena in circlePairs:
        l.append(cadena.split())
    for lst in l:
        def dis(x1, x2, y1, y2):
            from math import sqrt
            d = sqrt((x2-x1)**2+(y2-y1)**2)
            return d
        touchingCondition = dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4])) == abs(int(
            lst[5])-int(lst[2])) or int(lst[5]) + int(lst[2]) == dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4]))
        concentricCondition = int(lst[0]) == int(
            lst[3]) and int(lst[1]) == int(lst[4])
        disjointOutsiderCondition = dis(int(lst[0]), int(lst[3]), int(
            lst[1]), int(lst[4])) > int(lst[5]) + int(lst[2])
        intersectingCondition = dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4])) < int(
            lst[5]) + int(lst[2]) and dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4])) > int(lst[5]) - int(lst[2])
        disjointInsiderCondition = dis(int(lst[0]), int(lst[3]), int(
            lst[1]), int(lst[4])) < abs(int(lst[5]) - int(lst[2]))

        if touchingCondition:
            lstResponse.append('Touching')
        elif concentricCondition:
            lstResponse.append('Concentric')
        elif intersectingCondition and not disjointInsiderCondition and not disjointOutsiderCondition:
            lstResponse.append('Intersecting')
        elif disjointOutsiderCondition:
            lstResponse.append('Disjoint-Outsider')
        elif disjointInsiderCondition:
            lstResponse.append('Disjoint-Insider')
#         return lstResponse
# print(relativePositions(['12 0 21 14 0 23', '0 45 8 0 94 9', '35 0 13 10 0 38', '0 26 8 0 9 25']))


def odd_even_product(list_of_numbers):
    prod = 1
    suma = 0
    for num in list_of_numbers:
        suma = suma + num
    for num in list_of_numbers:
        prod = prod * prod
    if prod % 2 != 0:
        return suma
    else:
        return 0
# print(odd_even_product([1,2,3,4]))


def complete_inventory(warehouse_1, x, warehouse_2, y):
    back_index = len(warehouse_1)
    first_pointer = x
    second_pointer = y
    while second_pointer > 0:
        if first_pointer > 0 and warehouse_1[first_pointer] > warehouse_2[second_pointer-1]:
            warehouse_1[back_index] = warehouse_1[first_pointer]
        else:
            warehouse_1[back_index-1] = warehouse_2[second_pointer-1]

    return warehouse_1

# print(complete_inventory([2,3,4,0,0,0],3,[1,5,9],3))



def higher_future_temp( temperatures ) :
        l = []
        for index,temp in enumerate(temperatures):
                print(index,temp)
             
        
# higher_future_temp([21,22,21,22,25,21])


def higher_future_temp(T):
    n = len(T)
    diasAEsperar = [0] * n
    s = []
    for i in range(n):
        while(len(s) != 0 and T[s[-1]] < T[i]):
            diasAEsperar[s[-1]] = i - s[-1]
            s.pop(-1)
        s.append(i)
    for i in range(n):
        print(diasAEsperar[i], end = " ")
        
# print([1,2,3]*3)

# dailyTemperatures([21,22,21,22,25,21])
# higher_future_temp([22,23,21,25,23])


def is_leap(year):
      leap = False

      if (year % 4 == 0) and (year % 100 != 0): 
      # Note that in your code the condition will be true if it is not..
        leap = True
      elif (year % 100 == 0) and (year % 400 != 0):
        leap = False
      elif (year % 400 == 0):
      # For some reason here you had False twice
        leap = True
      else:
        leap = False

      return leap

# print(is_leap(2000))



def print1AN (n):
     l = []
     for i in range(1, n+1):
         l.append(i)
        # print(i, end='')
     return (''.join(str(e) for e in l))
# print(print1AN(3))

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
# print(list(zipped))

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
# print(X)
# print (list(zip(*X)))

digits = [1,2,3,4,5]
words = ['one', 'two', 'three', 'four','five']
zipobj = zip(digits, words)
# print(list(zipobj))
## to unzip
x,y = zip(*zipobj)
# print(x)
# print(y)


# print('Hola mundo')


def is_palindromo (s:str)-> bool:
    return True if s[::-1] == s else False

# print(is_palindromo('alagordadrogala'))

# ===============================================================

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
        
# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
# mi_perro.describeme()
# Soy un Animal del tipo Perro


# import string
# alphabet = list(string.ascii_lowercase)
# print(alphabet)

def StringChallenge(texto):
    import string
    alphabet = list(string.ascii_lowercase)
    l = []
    str_low = texto.lower()
    for i in str_low:
        if i in alphabet:
            l.append(str(alphabet.index(i) + 1))
        else:
            l.append(i)
    return ''.join(l)
# print(StringChallenge('FER-31'))