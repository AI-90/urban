
from time import sleep
def wite_words(word_count, file_name):
    with open(file_name, "a") as file:
        for number in range(word_count):
            number += 1
            file.write(f"Какое-то слово № {number}")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(10, 'example4.txt')