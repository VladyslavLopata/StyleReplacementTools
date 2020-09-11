import glob
import os

import ass

'''
Блок работы со стилями аэгисаба.
В этом блоке выбираем файл стилей, перечисляем стили и костыляем костыли.
'''

# путь к стилям
stylesheets_filepath = os.path.join(os.path.expanduser('~'), r'AppData\Roaming\Aegisub\catalog')

# список всех наборов стилей
stylesheets = os.listdir(stylesheets_filepath)

print('Выберите набор стилей, который хотите использовать для замены')
# печать всех наборов по номерам, чтобы проще было выбирать
for i, style in enumerate(stylesheets):
    print('{}. {}'.format(i + 1, os.path.splitext(style)[0]))

# считывание ввода и конвертация ввода в реальный индекс в массиве
stylesheet_index = int(input('Введите номер выбранного набора: ')) - 1

# считывание файла стилей. encoding='utf-8' потому что aegisub внезапно использует utf-8 с bom
# и при стандартном чтении питон охуевает от происходящего и вставляет какую-то залупу в текст
with open(os.path.join(stylesheets_filepath, stylesheets[stylesheet_index]), 'r', encoding='utf-8-sig') as styles_file:
    styles = list(style.strip() for style in styles_file.readlines())

print('\n\nДоступные стили в наборе:\n')
for style in styles:
    print(style)

'''
Блок работы с текущей директорией.
Здесь выбираем файл, куда нужно — прости господи — вставить и изменить.
'''
# собираем список всех .ass файлов в директории
ass_files_list = glob.glob('*.ass')

# выбираем нужный, если это необходимо.
ass_file_index = 0
if len(ass_files_list) > 1:
    '''
    TODO:
    — добавить выбор
    — добавить сортировку по дате модификации
    '''
    pass

with open(ass_files_list[ass_file_index], encoding='utf_8_sig') as ass_file:
    parsed_ass_document = ass.parse(ass_file)

print('\n\n\n\n')
print(parsed_ass_document.styles)
parsed_ass_document.styles.add_line(type_name='Style', raw_line=styles[0])
print(parsed_ass_document.styles)
