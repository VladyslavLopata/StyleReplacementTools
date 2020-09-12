import glob
import os


def prompt_range(expected_low: int, expected_max: int):
    """Ask prompt, assert expected values and return selected value"""

    assert expected_max - expected_low > 1, "Неправильное значение expected_low либо expected_max"

    error_message = f'Некорректный ввод. Введите число от {expected_low + 1} до {expected_max}.'
    prompt_message = 'Введите номер выбранного элемента.'

    while True:
        try:
            answer = int(input(prompt_message).replace(r'\D', '')) - 1
        except ValueError:
            print(error_message)
            answer = expected_low - 1
        if answer in range(expected_low, expected_max):
            break
        else:
            print(error_message)

    return answer


def select_element(selection_list: list, selection_prompt: str):
    """Ask prompt, return index of a selected file"""

    assert selection_list, "List is empty"

    idx = 0

    if len(selection_list) > 1:
        print(selection_prompt)

        for i, style in enumerate(selection_list):
            print(f'{i + 1}. {os.path.splitext(style)[0]}')

        idx = prompt_range(0, len(selection_list))

    return idx


def select_styles():
    """Select stylesheet in stylesheets folder"""

    stylesheets_filepath = os.path.expanduser(r'~\AppData\Roaming\Aegisub\catalog')  # путь к стилям

    stylesheets = os.listdir(stylesheets_filepath)  # список всех наборов стилей

    stylesheet_index = select_element(stylesheets, 'Выберите набор стилей')

    # Считывание файла стилей. encoding='utf-8-sig' потому что aegisub использует utf-8 с bom
    with open(os.path.join(stylesheets_filepath, stylesheets[stylesheet_index]),
              encoding='utf-8-sig') as styles_file:
        styles = styles_file.readlines()

    return styles


def select_ass_file():
    """Select .ass file from working directory"""

    ass_files_list = glob.glob('*.ass')  # собираем список всех .ass файлов в директории

    # выбираем нужный, если это необходимо.
    ass_file_index = select_element(ass_files_list, 'Выберите файл субтитров')

    return ass_files_list[ass_file_index]


if __name__ == '__main__':
    select_styles()
    select_ass_file()
