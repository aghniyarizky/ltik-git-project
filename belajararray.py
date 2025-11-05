# gapake from waktu ngimport
# import array 

# arr = array.array('i', [1,2,3])
# arr2 = array.array('i', [4, 5, 6])
# arr.extend(arr2)
# print(arr)


# pakai from waktu ngimport
# from array import array 

# arr = array('i', [1,2,3])
# arr2 = array('i', [4, 5, 6])
# arr.extend(arr2)
# print(arr)


# pake numpy
import numpy as np
# print(np.__version__)
# arr = np.array([10, 20, 30, 40, 50, "4"]) #contoh 
arr = np.array([10, 20, 30, 40, 50])
print (arr * 2)
print(arr)
print(type(arr))

list = [1,2,3,4,5]
print(list)
print(type(list))

print("")

# fungsionalitas
a = np.array(([1,2,3]))
print(np.mean(a)) #harus pake np. soalnya mean bukan elemen langsung dari python
print(sum(a)) #sum gausah pake np. soalnya udah elemen dari python

print("")

# index array
arr3 = np.array([1,2,3,4,5])
print(arr3[1])
print(arr3[2:5])
print(arr3[0] + arr3[4])

# ndarray = end array
# kalo misal isi arraynya int semua, trus tiba2 muncul str walaupun sebiji, 
# nanti semuanya malah jadi str
# hierarki = bool -> int -> float -> str

# multidimensional
print("")
# 2d (matriks huwekk)
matriks = np.array([[1, 0, 0], [0, 1, 0]])
print(matriks)

print("")
print("3d")
# 3d (matriks huwekk)
matriks3d = np.array([ [[1, 0], [0, 1]], [[0, 1], [1, 0]], [[0, 1], [0, 1]] ])
print(matriks3d)

# array n dimensi (ND) n itu jumlah dimension array. bisa 4d 5d dll.
# pake ndim buat kembaliin bil bulat yg memberitahu berapa byk dimensinya
print(arr3.ndim)
print(matriks.ndim)
print(matriks3d.ndim) #cek berapa dimensi array yg namanya matriks3d

# tipe data array disingkat2
# misal int jadi i, boolean, unsigned 

# cek tipe data pake dtype
cektipe = np.array([1, 0, 0])
print(cektipe.dtype)

cektipedata = np.array([1, 0, 0], dtype="S")
print(cektipedata)
print(cektipedata.dtype)