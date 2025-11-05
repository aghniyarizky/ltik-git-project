import numpy as np

keuntungan = np.array([90000, 30000, 40000, 50000, 21000, 43000, 100000,
                       89000, 79000, 43000, 59000, 26000, 43000, 80000])

untung = np.mean(keuntungan)
untung = np.array(untung, dtype="i")
print("Rata-rata keuntungan: Rp.", untung)

print("Keuntungan tertinggi: Rp.", np.max(keuntungan), "hari ke-", np.argmax(keuntungan)+1)
print("Keuntungan terendah: Rp.", np.min(keuntungan), "hari ke-", np.argmin(keuntungan)+1)