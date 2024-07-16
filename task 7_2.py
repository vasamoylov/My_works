import io
def custom_write(file_name, strings):
    strings_positions = {}
    count = 0
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        n = file.tell()
        file.write(str(i))
        file.write('\n')
        file.close()
        count += 1
        key = (count, n)
        strings_positions[key] = i
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


