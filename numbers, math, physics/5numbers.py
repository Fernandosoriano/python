# 1.- Is the Sequence Linear, Quadratic or Cubic?
# Create a function that determines if a given sequence is linear, quadratic or cubic.
# The input will be a list of numbers of varying lengths. The function should return 
# "Linear", "Quadratic" or "Cubic".

# LINK = https://edabit.com/challenge/vfuZia9ufckGzhGZh

def seq_level(lst:list) -> str: 
    """This is a function that receives a list, with a sequence
    of numbers, and the goal of this function is to determine if
    the sequence is linear, quadratic or cubic.

    Args:
        lst (list): List of a sequence of numbers

    Returns:
        str: A text indicating if the sequence is linear, quadratic
        or cubic.
    """
    try:
        first_list_of_diferences:list = [lst[index+1]-lst[index] for index in range(len(lst)-1)]
        if all(ele == first_list_of_diferences[0] for ele in first_list_of_diferences):
            return 'is lineal'
        else:
            second_list_of_diferences = [first_list_of_diferences[ind+1]-first_list_of_diferences[ind]
                                        for ind in range(len(first_list_of_diferences)-1)]
            if all(ele == second_list_of_diferences[0] for ele in second_list_of_diferences):
                return 'is cuadratic'
            else:
                return 'is cubic, o greater order'
    except Exception as e:
        print('::::::::::error:' ,e)
        return 'An error ocurred, please check the logs'

# TESTS:
# print(seq_level([1, 2, 3, 4, 5]))
# print(seq_level([3, 6, 10, 15, 21]))
# print(seq_level([4, 14, 40, 88, 164]))
