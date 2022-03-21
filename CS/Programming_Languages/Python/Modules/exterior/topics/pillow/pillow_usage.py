"""Основные возможности библиотеки Python Imaging Library / Pillow / PIL
https://pythonru.com/biblioteki/osnovnye-vozmozhnosti-biblioteki-python-imaging-library-pillow-pil
"""

from PIL import Image

# Создание миниатюр

filename = "Beeline_logo.jpg"

size_1 = (32, 32)
size_2 = (16, 16)

try:
    img = Image.open(filename)
    print("Размер изображения:")
    print(img.format, img.size, img.mode)

    for size in [size_1, size_2]:
        match size:
            case (32, 32):
                saved = "Beeline_logo_32x32.jpg"
            case _:
                saved = "Beeline_logo_16x16.jpg"
        img.thumbnail(size)
        img.save(saved)
        img.show()
except FileNotFoundError:
    print("Файл не найден")
