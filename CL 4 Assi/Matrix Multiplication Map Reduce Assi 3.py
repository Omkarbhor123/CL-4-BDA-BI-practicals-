from collections import defaultdict
import numpy as np

# Function to multiply matrices using MapReduce
def matrix_multiply_mapreduce(A, B):
    A = np.array(A)
    B = np.array(B)

    # Check if multiplication is valid
    if A.shape[-1] != B.shape[0]:  
        raise ValueError("Number of columns in A must match number of rows in B")

    # Map Phase: Generate key-value pairs
    mapped_values = []
    
    """
    it will store output like this
    mapped_values = [
  ((0, 0), 5), ((0, 0), 14),
  ((0, 1), 6), ((0, 1), 16),
  ((1, 0), 15), ((1, 0), 28),
  ((1, 1), 18), ((1, 1), 32)
  ]

"""

    for i in range(A.shape[0]):  # Rows in A
        for j in range(B.shape[-1]):  # Columns in B
            for k in range(A.shape[-1]):  # Matching dimension
                mapped_values.append(((i, j), np.dot(A[i, k], B[k, j])))

    # Reduce Phase: Aggregate values
    result_matrix = defaultdict(int)
    for key, value in mapped_values:
        result_matrix[key] += value



    """
      Key  	Values Added	Final Value
    (0, 0)	  5 + 14	       19
    (0, 1)	   6 + 16	       22
      """

    # Convert to final matrix format
    rows_A, cols_B = A.shape[0], B.shape[-1]
    return [[int(result_matrix[(i, j)]) for j in range(cols_B)] for i in range(rows_A)]

# Example matrices (works for 1D, 2D, and 3D)
A_1D = [[2, 3, 4]]  # 1x3
B_1D = [[1], [2], [3]]  # 3x1

A_2D = [[1, 2], [3, 4]]  # 2x2
B_2D = [[5, 6], [7, 8]]  # 2x2

A_3D = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # 2 layers, 2x2 matrices
B_3D = [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]  # 2 layers, 2x2 matrices

Ac_3D = [
    [2, 4, 1],
    [0, 1, 3],
    [5, 2, 2]
]

Bc_3D = [
    [1, 3, 2],
    [4, 0, 1],
    [2, 5, 3]
]


# Running the multiplication
print("1D Multiplication:", matrix_multiply_mapreduce(A_1D, B_1D))
print("2D Multiplication:", matrix_multiply_mapreduce(A_2D, B_2D))
print("3D Multiplication:", matrix_multiply_mapreduce(A_3D, B_3D))
print("3D Multiplication:", matrix_multiply_mapreduce(Ac_3D, Bc_3D))