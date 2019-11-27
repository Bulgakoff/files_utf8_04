import random

# создать список случайных чисел от 1 до 100
result = [random.randint(1, 20) for i in range(10)]

print(result)

# создать список квадратов чисел
my_list = [2, 2, 3, -5]
result = [n ** 2 for n in my_list]
print(result)



# создать список имен на букву А
names = ['Вся', 'Дфша', 'Алексец', 'Анна', 'таня', 'Лиза']
result = [name for name in names if name.startswith('А')]
print(result)