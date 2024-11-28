# # 6 ejercicio personal para practicar lo que es POO con clases
# import uuid
# import string
# import random
# from datetime import date
# import datetime


# class persona:
#     def __init__(self, dictionary={}):
#         for key in dictionary:
#             setattr(self, key, dictionary[key])
#         # self.dictionary = dictionary

#     def returnDict(self):
#         return self.nombre

#     # def __init__(self,nombre:str, edad:int, ocupación:str):
#     #         self.nombre = nombre
#     #         self.edad = edad
#     #         self.ocupación = ocupación
#     # def habla(self):
#     #         return f"Hola, mi nombre es {self.nombre} soy {self.ocupación} y tengo {self.edad} años"

# # class niño(persona):
# #         def hablaNiño(self):
# #                 return f"Hola, soy un niño y mi nombre es {self.nombre}, tengo {self.edad} años"


# persona1 = persona(
#     {
#         "nombre": "gabriela",
#         "edad": 53,
#         "ocupacion": "conserje"
#     }
# )
# # persona1 = persona("fernando",28,"progrmador")
# # print(persona1.habla())
# # niño1 = niño("Aldo",7)
# # print (niño1.hablaNiño())
# # print(persona1.nombre)
# # print(persona1.nombre)


# listaNew = [
#     [{
#         "name1": "Fer", "apellido1": "valle",
#         "name2": "Fer2", "apellido2": "valle2"
#     }, {
#         "name1": "Fer3", "apellido1": "valle3",
#         "name2": "Fer4", "apellido2": "valle4"
#     }],

#     [{
#         "name1": "Fer5", "apellido1": "valle5",
#         "name2": "Fer6", "apellido2": "valle6"
#     }, {
#         "name1": "Fer7", "apellido1": "valle7",
#         "name2": "Fer8", "apellido2": "valle8"
#     }]

# ]

# for i in range(len(listaNew)):
#     for j in range(len(listaNew[0])):
#         # print (listaNew[i][j]["name1"],i,j)
#         if listaNew[i][j]["name1"] == "Fer":
#             pass
#             # print("Sí existe Fer")


# # lista = [{
# #         "name": "Fer", "apellido":"valle",
# #         "name2": "Fer2", "apellido2":"valle2"
# #         },{
# #         "name": "Fer3", "apellido":"valle3",
# #         "name2": "Fer4", "apellido2":"valle4"
# #         }]

# # print(lista[1])

# # lista = [[1,2,3],[2,3],[1]]

# # for i in range(len(lista)):
# #         for j in range(len(lista[i])):
# #                 print(lista[i][j])

# persona = {
#     'nombre': 'Fer',
#     'apellido': 'Soriano'
# }

# # print(len(persona))
# str_date = '24/12/1993'
# date_no_str = datetime.datetime.strptime(str_date, '%d/%m/%Y')
# # print(date_no_str)
# # print(date_no_str.year)
# # print(datetime.date.today().year)
# # print(datetime.date.today().year - date_no_str.year) - ((datetime.date.today().month, datetime.date.today().day) < (date_no_str.month, date_no_str.day))


# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
# # print(calculate_age(datetime.datetime(2003, 12, 15, 0, 0)))


# # for i in range(3):
# #         print(i)
# l2 = []
# l = [1, 2, 3]

# for i in l:
#     l2.append(4)
# # print(l2)

# # print(len('Proceso de actualización de biometrías terminado con problemas'))

# l_p = [(1, 2), (3, 4)]

# l_m = []
# for tup in range(len(l_p)):
#     for el in range(len(l_p[0])):
#         l_m.append(l_p[tup][el])

# # print(l_m)

# dictionary = {1: 'one', 2: 'two', 3: 'three'}
# dictionary['ONE'] = dictionary.pop(1)
# # print(dictionary)


# def listAlphabet():
#     # con esta función generas una lista con las
#     # letras del abecedario en minusculas
#     return list(string.ascii_lowercase)


# def listNums(n):
#     # con esta función generas una lista con las
#     # numeros en el rango en base al número que
#     # entra a la función como parámetro
#     lst = []
#     for i in range(n+1):
#         lst.append(str(i))
#     return (lst)


# def lista_concat():
#     # Esta función concatena ambas listas
#     # de las funciones anteriores, y te forma
#     # una que contiene letras en minuscula
#     # y numeros del 0 al 9 en este caso
#     return listAlphabet() + listNums(9)


# def bloques_aleatorios(list, num):
#     list_aleatoria = random.sample(list, num)
#     # concatenas los elementos de una lista en una cadena, en este caso sin espacio
#     cadena_unida = "".join(list_aleatoria)
#     return cadena_unida


# def genera_trace_id():
#     return f'{bloques_aleatorios(lista_concat(),8)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),4)}-{bloques_aleatorios(lista_concat(),12)}'


# # print (genera_trace_id())
# ##################################################################################################
# # Lo mismo que el código que use para formar el trace_id, pero en tres líneas
# # usando la libreria uuid de python
# traceId = uuid.uuid4()
# # print(traceId)


# # for i in lista_devuelta:
# #         for j in lista_a_considerar:
# #                 if i == j:
# #                         lista_a_sellar.append(i)
# # print(lista_a_sellar)

# # def documentos_a_sellar(lista_idDocs_deben_sellarse, lista_docs_creditkit):
# #         lista_con_idDocs_a_sellar = []
# #         for id_doc_creditkit in lista_docs_creditkit:
# #                 for id_doc_a_sellar in lista_idDocs_deben_sellarse:
# #                         if id_doc_creditkit == id_doc_a_sellar:
# #                                 lista_con_idDocs_a_sellar.append(id_doc_creditkit)
# #         return lista_con_idDocs_a_sellar

# def documentos_a_sellar(lista_docs_creditkit):
#     lista_idDocs_deben_sellarse = [121, 137, 120, 136, 135, 149, 182, 183]
#     lista_con_idDocs_a_sellar = []
#     for id_doc_creditkit in lista_docs_creditkit:
#         for id_doc_a_sellar in lista_idDocs_deben_sellarse:
#             if id_doc_creditkit == id_doc_a_sellar:
#                 lista_con_idDocs_a_sellar.append(id_doc_creditkit)
#     return lista_con_idDocs_a_sellar


# # lista_a_considerar_p = [121,137,120,136, 135, 149, 182, 183]
# lista_devuelta_p = [127, 140, 137, 182]
# # print(documentos_a_sellar(lista_devuelta_p))


# var_global = ""
# lista_por_recorrer = [1, 2, 3, 4, 5, 6]


# # for num in lista_por_recorrer:
# #         var_global = "33"
# #         num = num + 1
# #         print (num)
# # print(var_global)

# data = [
#     {
#         "id_proceso_venta": 6691697,
#         "id_individuo": 201777968,
#         "id_funcion_participante": 1.0,
#         "id_tipo_proceso_venta": "A01",
#         "id_oferta_fabrica": 13027,
#         "id_tipo_punto_venta": 1,
#         "id_punto_venta": 242,
#         "id_macro_proceso": "MPC01",
#         "id_proceso": "PC002",
#         "id_canal": "C01",
#         "id_medios_digitales": 'null',
#         "id_esquema": "ECDCT",
#         "id_estatus_esquema": "EC200",
#         "estatus_esquema_descripcion": "Solicitante con oferta confirmada",
#         "id_motivo_estatus": 'null',
#         "descripcion_motivo_estatus": "",
#         "agrupador": 1,
#         "fechas": [],
#         "preferencia_atencion": [],
#         "fecha_creacion": "2022-07-15 17:19:31",
#         "fecha_modificacion": "2022-07-23 02:03:26",
#         "id_oferta_fabrica_general": 3171,
#         "id_oferta_fabrica_persona": 13027,
#         "id_promocion": 'null',
#         "id_pais": 1.0,
#         "id_empresa": 2.0,
#         "id_canal_entrada": 7.0,
#         "id_tipo_estrategia": 'null',
#         "id_destino": 11,
#         "otro_destino": 'null',
#         "id_tipo_ciclo": 'null',
#         "valor_ciclo": 'null',
#         "id_tipo_participante": 2.0,
#         "id_tipo_renovacion": 'null',
#         "id_estado_proceso_venta": "E001"
#     },
#     {
#         "id_proceso_venta": 6691698,
#         "id_individuo": 201777968,
#         "id_funcion_participante": 1.0,
#         "id_tipo_proceso_venta": "A01",
#         "id_oferta_fabrica": 13027,
#         "id_tipo_punto_venta": 1,
#         "id_punto_venta": 242,
#         "id_macro_proceso": "MPC01",
#         "id_proceso": "PC002",
#         "id_canal": "C01",
#         "id_medios_digitales": 'null',
#         "id_esquema": "ECDCT",
#         "id_estatus_esquema": "EC200",
#         "estatus_esquema_descripcion": "Solicitante con oferta confirmada",
#         "id_motivo_estatus": 'null',
#         "descripcion_motivo_estatus": "",
#         "agrupador": 1,
#         "fechas": [],
#         "preferencia_atencion": [],
#         "fecha_creacion": "2022-07-15 17:19:31",
#         "fecha_modificacion": "2022-07-23 02:03:26",
#         "id_oferta_fabrica_general": 3171,
#         "id_oferta_fabrica_persona": 13027,
#         "id_promocion": 'null',
#         "id_pais": 1.0,
#         "id_empresa": 2.0,
#         "id_canal_entrada": 7.0,
#         "id_tipo_estrategia": 'null',
#         "id_destino": 11,
#         "otro_destino": 'null',
#         "id_tipo_ciclo": 'null',
#         "valor_ciclo": 'null',
#         "id_tipo_participante": 2.0,
#         "id_tipo_renovacion": 'null',
#         "id_estado_proceso_venta": "E001"
#     }
# ]
# lista_procesos_venta = []

# if len(data) == 1:
#     pass  # hacer proceso de sellado normal, pero no habria el segundo for de recorrer todos los individuos
# else:
#     for soli_obj in data:  # Quizá este for ya NO deba ir, porque se haria el proceso de sellado para tooodos los individuos que vengan en el arrary data, y esto sólo se debe hacecr para el padre
#         solicitante = soli_obj  # almacenar en memoria el soli para el proceso de venta
#         id_proceso_venta = solicitante.get('id_proceso_venta')
#         lista_procesos_venta.append(id_proceso_venta)

# # print (lista_procesos_venta)


# def identifica_pv_padre(proceso_venta):
#     if proceso_venta == 6691698:
#         return proceso_venta


# list_proceso_venta_padre = list(
#     filter(identifica_pv_padre, lista_procesos_venta))

# # print(list_proceso_venta_padre[0])
# padre = 3
# lista = [1, 2, 3, 4, 5]
# lista.append(padre)
# lista_completa = lista
# # print(lista)

# lista_docs_sellados = []
# lista_id_clients = [124, 123, 345, 1234]
# lista_docs_ya_sellados = [123, 127]

# for id_doc in lista_docs_ya_sellados:
#     id_plantilla = 3
#     base64 = 64
#     file_name = "doc_name"
#     lista_docs_sellados.append({
#         'id_plantilla': id_plantilla,
#         'base64': base64,
#         'file_name': file_name
#     })

# # print(lista_docs_sellados)

# lista_content = []
# for doc_sellado in lista_docs_sellados:
#     for id_cliente in lista_id_clients:
#         lista_content.append(doc_sellado)

# # print(lista_docs_sellados)
# # print(lista_content)


# # print('hola ')

# # def suma (n):
# #         suma = 0
# #         for i in n:
# #                 suma = suma + int(i)
# #         return str(suma)
# #         if len (suma) > 2:
# #                 pass

# # print(suma ('16'))

# # def suma(n):
# # #     x = str(n)
# #     s = 0
# #     while len(n) > 1:
# #         s = 0
# #         for i in range(len(n)):
# #             s = s + int(n[i])
# #             x = str(s)
# #     return x

# # print(suma ('132189'))


# def sum(n):
#     while len(n) > 1:
#         suma = 0
#         for i in range(len(n)):
#             suma = suma + int(n[i])
#         n = str(suma)
#     return suma

# # print(sum('942'))

# # print (abs(-3))
# # circlePairsIn = ['12 0 21 14 0 23', '0 45 8 0 94 9', '35 0 13 10 0 38', '0 26 8 0 9 25']
# #    print(i.split()[5])
# # l = []
# # for cadena in circlePairs:
# #         l.append(cadena.split())
# # print(l)


# def relativePositions(circlePairs):
#     l = []
#     lstResponse = []
#     for cadena in circlePairs:
#         l.append(cadena.split())
#     for lst in l:
#         def dis(x1, x2, y1, y2):
#             from math import sqrt
#             d = sqrt((x2-x1)**2+(y2-y1)**2)
#             return d
#         touchingCondition = dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4])) == abs(int(
#             lst[5])-int(lst[2])) or int(lst[5]) + int(lst[2]) == dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4]))
#         concentricCondition = int(lst[0]) == int(
#             lst[3]) and int(lst[1]) == int(lst[4])
#         disjointOutsiderCondition = dis(int(lst[0]), int(lst[3]), int(
#             lst[1]), int(lst[4])) > int(lst[5]) + int(lst[2])
#         intersectingCondition = dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4])) < int(
#             lst[5]) + int(lst[2]) and dis(int(lst[0]), int(lst[3]), int(lst[1]), int(lst[4])) > int(lst[5]) - int(lst[2])
#         disjointInsiderCondition = dis(int(lst[0]), int(lst[3]), int(
#             lst[1]), int(lst[4])) < abs(int(lst[5]) - int(lst[2]))

#         if touchingCondition:
#             lstResponse.append('Touching')
#         elif concentricCondition:
#             lstResponse.append('Concentric')
#         elif intersectingCondition and not disjointInsiderCondition and not disjointOutsiderCondition:
#             lstResponse.append('Intersecting')
#         elif disjointOutsiderCondition:
#             lstResponse.append('Disjoint-Outsider')
#         elif disjointInsiderCondition:
#             lstResponse.append('Disjoint-Insider')
# #         return lstResponse
# # print(relativePositions(['12 0 21 14 0 23', '0 45 8 0 94 9', '35 0 13 10 0 38', '0 26 8 0 9 25']))


# def odd_even_product(list_of_numbers):
#     prod = 1
#     suma = 0
#     for num in list_of_numbers:
#         suma = suma + num
#     for num in list_of_numbers:
#         prod = prod * prod
#     if prod % 2 != 0:
#         return suma
#     else:
#         return 0
# # print(odd_even_product([1,2,3,4]))


# def complete_inventory(warehouse_1, x, warehouse_2, y):
#     back_index = len(warehouse_1)
#     first_pointer = x
#     second_pointer = y
#     while second_pointer > 0:
#         if first_pointer > 0 and warehouse_1[first_pointer] > warehouse_2[second_pointer-1]:
#             warehouse_1[back_index] = warehouse_1[first_pointer]
#         else:
#             warehouse_1[back_index-1] = warehouse_2[second_pointer-1]

#     return warehouse_1

# # print(complete_inventory([2,3,4,0,0,0],3,[1,5,9],3))



# def higher_future_temp( temperatures ) :
#         l = []
#         for index,temp in enumerate(temperatures):
#                 # print(index,temp)
             
        
# # higher_future_temp([21,22,21,22,25,21])


# def higher_future_temp(T):
#     n = len(T)
#     diasAEsperar = [0] * n
#     s = []
#     for i in range(n):
#         while(len(s) != 0 and T[s[-1]] < T[i]):
#             diasAEsperar[s[-1]] = i - s[-1]
#             s.pop(-1)
#         s.append(i)
#     for i in range(n):
#         print(diasAEsperar[i], end = " ")
        
# # print([1,2,3]*3)

# # dailyTemperatures([21,22,21,22,25,21])
# # higher_future_temp([22,23,21,25,23])


# def is_leap(year):
#       leap = False

#       if (year % 4 == 0) and (year % 100 != 0): 
#       # Note that in your code the condition will be true if it is not..
#         leap = True
#       elif (year % 100 == 0) and (year % 400 != 0):
#         leap = False
#       elif (year % 400 == 0):
#       # For some reason here you had False twice
#         leap = True
#       else:
#         leap = False

#       return leap

# # print(is_leap(2000))



# def print1AN (n):
#      l = []
#      for i in range(1, n+1):
#          l.append(i)
#         # print(i, end='')
#      return (''.join(str(e) for e in l))
# # print(print1AN(3))

# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y)
# # print(list(zipped))

# A = [1,2,3]
# B = [6,5,4]
# C = [7,8,9]
# X = [A] + [B] + [C]
# # print(X)
# # print (list(zip(*X)))

# digits = [1,2,3,4,5]
# words = ['one', 'two', 'three', 'four','five']
# zipobj = zip(digits, words)
# # print(list(zipobj))
# ## to unzip
# x,y = zip(*zipobj)
# # print(x)
# # print(y)


# # print('Hola mundo')


# def is_palindromo (s:str)-> bool:
#     return True if s[::-1] == s else False

# # print(is_palindromo('alagordadrogala'))

# # ===============================================================

# class Animal:
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad = edad

#     # Método genérico pero con implementación particular
#     def hablar(self):
#         # Método vacío
#         pass

#     # Método genérico pero con implementación particular
#     def moverse(self):
#         # Método vacío
#         pass

#     # Método genérico con la misma implementación
#     def describeme(self):
#         print("Soy un Animal del tipo", type(self).__name__)
        
# # Perro hereda de Animal
# class Perro(Animal):
#     pass

# mi_perro = Perro('mamífero', 10)
# # mi_perro.describeme()
# # Soy un Animal del tipo Perro


# # import string
# # alphabet = list(string.ascii_lowercase)
# # print(alphabet)

# def StringChallenge(texto):
#     import string
#     alphabet = list(string.ascii_lowercase)
#     l = []
#     str_low = texto.lower()
#     for i in str_low:
#         if i in alphabet:
#             l.append(str(alphabet.index(i) + 1))
#         else:
#             l.append(i)
#     return ''.join(l)
# # print(StringChallenge('FER-31'))

# # print(bin(4))
# binary = '11111111111111111111111111111011'
# # print(int(binary,2))
# x = 3.14159265
# # print(f'4 figures {x :.4}')

# core_fam = ['gabix', 'fers', 'vali', 'chow']
# external_fam = ['julix', 'felix', 'leo', 'vali2']
# # you can casta a list to a set, using the set function
# set_core_fam:set = set(core_fam)
# set_external_fam:set = set(external_fam)
# tuple1 = (0,'1','fer',3,3,4)
# list1 = [0,1,2,3,3,4,]
# set1 = {0,1,2,3,3,'fe2', tuple1}
# # print(tuple1, list1, set1)
# # print(set_core_fam)
# # print(set_external_fam)
# # print(list(set_core_fam.difference(set_external_fam)))

# biologia_califs = [10,7,10,8,5,9,6,6,7,8]
# mat_califs      = [5,8,5,8,5,7,6,6,5,8]
# fis_califs      = [9,8,5,6,5,7,6,6,5,8]

# list_of_lists = [biologia_califs, math_califs, phys_califs]
# list_of_tuples = list(zip(*list_of_lists))
# list_of_averages = [round(sum(t)/len(t),1) for t in list_of_tuples]
# print(list_of_averages)

# temp = 34.5745
# print(f'the temperature  is {temp:.3f}')



# You can iterate Lists in Parallel with zip

# names_1 = ['Fer', 'Maritet', 'fanytet']
# names_2 = ['Fer', 'Mari', 'kat']

# for name_1, name_2 in zip(names_1,names_2):
#     if name_1 == name_2:
#         print(f'{name_1} is repeated in both lists')
#     else:
#         print (name_1, name_2)



# dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
# dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
# ziped_dict = list(zip(dict_one.items(), dict_two.items()))
# # print(ziped_dict)

# names = ['Fer', 'Vale']
# ages = [30, 29]
# dict_formed = dict(zip(names, ages))
# print(dict_formed)


# dict_1 = {'name': 'fer', 'carrer': 'Physics'}
# dict_2 = {'name_2': 'vali', 'carrer_2': 'Admin'}
# new_dict = {**dict_1, **dict_2}
# print(new_dict)


decimal_number = 23
hexadecimal_value = hex(decimal_number)
# print(hexadecimal_value[2::])

character = 'P'
# find unicode of P
unicode_char = ord(character)
# print(unicode_char)
# Output: 80


# edad = int(input('Ingresa tu edad: '))
# print(f'tu edad en un año será:{edad +1 }')

dict_example = {"Fer": 32, "Norma": 45, "vale": 42}

l = dict_example.values()
# print(l)


users = [(0,'Fer','pass'), 
        (1, 'gabi', 'gueris'),
        (2, 'sydney', 'barbie20'), 
        (3, 'vale', 'moxita3000')]
l = []
for i_d, name, password in users:
    l.append({'id': i_d, 'name': name, 'pass': password})

# print(l)

# student_list = [{'name':'Jose', 'school': 'Computing', 'grades': (66,77,88)},
#                 {'name':'Fer', 'school': 'Science', 'grades': (88,77,90)},
#                 {'name':'Mich', 'school': 'Arts', 'grades': (89,78,80)}]

student_list = [{'grades': (1, 2, 3)},
{'grades': (0, 0, 0)},
{'grades': (2, 10, 55)}]
# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade
# received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        count += len(student['grades'])
        total += sum(student['grades'])
    return total / count

# print(average_grade_all_students(student_list))

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

# print(greeting(382))
# print(greeting(333333))



matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
flat = [x for row in matrix for x in row]
# print(sum(flat))

string = 'Fernando'

new_str = list(map(lambda x: 'R' if x == 'F' else x, string))
# print('The value of the new_str var is: ', new_str)

dict_test = {'name': 'fer','hoby': 'vg'}

# print(dict_test.items())


# try:
#     [1,2,3][4]
# except IndexError:
#     print('error')
# except:
#     print('exception')
# else:
#     print('something else h')
# finally:
#     print('cleaning up')
    
# a = 9
# a.__str__()
# print(type(a))

# a = {1:9, 2:8, 3:7, 4:6, 5:5}
# a.get(6)

class test():
    id = 0 
    def __init__(self, id):
        self.id = id
        id = 2
t = test(1)
# print(t.id)


self = {'name': 'fer', 'hair': 'black'}

# print(self.name)


class Dog():
    def __init__(self, owner:str):
        self.owner = owner   
        
    def get_basic_information(self) -> str:
        if self.owner == 'Valeria Valle':
            name = 'Hachicko'
            age = 10
            return f'{name} has {age} years old and the owner registred is: {self.owner}'
    
    def historial (self):
        pass
    
dog = Dog('Valeria Valle')

# print(dog.get_basic_information())
# one waay to flat a list of lists 
# list_of_lists:list = [[1,2,3], [4,6,7], [8,4,23,1]]
# flated_list:list = [value for sub_list in list_of_lists for value in sub_list]
# print(flated_list)

# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)


# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)

# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)


# def myFun(*args, **kwargs):
#     print("args: ", type(args))
#     print("kwargs: ", type(kwargs))


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
# myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name':name, 'price':price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return f'the total stock_price in {self.name} is:\
{sum([item['price'] for item in self.items])}'
sears = Store('sears')
sears.add_item('switch',50)
sears.add_item('switch2',500)
# print(sears.stock_price())



# ====================================================================
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def __repr__(self) -> str:
        return self.name
    
    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total:int = sum([item['price'] for item in self.items])
        # total = 0
        # for item in self.items:
        #     total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(f'{store.name} - franchise')
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return f'{store.name}, total stock proce: {store.stock_price()}'
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

# print(Store.franchise(store))  # returns a Store with name "Test - franchise"
# print(Store.franchise(store2))  # returns a Store with name "Amazon - franchise"

# print(Store.store_details(store))  # returns "Test, total stock price: 0"
# print(Store.store_details(store2))  # returns "Amazon, total stock price: 160"



# import re
# lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie", 'bad cookie']
# pattern = "bad"


# print(len(re.findall(pattern, ", ".join(lst))))
# print(", ".join(lst))


from typing import List
def average_calc (ls:List[int]) -> float:
    avg:float = sum(ls)/len(ls)
    return avg

# print(average([4,8,6]))
# alumns:List[str]      = ['Fer', 'Adri', 'Vale']
# bio_grades:List[int]  = [6,8,9]
# math_grades:List[int] = [5,7,9]

# list_of_tup = zip(alumns, bio_grades, math_grades)
# print(list(list_of_tup))

class Student:
    def __init__(self, name:str, age:int, group:int):
        self.name  = name
        self.age   = age
        self.group = group
    
    def return_asigned_group (self):
        return f'{self.name} has {self.age} years old and was asigned to the group {self.group}'
    

student_one = Student('Fernando', 15, 402)

# print(student_one.return_asigned_group())


list_of_prods = [{'prod': 'switch', 'price': 30}, {'prod': 'play', 'price': 49}]

# print(sorted(list_of_prods, key = lambda dict: dict['price'], reverse = True))  



class Schrodinger_cat ():
    box_state = ['box opened', 'box closed']










    











