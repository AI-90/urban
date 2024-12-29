def custom_write(file_name, strings:list):
    strings_positions = {}
    number_string=1
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        key = (number_string,file.tell())
        strings_positions[key]=string
        file.write(string+'\n')
        number_string += 1
    file.close()
    return  strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)