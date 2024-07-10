keys = ['name', 'age', 'hair']
values = ['vali', '20', 'brown']
dict_formed = dict(zip(keys,values))
# print(dict_formed)


fruits = ['apple', 'peach', 'banana']
fruits_2 = ['apple', 'orange', 'watermelon']
for fruit_1, fruit_2 in zip(fruits, fruits_2):
    # print(fruit_1, fruit_2)
    if fruit_1 == fruit_2:
        print(f'the fruit that appears in both lists is: {fruit_1}')
        

# obj = zip(keys, values)
# print('obj:', list(obj))