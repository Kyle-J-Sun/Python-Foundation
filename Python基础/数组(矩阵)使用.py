
# 三位数组
c = np.array([
    [
        [1,2,3,4],
        [3,2,1,4],
        [2,3,4,5]
    ],
    [
        [1,2,3,4],
        [3,2,1,4],
        [2,3,4,5]
    ]
])

print(c.ndim)  #秩，轴的数量或维度的数量
print(c.shape)  #ndarra对象的尺度，对于矩阵，n行m列
print(c.size)   #ndarray对象元素的个数，n*m的值
print(c.dtype)  #元素类型
print(c.itemsize) #每个元素大小，以字节为单位

d = np.arange(20)
print(d)
e = np.ones((2,3,4), dtype = np.int)
print(e)
f = np.zeros((2,6))
print(f)
p = np.eye(6)
print(p)

a = np.linspace(1,10)
print(a)
b = np.linspace(1,10,6)
print(b)

c1 = e.reshape((3,8))
print(c1)
print(e)
c2 = e.resize((4,6))
print(e)

f1 = e.flatten() #降维
print(f1)

a1 = e.astype(np.float) #拷贝e数组到新数组
print(a1)

t1 = np.full((2,4,5), 33, dtype=np.int32)
to1 = t1.tolist() #数组向列表变换
print(to1)

m1 = np.array([1,4,5,6,7,1,4,2])
print(m1[5])
print(m1[1:4:2])

matrix1 = np.array([
    [
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
    ],
    [
        [12,13,14,15],
        [16,17,18,19],
        [20,21,22,23]
    ]
])
print(matrix1)
matrix2 = np.full_like(matrix1,34)
print(matrix2)

mm1 = matrix1.mean()
print(mm1)
mmm1 = matrix1 / mm1
print(mmm1)

fun1 = matrix1 * matrix2
print(fun1)