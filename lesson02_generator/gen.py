# запись только отрицательных чисел
num = [1, 2, 3, 4, 5, -4, 93, -3]

# классика :
result = []
for number in num:
    if number < 0:
        result.append(number)
print(result)

# а это генератор:
numbers = [number for number in num if number < 0]  # ------> а это генератор
print(result)
 
#  через filter:
result = list(filter(lambda number : number < 0, num))  # <par1 (number: number < 0)- простая функция >,
# <par2 -(num) иттерируемый список >на входе number на выходе (return) number < 0
print(result)
