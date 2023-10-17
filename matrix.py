matrix = [[0,1,9],
          [5,6,1],
          [6,3,4]]



def find_matrix_det(matrix):
  if len(matrix) == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  else:
    total = 0
    for x in range(len(matrix[1])):
      minor = find_matrix_minor(matrix, 1, x)
      total += matrix[1][x] * ((-1) ** (x+1)) * find_matrix_det(minor)
    return total


def transpouse(mat):
  matrix = []
  for i in range(len(mat[0])):
    matrix.append(list())
    for j in range(len(mat)):
      matrix[i].append(mat[j][i])
  return matrix   


def find_matrix_minor(matrix,i,j):
  return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

new_arr = []

def main(matrix):
  new_row = []
  determinant = find_matrix_det(matrix)
  transpoused_mat = transpouse(matrix)
  for i in range(len(transpoused_mat)):
    for j in range(len(transpoused_mat[i])):
      minor = find_matrix_minor(transpoused_mat,i,j)
      cofactor = (-1) ** (j+i) * find_matrix_det(minor)
      new_row.append(cofactor*1/determinant)
      if len(new_row) == 3:
        new_arr.append(new_row)
        new_row = []
  return new_arr    



print(main(matrix))






