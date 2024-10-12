# Koşullar (Conditions)

# if örnekleri
if 1 == 1:
    print("Something")

if 1 == 2:
    print("Something")  # Bu blok çalışmaz çünkü koşul False

number = 11
if number == 10:
    print("number is 10")

# if-else örneği
def number_check(number):
    if number == 12:
        print("number is 12")
    else:
        print("number is not 12")

number_check(10)

# elif örneği
def number_check2(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check2(6)

print("\n" + "#" * 30 + "\n")

# Döngüler (Loops)

# for döngüsü örneği
students = ["John", "Mark", "Venessa", "Marian"]
for student in students:
    print(student + " " + student.upper())

print("\n" + "#" * 30 + "\n")

# Maaşlara zam uygulaması
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(salary, rate):
    return salary * rate / 100 + salary

# Maaşlara %20 zam
for salary in salaries:
    print(int(new_salary(salary, 20)))

print("\n" + "#" * 30 + "\n")

# Alternating string örneği
def alternating(string):
    new_string = ""
    for index in range(len(string)):
        if index % 2 == 0:
            new_string += string[index].upper()
        else:
            new_string += string[index].lower()
    print(new_string)

alternating("Eren")

print("\n" + "#" * 30 + "\n")

# break & continue & while örnekleri

# break örneği
for salary in salaries:
    if salary == 3000:
        break
    print(salary)

print("\n" + "#" * 30 + "\n")

# while döngüsü örneği
number = 1
while number < 5:
    print(number)
    number += 1

print("\n" + "#" * 30 + "\n")

# Enumerate örneği: Otomatik Counter/Indexer ile for döngüsü
students = ["John", "Mark", "Venessa", "Mariam"]
A, B = [], []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print("Çift indexli öğrenciler:", A)
print("Tek indexli öğrenciler:", B)

print("\n" + "#" * 30 + "\n")

# Mülakat Sorusu: divide_students fonksiyonu
def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print("Çift indexli grup:", groups[0])
    print("Tek indexli grup:", groups[1])
    return groups

st = divide_students(["Ali", "Veli", "Ayşe", "Fatma"])

print("\n" + "#" * 30 + "\n")

# alternating fonksiyonunun enumerate ile yazılması
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is Eren and I am learning python")

print("\n" + "#" * 30 + "\n")

# Zip örneği: Listeleri birleştirme
students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

# Üç listeyi zip ile birleştirme
print(list(zip(students, departments, ages)))

print("\n" + "#" * 30 + "\n")

# Lambda, Map, Filter, Reduce örneği

# Lambda fonksiyonu
new_sum = lambda a, b: a + b
print(new_sum(1, 3) * 9)


# map
salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

print(list(map(lambda x: x * 20 / 100 + x,salaries)))

print(list(map(lambda x: x ** 2 ,salaries)))


# FILTER

list_store = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, list_store)))


# REDUCE
from functools import reduce
list_store = [1,2,3,4]
reduce(lambda a,b: a+b, list_store)
