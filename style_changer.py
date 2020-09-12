import glob
import os

import ass


def select_styles():
    stylesheets_filepath = os.path.join(os.path.expanduser('~'), r'AppData\Roaming\Aegisub\catalog')  # путь к стилям

    stylesheets = os.listdir(stylesheets_filepath)  # список всех наборов стилей

    print('Выберите набор стилей, который хотите использовать для замены')

    # печать всех наборов по номерам, чтобы проще было выбирать
    for i, style in enumerate(stylesheets):
        print(f'{i + 1}. {os.path.splitext(style)[0]}')

    stylesheet_index = int(input('Введите номер выбранного набора: ').replace(r'\D', '')) - 1

    # Считывание файла стилей. encoding='utf-8-sig' потому что aegisub использует utf-8 с bom
    with open(os.path.join(stylesheets_filepath, stylesheets[stylesheet_index]), 'r',
              encoding='utf-8-sig') as styles_file:
        styles = list(style.strip() for style in styles_file.readlines())

    print('\n\nДоступные стили в наборе:\n')
    print(*styles, sep='\n')

    return styles


'''
Блок работы с текущей директорией.
'''


def select_file():
    ass_files_list = glob.glob('*.ass')  # собираем список всех .ass файлов в директории

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

    return parsed_ass_document
