import os
from pathlib import Path

def get_size(path: str) -> int:
    """Возвращает размер файла или директории."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for entry in os.scandir(path):
            total_size += get_size(entry.path)
        return total_size

def main():
    current_directory = Path('.')
    
    # Получение списка всех поддиректорий и файлов в текущей директории
    all_items = list(current_directory.glob('**'))
    
    # Инициализация пустого списка для хранения размеров элементов
    sizes = []
    
    # Проход по каждому элементу и получение его размера
    for item in all_items:
        size = get_size(item)
        sizes.append((item, size))
        
    # Сортировка по убыванию размера
    sorted_sizes = sorted(sizes, key=lambda x: x[1], reverse=True)
    
    # Вывод результата в терминал
    for item, size in sorted_sizes:
        print(f"{item}: {size} bytes")

if __name__ == "__main__":
    main()
