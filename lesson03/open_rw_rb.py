
# открываем файл для записи бфйтов
with open('bytes.txt', 'wb') as f:
    pass
with open('bytes.txt', 'rb') as f:
    pass
# мы отрываем файл  в текстовом режиме с указанием кодировки
with open('bytes.txt', 'r', encoding='utf-8') as f:
    pass