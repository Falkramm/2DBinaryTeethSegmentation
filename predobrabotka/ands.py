import os
from PIL import Image

from PIL import Image
import os

def apply_mask_to_images(image_dir, mask_path, output_dir):
    # Загрузка маски
    mask = Image.open(mask_path)
    mask = mask.convert('1')

    # Создание директории для сохранения результатов
    os.makedirs(output_dir, exist_ok=True)

    # Обработка каждого изображения в директории
    for filename in os.listdir(image_dir):
        print(filename)
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Загрузка и преобразование изображения в черно-белый формат
            image_path = os.path.join(image_dir, filename)
            image = Image.open(image_path)
            image = image.convert('L')

            # Применение маски к изображению
            result = Image.new('RGB', image.size)
            pixels_result = result.load()
            pixels_image = image.load()
            pixels_mask = mask.load()

            for i in range(result.size[0]):
                for j in range(result.size[1]):
                    if pixels_mask[i, j] == 255:
                        pixels_result[i, j] = (pixels_image[i, j], pixels_image[i, j], pixels_image[i, j])
                    else:
                        pixels_result[i, j] = (0, 0, 0)  # Черный цвет

            # Сохранение результата
            output_path = os.path.join(output_dir, filename)
            result.save(output_path)

# Пример использования
image_dir = 'data_256/images_gist'
mask_path = 'mask_256.png'
output_dir = 'image_cut/'

apply_mask_to_images(image_dir, mask_path, output_dir)
