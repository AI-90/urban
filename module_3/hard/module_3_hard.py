data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_t = 0
def calculate_structure_sum(structure):
    global sum_t
    for element in structure:
        if isinstance(element,int):
           sum_t += element
        elif isinstance(element,str):
           sum_t += len(element)
        elif isinstance(element,dict):
            for key in element:
                if isinstance(key, int):
                    sum_t += key
                elif isinstance(key, str):
                    sum_t += len(key)
                else:
                    calculate_structure_sum(key)

                if isinstance(element[key], int):
                    sum_t += element[key]
                elif isinstance(element[key], str):
                    sum_t += len(element[key])
                else:
                    calculate_structure_sum(element[key])
        else:
            calculate_structure_sum(element)
    return  sum_t

result = calculate_structure_sum(data_structure)
print(result)
