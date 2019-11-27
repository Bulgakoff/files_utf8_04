person = dict(name='Max', phones=[123, 345])
# откроем файл
with open('person.dat', 'wb') as f:
    #     запишем объект в файл построчно
    # сначала возмем имя
    name = person['name']
# добавим перенос строки переведем в бацты и запишем
    f.write(f'{name}\n'.encode('utf-8'))
# олучим телефоны
    phones = person['phones']
# запишем номер
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')