# # открываем файл длф записи байтов
# with open('bytes.txt', 'wb') as f:
#     str = 'Миру мирок'
#     f.write(str.encode('utf-8'))

#можно записать выше пример по другому:
with open('bytes.txt', 'w', encoding='utf-8') as f:
    str = 'Миру мирок'
    f.write(str)

# открываем файл в режиме чтения байтов
with open('bytes.txt', 'rb') as f:
    # читаем байты из файла
    result = f.read()
    print(result)  # b'\xd0\x9c\xd0\xb8\xd1\x80\xd1\x83 \xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xba'
    print(type(result))  # <class 'bytes'>
    # едекодируем строку
    result1 = result.decode("utf-8")  #
    print(result1)  # Миру мирок
    print(type(result1))  # <class 'str'>
