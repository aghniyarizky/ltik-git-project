import numpy as np

nilai = np.array([90, 80, 55, 99, 98, 80, 73, 62, 78, 46,
                  91, 81, 15, 91, 91, 89, 72, 65, 72, 45,
                  22, 31, 77, 66, 45, 55, 34, 33, 22, 88])

balik = np.sort(nilai)[::-1]
besar = balik[0:5]
print("Nilai terbesar ke terkecil :", balik)
print("5 nilai terbesar :", besar)