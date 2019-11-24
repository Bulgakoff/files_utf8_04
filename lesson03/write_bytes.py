# открываем файл для записи бфйтов
with open('bytes.txt', 'wb') as f:
    # пишем сроку байт
  
    f.write(b'Hello bytes')
#     читаем как текст
with open('bytes.txt', 'r', encoding='ascii') as f:
    # печатаем сроку байт  врежиме чтения
    print(f.read())
    # тепрь запишем(write()) и выведем на печать то что читаем(read())теперь русский техт utf -8
with open('bytes.txt', 'wb') as f:
    str = 'Миру мир'
    f.write(str.encode('utf-8'))
with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())
