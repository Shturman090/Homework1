def calculate_structure_sum(data_):
    _sum = 0
    if isinstance(data_, int):
        _sum += data_
    elif isinstance(data_, str):
        _sum += len(data_)
    elif isinstance(data_, (list, tuple, set)):
        for item in data_:
            _sum += calculate_structure_sum(item)
    elif isinstance(data_, dict):
        for key, value in data_.items():
            _sum += calculate_structure_sum(key)
            _sum += calculate_structure_sum(value)

    return _sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)