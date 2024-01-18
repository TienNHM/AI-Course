import numpy as np

# Exercise 6
def transpose(matrix):
    return np.transpose(matrix)


# Exercise 7
def product(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        return "Khong co tich ma tran"
    
    return np.dot(matrix1, matrix2)

def Hadamard(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        return "Khong co tich Hadamard"
    
    return np.multiply(matrix1, matrix2)


# Exercise 8
def replace_col(mat, col_ind):
    '''Relace column col_ind of matrix mat with a column of ones (1)
    Args:
        mat: a numpy matrix
        col_ind: index of column to be replaced (0-based)

    Returns:
        a numpy matrix with column col_ind replaced with a column of ones (1)

    Example:
        mat = np.array([[1, 2, 3], [4, 5, 6]]) \n
        replace_col(mat, 1) = np.array([[1, 1, 3], [4, 1, 6]])
    '''

    mat[:, col_ind] = 1
    return mat


if __name__ == "__main__":
    print("Câu 6: ")
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Ma trận ban đầu: ")
    print(matrix)

    print("Ma trận chuyển vị: ")
    print(transpose(matrix))


    print("Câu 7: ")
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[1, 2], [3, 4], [5, 6]])

    print("Tích của hai ma trận: ")
    print(product(matrix1, matrix2))

    print("Hadamard của hai ma trận: ")
    print(Hadamard(matrix1, matrix2))


    print("Câu 8: ")
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    print("Ma trận ban đầu: ")
    print(mat)

    col_ind = int(input("Nhập chỉ số cột cần thay thế: "))
    print("Ma trận sau khi thay thế cột " + str(col_ind) + " bằng một cột toàn số 1: ")
    print(replace_col(mat, col_ind=col_ind))