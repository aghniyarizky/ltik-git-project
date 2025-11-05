# rumus = (derajat C x 9/5) + 32 = 32F
import numpy as np

suhu = np.array([20, 15, 21, 22, 18, 19, 20, 17, 16, 15])
konversi = (suhu * 9/5) + 32
tipedata = np.array(konversi, dtype="i")
print(suhu, "= derajat Celcius")
# print(konversi, "= derajat Fahrenheit")
print(tipedata, "= derajat Fahrenheit")