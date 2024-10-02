# Liste
liste = [1, 2, 3]
liste[1] = 5  # Liste değiştirilebilir
print(liste)  # Çıktı: [1, 5, 3]
liste.append(4)  # Listeye eleman ekler
liste.remove(2)  # Listeden eleman çıkarır

# Demet (Tuple)
demet = (1, 2, 3)
# demet[1] = 5  # Hata verir çünkü tuple değiştirilemez
print(demet.index(2))  # 2 sayısının indeksini bulur (Çıktı: 1)
print(demet.count(2))  # 2 sayısından kaç tane olduğunu bulur (Çıktı: 1)

# Set
my_set = {1, 2, 2, 3}
print(my_set)  # Set, tekrar eden elemanları tutmaz. Çıktı: {1, 2, 3}
my_set.add(4)  # Set'e yeni eleman ekler
my_set.remove(2)  # Set'ten eleman çıkarır
print(my_set)  # Çıktı: {1, 3, 4}

# Set operasyonları
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))        # Birleşim: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Kesişim: {3}
print(set1.difference(set2))    # Fark: {1, 2}

# Veri Tipi Dönüşümleri
x = int(3.5)  # 3
y = int("10")  # 10
x = float(7)  # 7.0
y = float("3.14")  # 3.14
x = str(100)  # "100"
y = str(3.14)  # "3.14"

# Liste, Tuple ve Set Dönüşümleri
x = list("abc")  # ['a', 'b', 'c']
y = list((1, 2, 3))  # [1, 2, 3]
x = tuple([1, 2, 3])  # (1, 2, 3)
x = set([1, 2, 3, 3])  # {1, 2, 3}

# Dictionary oluşturma
x = dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}

# Boolean Dönüşümleri
x = bool(1)  # True
y = bool(0)  # False

# String Uzunluğu
name = "Eren"
print(len(name))  # Çıktı: 4
