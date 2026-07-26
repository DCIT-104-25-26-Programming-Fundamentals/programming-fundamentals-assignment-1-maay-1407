# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    """Helper function to print a matrix in a neat grid format."""
    for row in matrix:
        print(" ".join(f"{val:>4}" for val in row))


def read_matrix(rows, cols, name=""):
    """Helper function to read a matrix from user input line by line."""
    if name:
        print(f"\nEnter entries for Matrix {name}:")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) == cols:
                matrix.append([float(val) for val in row_input])
                break
            print(f"Error: Please enter exactly {cols} numbers separated by spaces.")
    return matrix



def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed



def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        row_sum = []
        for j in range(cols):
            row_sum.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row_sum)

    return result
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

   
    result = []
    for i in range(rows_a):
        row_res = []
        for j in range(cols_b):
            # Compute the dot product of row i from A and column j from B
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            row_res.append(dot_product)
        result.append(row_res)

    return result



def main():
    print("=== PART A: TRANSPOSE MATRIX ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    mat_a = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(mat_a)

    transposed = transpose_matrix(mat_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    print("\n" + "=" * 40)
    print("=== PART B: ADD TWO MATRICES ===")
    print(f"Reading two matrices of size {m} x {n}...")
    mat_b1 = read_matrix(m, n, "1")
    mat_b2 = read_matrix(m, n, "2")

    sum_res = add_matrices(mat_b1, mat_b2)
    print("\nSum Matrix:")
    print_matrix(sum_res)

    print("\n" + "=" * 40)
    print("=== PART C: MULTIPLY TWO MATRICES ===")
    m_a = int(input("Enter rows for Matrix A: "))
    n_a = int(input("Enter columns for Matrix A: "))

    # Number of rows in B must equal number of columns in A
    n_b = int(input(f"Enter columns for Matrix B (rows will automatically be {n_a}): "))

    mat_c1 = read_matrix(m_a, n_a, "A")
    mat_c2 = read_matrix(n_a, n_b, "B")

    prod_res = multiply_matrices(mat_c1, mat_c2)
    print("\nProduct Matrix (A x B):")
    print_matrix(prod_res)


if __name__ == "__main__":
    main()