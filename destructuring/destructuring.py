        ####### Standard destructuring assignments ######
a, b = 5, 11
# print(a,b)

# the previous example is the same thing as: 
c,d = (5,11)
# print(c,d)

# And also  you can destructure other iterables
# like tuples, lists, strings, dicts or even sets
# altought you have to remeber that sets doesnt have order
# examples:

##### destructuring a list########
e,f,g = [1,2,3]
# print(e,f,g)

######## destructuring a chain ###############
h,i,j = 'Fer'
# print(h,i,j)


######### Destructuring dictionaries in Python#########
fer_dict = {'name': 'fer', 'weight': 70, 'hair':'black'}

# for defect in a destructuring process of a dict python takes
# the keys as values for the asignment of the variables
k,l,m = fer_dict  
# print(k,l,m)

n,o,p = fer_dict.values()
# print(n,o,p)

    
### # Ignoring Values###
# when you don't want to assign a value, you can use
# an underscore, this is for convention
x,_,z = 1,2,3
# print(x,z)



####### Using * to Collect Values##########
L = ["Fernando", 0]
head, *tail = L
# print(head, tail)




                    # Destructuring in for loops
people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    pass
	# print(f"Name: {name}, Age: {age}, Profession: {profession}")

for key,value in fer_dict.items():
    pass
    # print(key,value)
    
example_list = ["A", "B", "C"]

for counter, letter in enumerate(example_list):
    pass
	# print(counter, letter)