import numpy as np
from numexpr.expressions import double

# İki liste elemanlarının çarpımı (klasik yöntem)
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []

for i in range(len(a)):
    ab.append(a[i] * b[i])

print("Liste ile çarpım:", ab)

# NumPy ile elemanların çarpımı
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
print("NumPy ile çarpım:", a * b)

print("\n" + "#" * 30 + "\n")

# NumPy Array Oluşturma
print(np.array([1, 2, 3, 4, 5]))
print("Array tipi:", type(np.array([1, 2, 3, 4, 5])))

# Boş bir array oluşturma
print("10 elemanlı sıfırlardan oluşan array:", np.zeros(10, dtype=double))

# Rastgele sayılarla array oluşturma
print("0 ile 10 arasında 5 rastgele sayı:", np.random.randint(0, 10, 5))

# Belirli bir istatistiksel dağılıma göre sayı üretmek
print("Normal dağılımlı 3x4 array:", np.random.normal(10, 4, (3, 4)))

print("\n" + "#" * 30 + "\n")

# NumPy Array Özellikleri (Attributes)
a = np.random.randint(10, size=5)
print("Array:", a)
print("Boyut sayısı (ndim):", a.ndim)
print("Boyut bilgisi (shape):", a.shape)
print("Toplam eleman sayısı (size):", a.size)
print("Veri tipi (dtype):", a.dtype)

print("\n" + "#" * 30 + "\n")

# Yeniden Şekillendirme (Reshaping)
ar = np.random.randint(1, 10, size=9)
print("Düz array:", ar)
print("3x3 array:", ar.reshape(3, 3))

print("\n" + "#" * 30 + "\n")

# Index Seçimi (Index Selection)
a = np.random.randint(10, size=10)
print("Array:", a)
print("İlk eleman:", a[0])
print("İlk 5 eleman:", a[0:5])
a[0] = 999
print("0. indexe 999 atandıktan sonra:", a)

# 2D array
m = np.random.randint(10, size=(3, 5))
print("2D Array:\n", m)
print("0,0 index:", m[0, 0])
print("1,1 index:", m[1, 1])
m[2, 3] = 45
print("2,3 index 45 olarak güncellendi:", m)

# NumPy tip düzeltmesi (fix type)
m[2, 1] = 2.9
print("2,1 indexe 2.9 atandıktan sonra (integer olarak kaydedilir):", m)

# Slicing
print("0. sütun:", m[:, 0])
print("1. satır:", m[1, :])
print("İlk iki satır, ilk üç sütun:\n", m[0:2, 0:3])

print("\n" + "#" * 30 + "\n")

# Fancy Index
v = np.arange(0, 30, 3)
catch = [1, 2, 3]
print("Fancy index seçimi:", v[catch])

print("\n" + "#" * 30 + "\n")

# NumPy'da Koşullu İşlemler (Conditions on Numpy)
v = np.array([1, 2, 3, 4, 5])

# Klasik döngü ile
ab = []
for i in v:
    if i < 3:
        ab.append(i)
print("Döngü ile filtreleme:", ab)

# NumPy ile
print("Koşullu filtreleme:", v[v < 3])
print("v > 3:", v[v > 3])
print("v != 3:", v[v != 3])
print("v == 3:", v[v == 3])
print("v >= 3:", v[v >= 3])

print("\n" + "#" * 30 + "\n")

# Matematiksel İşlemler (Mathematical Operations)
v = np.array([1, 2, 3, 4, 5])

print("v - 1:", np.subtract(v, 1))
print("v + 1:", np.add(v, 1))
print("v'nin ortalaması:", np.mean(v))
print("v'nin toplamı:", np.sum(v))
print("v'nin minimum değeri:", np.min(v))
print("v'nin maksimum değeri:", np.max(v))
print("v'nin varyansı:", np.var(v))

# NumPy ile İki Bilinmeyenli Denklem Çözümü

# Denklem sistemi:
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

# Katsayı matrisi (a)
a = np.array([[5, 1], [1, 3]])

# Sonuçlar vektörü (b)
b = np.array([12, 10])

# Çözüm
solution = np.linalg.solve(a, b)
print("Çözüm (x0, x1):", solution)
