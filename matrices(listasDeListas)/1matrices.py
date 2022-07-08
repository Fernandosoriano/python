#1.-Finding Adjacent Nodes url ejercicio: https://edabit.com/challenge/3DAkZHv2LZjgqWbvW
matrix = [
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]
def is_adjacent(matrix, node1, node2):
        if matrix[node1][node2] == 1:
                print (True)
        else:
                print (False)
# is_adjacent(matrix,1,4)