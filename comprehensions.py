# COMPREHENSIONS

salaries = [1000, 2000, 3000, 4000, 5000]

# Yeni maaş hesaplama fonksiyonu
def new_salary(x):
    return x * 20 / 100 + x

# Listeyi oluşturma - for döngüsü ile
null_list = []
for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))
print(null_list)

# Aynı işlemi List Comprehension ile
print([new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries])

# List Comprehension örnekleri
print([salary * 2 for salary in salaries])
print([salary * 2 for salary in salaries if salary < 3000])
print([salary * 2 if salary < 3000 else salary * 20 for salary in salaries])

# Öğrencilerin isimlerini düzenleme
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]
print([student.lower() if student in students_no else student.upper() for student in students])

print("\n" + "#" * 30 + "\n")

# Dict Comprehension

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sözlük işlemleri
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# Dict Comprehension örnekleri
print({k: v ** 2 for (k, v) in dictionary.items()})
print({k.upper(): v for (k, v) in dictionary.items()})
print({k.upper(): v ** 2 for (k, v) in dictionary.items()})

print("\n" + "#" * 30 + "\n")

# Uygulama - Mülakat Sorusu
# Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmesi
numbers = range(10)
new_dict = {n: n ** 2 for n in numbers if n % 2 == 0}
print(new_dict)

print("\n" + "#" * 30 + "\n")

# List & Dict Comprehension Uygulamaları

# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
import seaborn as sns
df = sns.load_dataset("car_crashes")

# Değişken isimlerini büyük harfe çevirmek
df.columns = [col.upper() for col in df.columns]
print(df.columns)

print("\n" + "#" * 30 + "\n")

# İsminde "INS" olan değişkenlerin başına FLAG, diğerlerine NO_FLAG eklemek
print(["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns])

print("\n" + "#" * 30 + "\n")

# Amaç: key'i string, value'su liste olan bir sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.
# Output: {'total': ['mean', 'min', 'max', 'sum'], ...}
num_cols = [col for col in df.columns if df[col].dtype != "O"]
agg_list = ["mean", "min", "max", "sum"]

# Dict Comprehension ile sözlük oluşturma
new_dict = {col: agg_list for col in num_cols}
print(new_dict)

# Bu sözlüğü kullanarak veri setine aggregate işlemleri uygulamak
print(df[num_cols].agg(new_dict))
