
import numpy as np


def basic():
    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)
    
    # elementwise sum
    print(x + y)
    print(np.add(x, y))
    
    # elementwise difference
    print(x - y)
    print(np.subtract(x, y))
    
    # elementwise product
    print(x * y)
    print(np.multiply(x, y))

    # elementwise division
    print(x / y)
    print(np.divide(x, y))

    # elementwise square root
    print(np.sqrt(x))


def matrix():
    # matrix multiply: np.dot
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])

    v = np.array([9, 10])
    w = np.array([11, 12])

    # Inner product of vectors
    print(v.dot(w))
    print(np.dot(v, w))

    # Matrix / vector product
    print(x.dot(v))  # rank 1 array [29, 67]
    print(np.dot(x, v))
    
    # Matrix / matrix product
    print(x.dot(y))
    print(np.dot(x, y))
    

def built_in():
    x = np.array([[1, 2], [3, 4]])
    # sum
    print(np.sum(x))  # compute sum of all elements, prints "10"
    print(np.sum(x, axis=0))  # compute sum of each column, prints "[4, 6]"
    print(np.sum(x, axis=1))  # compute sum of each row, prints [3, 7]

    # transpose
    print(x)
    print(x.T)
    v = np.array([1, 2, 3])
    # NOTE: take the transpose of a rank 1 array does nothing
    print(v)  # [1, 2, 3]
    print(v.T)  # [1, 2, 3]


def broadcast():
    # add the vector v to each row of the matrix x
    # method 1: loop
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = np.empty_like(x)

    for i in range(4):  # loop is slow
        y[i, :] = x[i, :] + v 
    print(y)

    # mothod 2: np.tile
    vv = np.tile(v, (4, 1))
    print(vv)
    y = x + vv
    print(y)

    # mothod 3: broadcast
    y = x + v
    print(y)

    """
    rule of broadcast:
        1. 如果数组的秩不同，使用1来将秩较小的数组进行扩展，直到两个数组的尺寸的长度都一样
        2. 如果两个数组在某个维度上的长度是一样的，或者其中一个数组在该维度上长度为1，那么我们就说这两个数组在该维度上是相容的
        3. 如果两个数组在所有维度上都是相容的，他们就能使用广播
        4. 如果两个输入数组的尺寸不同，那么注意其中较大的那个尺寸。因为广播之后，两个数组的尺寸将和那个较大的尺寸一样
        5. 在任何一个维度上，如果一个数组的长度为1，另一个数组长度大于1，那么在该维度上，就好像是对第一个数组进行了复制
    """

    # outer product
    v = np.array([1, 2, 3])  # shape (3,)
    w = np.array([4, 5])  # shape (2,)
    print(np.reshape(v, (3, 1)) * w)

    # add a vector to each row of a matrix
    x = np.array([[1, 2, 3], [4, 5, 6]])
    print(x + v)

    # add a vector to each column of a matrix
    print(x.T + w).T
    print(x + np.reshape(w, (2, 1)))
    # NOTE: x + w is not supported

    # multiply a matrix by a constant
    print(x * 2)
