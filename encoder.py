import os
import numpy as np
from PIL import Image


class Encoder_NN():

    def __init__(self) -> None:
        pass

    def png_to_npArray_grayscale(self, dir_source, dir_to_save, name_of_file=''):

        if os.path.exists(f"{dir_to_save}/{name_of_file}.npy"):
            print("El archivo ya existe")
            return

        main_folder = dir_source

        list_files_png = os.listdir(dir_source)

        file = np.array([], dtype=np.uint8)

        flag = True

        i = 0

        for png in list_files_png:

            current_png = f"{main_folder}/{png}"

            image = Image.open(current_png)

            image_gray = image.convert('L')

            pixel_data = 255 - np.array(image_gray, dtype=np.uint8)

            row_col_pixel_structure = pixel_data.reshape((1, 128, 128))

            if flag:
                file = row_col_pixel_structure
                flag = False
                continue

            file = np.concatenate((file, row_col_pixel_structure), axis=0)

            if i % 500 == 0:
                os.system('cls')
                print(f"{round(100*i/(len(list_files_png)), 1)}%")

            i += 1

        np.save(f"{dir_to_save}/{name_of_file}", file)


if __name__ == '__main__':
    encoder = Encoder_NN()
    #encoder.png_to_npArray_grayscale("./res/dataset", "./res", 'data_set')
    encoder.png_to_npArray_grayscale("./res/testset", "./res", 'test_set')