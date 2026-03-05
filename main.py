import random
import sys
import time
from typing import Dict, Tuple


STOP_WORD = 'СТОП'


def load_words(filename: str = 'words.txt') -> Dict[str, str]:
    '''
    Загружает пары слов из текстового файла и формирует словарь переводов.
    Ключ — исходное слово, значение — его перевод.
    При ошибке чтения или неверном пути завершает программу через sys.exit(1).
    '''
    # Базовая защита от уязвимости Path Traversal (обход директорий).
    # Запрещаем переход на уровень выше через '..' в пути.
    # Запрещаем абсолютные пути, если ожидается относительный путь.
    if '..' in filename or filename.startswith('/'):
        print('Error: Invalid file path')
        sys.exit(1)

    try:
        # Используем контекстный менеджер для гарантированного закрытия файла.
        # Это освобождает ресурсы даже при возникновении ошибок внутри блока.
        with open(filename, 'r', encoding='utf-8') as file:
            # Словарь для хранения пар слов и их переводов.
            word_to_translation: Dict[str, str] = {}

            # Последовательно читаем каждую строку файла.
            for line in file:
                # Удаляем пробельные символы в начале и в конце строки.
                line_content = line.strip()

                # Пропускаем пустые строки для избежания ошибок обработки.
                if not line_content:
                    continue

                # Игнорируем строки без запятой или с несколькими запятыми.
                # Формат должен быть строго 'слово,перевод' (одна запятая).
                if line_content.count(',') != 1:
                    continue

                # Разделяем строку на две части по первой запятой.
                # Перая часть - исходное слово, вторая - перевод.
                key, value = line_content.split(',', 1)
                # Сохраняем пару в словарь с очисткой от лишних пробелов.
                word_to_translation[key.strip()] = value.strip()

            # Возвращаем сформированный словарь пар слов и переводов.
            return word_to_translation

    except FileNotFoundError:
        # Обрабатываем случай, когда файл не найден в указанном пути.
        print(f'Error: File "{filename}" not found.')
        sys.exit(1)


def print_statistics(score, total_time):
    ...


def ask_and_check(word, correct):
    ...


def start_game(words):
    ...


def train_until_mistake(words):
    ...


def add_words(words):
    ...


def show_all_words(words):
    ...


def save_words(words, filename):
    ...


def main():
    while True:
        menu = '''Меню:
        1. Начать игру
        2. Добавить слова
        3. Тренировка до первой ошибки
        4. Вывод всех слов
        5. Выход
        '''
        print(menu)
        menu_choice = input('Пункт меню: ')


if __name__ == '__main__':
    main()
