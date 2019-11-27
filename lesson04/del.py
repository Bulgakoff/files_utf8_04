f_var = 'hello'
with open('del.txt', 'wb') as f:
    f.write(f'{f_var}'.encode('utf-8'))
print('file created del.txt')
