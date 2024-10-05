# Fonksiyon Tanımlama

def calculate(x):
    """Verilen sayının karesini hesaplar."""
    print(x ** 2)

# Fonksiyonu çağır
calculate(5)


print()


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.
def summer(arg1, arg2):
    """İki sayının toplamını hesaplar."""
    print(arg1 + arg2)


# Fonksiyonu farklı argümanlarla çağır
summer(3, 5)
print()
summer(arg2=30, arg1=24)
print()


# Docstring ile fonksiyon tanımı
def summer2(arg1, arg2):
    """
    İki sayının toplamını döner.

    Parametreler
    ----------
    arg1: int, float  # İlk parametre: tam sayı veya ondalıklı sayı
    arg2: int, float  # İkinci parametre: tam sayı veya ondalıklı sayı

    Dönüş
    -------
    int, float  # Toplam sonucu: tam sayı veya ondalıklı sayı
    """
    print(arg1 + arg2)


# Fonksiyonu çağır
summer2(3, 47)
print()


# Fonksiyonların Statement/Body Bölümü

def say_hi():
    """Selamlaşma mesajlarını yazdırır."""
    print("Merhaba")
    print("Hi")
    print("Hello")


# Fonksiyonu çağır
say_hi()
print()


def say_hi2(string):
    """Verilen bir string ile birlikte mesajları yazdırır."""
    print(string)
    print("Eren")
    print("KIRMIZI")


# Fonksiyonu çağır
say_hi2("Merhaba")
print()


def multiplication(a, b):
    """İki sayının çarpımını hesaplar."""
    c = a * b
    print(c)


# Fonksiyonu çağır
multiplication(10, 9)
print()

# Girilen değerleri bir liste içinde saklayacak fonksiyon.
list_store = []


def add_element(a, b):
    """İki sayının çarpımını hesaplayarak listeye ekler."""
    c = a * b
    list_store.append(c)


# Fonksiyonu çağır
add_element(1, 9)
add_element(8, 2)
add_element(7, 5)

# Listeyi yazdır
print(list_store)
print()


# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)

def divide(a, b=2):
    """Verilen sayıyı 2'ye böler. Eğer b verilmezse varsayılan değeri 2 olur."""
    print(a / b)


# Fonksiyonu çağır
divide(1)
print()


def calculate(varm, moisture, charge):
    """Verilen değerleri kullanarak bir hesaplama yapar."""
    print((varm + moisture) / charge)


# Fonksiyonu çağır
calculate(98, 12, 78)

# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge

calculate(98,24, 65) * 10

print()

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

varm_result, moisture_result, charge_result, output_result = calculate(98, 24, 65)

print("varm:", varm_result)
print("moisture:", moisture_result)
print("charge:", charge_result)
print("output:", output_result)


print()

# sonucu int yapmak istersek

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

print(calculate(90,12,12) * 10)
print()

# Fonksiyon İçerisinden Fonksiyon Çağırmak

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


def standardization(a, p):
    return (a * 10 / 100) * (p * p)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    return b * 10

print(all_calculation(2, 4, 6, 10))  # Burada return edilen değeri yazdırıyoruz

print()

# Lokal & Global Değişkenler (Local & Global Variables)

list_store = [1,2] # Global

def add_element(a,b):
    c = a * b   # Local
    list_store.append(c)
    print(list_store)

add_element(1,9)
