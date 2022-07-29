import numpy as np

a = np.array([-1, 1, 2, 3, 4, 5, 6, 7], dtype=float)
a_list = [1, 2, 3, 4, 5, 6, 7]
print((a + 3) * 2, a-1)

x_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(x_2d[0][2], x_2d[0].min(), x_2d[1].min())


x = np.array([[[i+j+k for k in range(5)]for j in range(4)] for i in range(3)])
print(x_2d.shape)
print(x.shape)
print(x.size, x_2d.size)

one_matrix = np.ones((3, 3), dtype=np.int64)
print(one_matrix, one_matrix.size, one_matrix.shape)
#  создание единичной матрицы нужного размера

print(x_2d[0].sum(), x_2d[1].sum())


print('second part of lesson')
lins = np.linspace(0, 15, 20)
print(lins)
print(x_2d)
print(x_2d[1::])
print(a)
print(a[::-1])

x_2 = np.array([[i for i in range(10, 20)], [i for i in range(100, 110)]])
print(x_2)
print(x_2.shape, x_2.size, x_2[0, 4], x_2[0][4])
print(x_2[:, 3:5])
print(x_2[:, 0:2])
print(x_2[:, 4:6], x_2[1, 0:2] == x_2[1][0:2])

print(x_2[::-1, :])       # change matrix rows 1 - 2
# print(x_2[::-1][:]

some_np = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f']
                   ])

print(some_np[0, 0:2], ord('a'), chr(97))

vector = np.arange(9)
print(vector.shape, vector.size, vector.min(), vector.max())
print(vector.reshape((3, 3)))

vector = np.arange(12)
print(vector.shape, vector.size, vector.min(), vector.max())
print(vector.reshape((3, 4)))
print(vector.reshape((2, 6)))

print(np.sqrt(vector), np.sin(vector))
# print(np.log(vector))

print(vector.astype(bool))
print(vector.astype(np.float_))
print(f'Mediana of vector {np.median(vector)}, Med: {vector.mean()}')

# exercise 1
x_ones = np.ones((1, 2, 3))
print(x_ones.size, x_ones.shape)
print(x_ones.sum(axis=2))

x_v = np.array([1, 2, 3])
y_v = np.array([4, 5, 6])
print(np.concatenate([x_v, y_v]))


x_req = [1, 2, 3, 4]
r = x_req.copy()           # copy numpy arrays
print(x_req)

x_req.append(6)
print(r, x_req)
