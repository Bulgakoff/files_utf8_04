
with open('del.txt', 'rb') as f:
    result = f.readlines()
    print(result)
f_var = []
for p in result[:]:
    f_var.append(p.decode('utf-8'))
print(f_var)