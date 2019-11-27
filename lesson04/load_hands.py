# читаем объект из файла
# ткроем файл
with open('person.dat', 'rb') as f:
    #  a   теперь нам надо знать как мы записывали обхект
    # прочитаем файл в список
    result = f.readlines()
    print(result)  # ------>[b'Max\n', b'123\n', b'345\n']

# теперь воссоздаем исходный объект (пустой)
person = dict()
#   первый элемент это его имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телефоны
phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))
person['phone'] = phones
# получили  исходный объект ю это было тяжело ю но что если объект изменится,?
print(person)  # -------------->{'name': 'Max'}=======>{'name': 'Max', 'phone': ['123', '345']}
