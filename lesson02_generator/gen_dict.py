pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(type(pairs))
pair_dict_result = dict()

for pair in pairs:
    key = pair[0]
    value = pair[1]
    pair_dict_result[key] = value
print(pair_dict_result)
print(type(pair_dict_result))

pair_dict_result = {pair[0]: pair[1] for pair in pairs}
print(f'генератор --->{pair_dict_result}')


