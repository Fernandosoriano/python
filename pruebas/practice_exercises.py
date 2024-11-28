# input = [1,4,2, 2, 3, 3, 3, 4]
# Output: {1: 1, 2: 2, 3: 3, 4: 1}
# return_dict = lambda ls: {num: ls.count(num) for num in ls}  

# def return_dict(ls):
#     count_dict = {}
#     for num in ls:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#     return count_dict  

# print(return_dict(input))

# ========================================================================================

# def is_anagram (str_1, str_2):
#     ls = []
#     for letter_str_1 in str_1:
#         if letter_str_1 in str_2 and str_1.count(letter_str_1) == str_2.count(letter_str_1):
#             ls.append(True)
#         else:
#             ls.append (False)
#     return True if all(l == True for l in ls) else False


# from collections import Counter

# str_1 = "listen"
# str_2 = "silent"

# counter_1 = Counter(str_1)  # {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
# counter_2 = Counter(str_2)  # {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}

# # Comparing the two counters
# are_anagrams = counter_1 == counter_2  # This will be True

# print(is_anagram( "hello", "oellh"))
# print(is_anagram("hello", "world"))
# ===============================================================================================

def find_missing_num (ls:list):
    full_list = [num for num in range(1, len(ls)+2)]
    for num in full_list:
        if num not in ls:
            return num

# print(find_missing_num([3, 7, 1, 2, 8, 4, 5]))
# print(find_missing_num([1, 2, 4, 6, 3, 7, 8]))



countTrue_2  = lambda ls: ls.count(True)
# print(countTrue_2([True, False, False, True, False]))

ls = [1,1,2,2,3,5,6,8,8,9]
# print(list(set(ls)))

from typing import List, Dict
from collections import Counter

def return_unique (ls:List) -> List:
    """_summary_

    Args:
        ls (List): _description_

    Returns:
        List: _description_
    """
    try:
        dict_counter:Dict = dict(Counter(ls))
        return [k for k,v in dict_counter.items() if v == 1]
    except Exception as e :
        print(f'The following error: {e} occurs')
# print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))


# From a list of numbers, move zero to the end of the list
list = [1,0,2,0,4,6]

def remove_zeros(list:List):
    try:
        for item in list:
            if item == 0:
                list.remove(item)
                list.append(0)
        return list
    except Exception as e:
        print(f'This error: {e} ocurred')

# print(remove_zeros(list))

list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 

res = [j for i in [list1, list2] for j in i] 



reverse_chain = lambda str: str[::-1]

# print(reverse_chain('fer'))


# Escribe una función en Python llamada find_even_numbers que reciba una lista de números y devuelva
# una nueva lista que contenga solo los números pares.

def return_even_numbers (ls:List) -> List:
    """This is a function that receives a list of
    numbers, and returns a list that contains
    just even nummbers

    Args:
        ls (List): A list with numbers to check
        if it has even numbers

    Returns:
        List: A list that only contains even numbers
    """
    even_ls:List = [num for num in ls if num%2 == 0]
    return even_ls

# print(return_even_numbers([1, 2, 3, 4, 5, 6]))



# Write a function in Python called count_char_frequency that takes a string as input and returns a dictionary
# where the keys are characters
# and the values are the number of times each character appears in the string.
def count_char_frequency (str:str) -> Dict:
    """This is a function that receives a string
    and returns a ditionary  that cotains
    the letter as a key and the value  is the frequency
    of this letter (key)

    Args:
        str (str): A string to analyze

    Returns:
        Dict: A dictionary with  the frequency of each letter
        of the string received
    """
    counter_dict:Dict = dict(Counter(str))
    return counter_dict


# print(count_char_frequency('hello'))



# Write a function in Python called fizzbuzz that takes an integer n as input and prints the numbers 
# from 1 to n. However, for multiples of three, print "Fizz" instead of the number, and for the 
# multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

def fizzbuzz (n:int):
    for num in range (1,n+1):
        if num%3==0 and num%5==0:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')
        else:
            print(num)
            
# fizzbuzz(15)

# ===========================================================================================================
def merge_intervals (ls:List) -> List:
    ls_sorted:List = sorted(ls,key= lambda tup: tup[0])
    merged_list:List = []
    for tup in ls_sorted:
        if len (merged_list) == 0:
            merged_list.append(tup) 
            continue
        if tup[0] < merged_list[-1][1]:
            merged_list.append((merged_list[-1][0], tup[1]))
        else:
            merged_list.append(tup)
    return merged_list
# =============================================================================================
from typing import List,Tuple
def merge_intervals_2(ls: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    ls_sorted: List[Tuple[int, int]] = sorted(ls, key=lambda tup: tup[0])
    merged_list: List[Tuple[int, int]] = []
    for tup in ls_sorted:
        if len(merged_list) == 0:
            merged_list.append(tup)
            continue
        else:
            last_interval = merged_list[-1]
            if tup[0] <= last_interval[1]:  # Verifica si hay superposición
                # Actualiza el último intervalo con el nuevo final más grande
                merged_list[-1] = (last_interval[0], max(last_interval[1], tup[1]))
            else:
                merged_list.append(tup)    
    return merged_list
# Ejemplo de prueba
# print(merge_intervals_2([(1, 3), (2, 6), (8, 10), (15, 18)]))  # Espera [(1, 6), (8, 10), (15, 18)]
# print(merge_intervals_2([(1, 5), (2, 6), (3, 7)]))


def find_unique(ls:List[int]) -> int:
    from collections import Counter
    count_dict = dict(Counter (ls))
    for k,v in count_dict.items():
        if v == 1:
            return k
    return'the unique number doesnt exist'

entrada = [4, 1, 2, 1, 2]
# print(find_unique(entrada))
# ===================================================================================================================0
def is_anagrama (str_1:str, str_2:str) -> bool:
    str_1_format:str = str_1.replace(" ", "").lower()
    str_2_format:str = str_2.replace(" ", "").lower()
    return Counter(str_1_format) == Counter(str_2_format)

# print(is_anagrama("liste n", "Silen t"))

# =====================================================================================================================


def find_missing_numbers(min_num:int, max_num:int, ls:List[int]) -> List[int]:
    """_summary_

    Args:
        min_num (int): _description_
        max_num (int): _description_
        ls (List[int]): _description_

    Returns:
        List[int]: _description_
    """
    try:
        complete_list:List[int] = [num for num in range(min_num, max_num+1)]
        res_list:List[int] = [num for num in complete_list if num not in ls]
        return res_list
    except Exception as e:
        return f'the following error: {e} ocurred'
# print(find_missing_numbers(1, 10, [1, 2, 3, 5, 6, 7, 10]))  # Debe retornar [4, 8, 9]

def find_unique_subsets (in_ls:List):
    ls: List[List] = [[]]
    for num in in_ls:
        new_subsets = []
        for sub in ls:
            new_subset = sub + [num]
            new_subsets.append(new_subset)
        ls.extend(new_subsets)
    return ls      
    
# print(find_unique_subsets([1, 2, 3]))


# def specific_sum (nums:List[int]):
#     for num in nums:


# print(specific_sum([2, 4, 3, 3, 5, -1, 0]))

nums = [2, 4, 3, 3, 5, -1, 0]
# tarjet = 4

def sum_tarjet (nums, tarjet):
    l = []
    res = []
    for num in nums:
        for idx in range (len(nums)):
            if idx == nums.index(num):
                continue
            if  nums[idx]+num == tarjet and (nums[idx], ):
                l.append((nums[idx], num))
                
    for tup in l:
        if tup and tup[::-1] not in res:
            res.append(tup)
    return res

# print(res, '|', l)
# print(sum_tarjet(nums,4))



def sum_target_op(nums: List[int], target: int) -> List[Tuple[int, int]]:
    res = []
    seen = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pair = (diff, num) if diff < num else (num, diff)
            if pair not in res:
                res.append(pair)
        seen.add(num)
    
    return res
nums = [1, 2, 3, 4, 5]
target = 6

# print(sum_target_op(nums, target))


def find_duplicates (nums:List[int]):
    l = []
    res = []
    for num in nums:
        if num not in l:
            l.append(num)
        elif num not  in res:
            res.append(num)
    return ('res=',res,'l =', l)
# print(find_duplicates([1, 2, 2, 3, 3, 3, 4, 4]))

# =========================================================================================
# Write a function that finds the maximum sum of k consecutive elements in a list of integers. If
# the list has fewer than k elements, the function should return None.

from typing import Optional
def max_consecutive_sum(nums: List[int], k: int) -> Optional[int]:
    res_ls = []
    sum_ls = []
    for idx in range(len(nums)):
        if len(nums) < k:
            return None
        if len(nums[idx:idx+k:]) == k:
            res_ls.append(nums[idx:idx+k:])
    for ls in res_ls:
        sum_ls.append(sum(ls))
    max_idx = sum_ls.index(max(sum_ls))
    return max(sum_ls), res_ls[max_idx], res_ls
# TESTS:
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# nums = [4, -1, 2, 1, 6]
# k = 4
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
nums = [1, 2, 3, 4, 5]
k = 2
# nums = [4, 3]
# k = 3
# nums = [-2, -3, -4, -1]
# k = 2
# print( max(nums))
# print(max_consecutive_sum(nums,k))
# optimized version:
def max_consecutive_sum_op(nums: List[int], k: int) -> Optional[Tuple[int, List[int]]]:
    if len(nums) < k:
        return None
    # Calculate the sum of the first window
    max_sum = current_sum = sum(nums[:k])
    start_idx = 0
    # Slide the window across the array
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]  # Move the window by adding new element and removing the old
        if current_sum > max_sum:
            max_sum = current_sum
            start_idx = i - k + 1  # Update the start index of the max sum window
    max_subarray = nums[start_idx:start_idx + k]
    return max_sum, max_subarray
# print(max_consecutive_sum_op(nums,k)


