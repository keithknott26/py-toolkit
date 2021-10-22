import numpy as np

def construct():
    a = np.array([1, 2, 3])  # constuct arry from list
    print(type(a))  # Prints "<type 'numpy.ndarray'>"
    print(a.shape)  # (3,)
    print(a[0], a[1], a[2])
    a[0] = 5
    print(a)  # [5, 2, 3]

    b = np.array([[1, 2, 3], [4, 5, 6]])  # create a rank 2 array
    print(b)
    print(b.shape)  # (2, 3)
    print(b[0, 0], b[0, 1], b[1, 0])  # 1 2 4

    a = np.zeros((2, 2))
    print(a)  # [[0. 0.], [0. 0.]]
    b = np.ones((1, 2))
    print(b)  # [[1. 1.]]
    c = np.full((2, 2), 7)
    print(c)  # [[7. 7.], [7. 7.]]
    d = np.eye(2)  # create a 2*2 identity matrix
    print(d)  # [[1. 0.], [0. 1.]]
    e = np.random.random((2, 2))  # create an array filled with random values
    print(e)  # might print [[0.91940167, 0.08143941], [0.68744134, 0.87236687]]

def access():
    # slice
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    b = a[:2, 1:3]  # [[2, 3], [6, 7]]
    # NOTE: A slice of an array is a view into the same data, so modifying
    # it will modify the original array
    print(a[0, 1])  # 2
    b[0, 0] = 77
    print(a[0, 1])  # 77

    # mixing int and slice
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    row_r1 = a[1, :]  # NOTE: rank 1 view of the second row of a
    row_r2 = a[1:2, :]
    print(row_r1, row_r1.shape)  # [5, 6, 7, 8] (4,)
    print(row_r2, row_r2.shape)  # [[5, 6, 7, 8]] (1, 4)

    col_r1 = a[:, 1]
    col_r2 = a[:, 1:2]
    print(col_r1, col_r1.shape)  # [2, 6, 10], (3,)
    pritn(col_r2, col_r2.shape)  # [[2], [6], [10]], (3, 1)

    # NOTE: int array access
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a[[0, 1, 2], [0, 1, 0]])
    print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # equivalent to above

    print(a[[0, 0], [1, 1]])  # you can reuse the same element 
    print(np.array([a[0, 1], a[0, 1]]))  # equivalent to above

    # NOTE: use int array access to select or mutate one element from each row
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print(a)

    b = np.array([0, 2, 0, 1])  # create an array of indices
    print(a[np.arange(4), b])  # [1, 6, 7, 11], select one element from each row of a using the indices in b

    a[np.arange(4), b] += 10
    print(a)

    # NOTE: bool array access
    a = np.array([[1, 2], [3, 4], [5, 6]])
    bool_idx = (a > 2)  # the same shape as a
    print(bool_idx)
    print(a[bool_idx])  # [3, 4, 5, 6], rank 1 array
    print(a[a > 2])  # [3, 4, 5, 6]


def dtype():
    x = np.array([1, 2])  # Let numpy choose the datatype
    print(x.dtype)  # Prints "int64"

    x = np.array([1.0, 2.0])
    print(x.dtype)  # Prints "float64"

    x = np.array([1, 2], dtype=np.int64)  # Force a particular datatype
    print(x.dtype)  # Prints "int64"


