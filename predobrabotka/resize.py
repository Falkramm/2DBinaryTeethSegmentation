from PIL import Image
import os


def resize_images(directory, output_directory, size):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    filenames = sorted(os.listdir(directory))
    for filename in filenames:
        if filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)

            image = Image.open(image_path)
            resized_image = image.resize(size)
            resized_image.save(output_path)


# Пример использования
data_dir = "data"
images_dir = "images"
output_dir = "data_256/images"
resize_size = (256, 256)

images_directory = os.path.join(data_dir, images_dir)
output_directory = os.path.join(data_dir, output_dir)

resize_images(images_directory, output_directory, resize_size)