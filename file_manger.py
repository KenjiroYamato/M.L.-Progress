import os
import shutil
import math
import random
import numpy as np


class File_Maneger():

    def __init__(self, dir):
        self.source = dir

    def dataset_testset_selector(self, ratio, dir_data, dir_test):
        """@param ratio: que porcentaje de los archivos de cada carpeta va a ir para el dataset
        @param dir_data: la direccion de la carpeta donde van a ir los archivos del data set
        @param dir_test: la direccion de la carpeta donde van a ir los archivos del test set
        
        dada la carpeta padre, se suponen que: todos los archivos de las carpetas hijos son necesarias para el data set y el data test
        ademas toma la misma cantidad de archivos de cada carpeta para las carpetas del data set y data test
        """
        list_folders_sons = os.listdir(self.source)
        n_files_by_folder = self.same_num_of_files_in_N_folders()

        n_files_dataset = round(n_files_by_folder * ratio)
        n_files_testset = n_files_by_folder - n_files_dataset
        i_file = 0
        i_n_folder = 0

        if (len(os.listdir(dir_data)) + len(os.listdir(dir_test)) > 0):
            print('los archivos ya estan cargados o hay archivos en la carpeta destino')
            return

        for current_name in list_folders_sons:  #itera en cada carperpeta hija
            current_folder = f"{self.source}/{current_name}"

            files_to_copy_dataset = os.listdir(current_folder)[:n_files_dataset]
            files_to_copy_testset = os.listdir(current_folder)[n_files_dataset:]

            todo_bien = len(files_to_copy_dataset) + len(files_to_copy_testset) == n_files_by_folder

            if not todo_bien:
                print('inesperado.')
                return

            print(f"copying Dataset from {current_folder}")
            for file in files_to_copy_dataset:
                shutil.copy(f"{current_folder}/{file}", dir_data)
                os.rename(f"{dir_data}/{file}", f"{dir_data}/{i_n_folder}_{i_file}.png")
                i_file += 1
            print("Copied", end='\n')

            print(f"copying Testset from {current_folder}")
            for file in files_to_copy_testset:
                shutil.copy(f"{current_folder}/{file}", dir_test)
                os.rename(f"{dir_test}/{file}", f"{dir_test}/{i_n_folder}_{i_file}.png")
                i_file += 1
            print("Copied", end='\n')
            i_n_folder += 1

            print('Perfecto' if len(os.listdir(dir_data)) +
                  len(os.listdir(dir_test)) == i_file else 'Error numero de archivos')

    def same_num_of_files_in_N_folders(self):
        """Dada una direccion (carpeta padre), todos las carpetas dentro de la carpeta padre se les obligara
          a tener el mismo numero (ese munero es igual a la carpeta con menor numero de archivos) de archivos dentro de cada una de ellas.
          elimina los archivos basado en un criterio de aleatoriedad
          @return: el numero de archivos en cada una de las carpetas hijo"""
        n_min = math.inf
        len_each_folder = []
        are_all_same = False

        folder_main = os.listdir(self.source)

        for current_name in folder_main:
            current_folder = f"{self.source}/{current_name}/"
            len_current_folder = self.len_File(current_folder)
            len_each_folder += [len_current_folder]
            if len_current_folder < n_min:
                n_min = len_current_folder

        are_all_same = np.all(n_min == len_each_folder)

        print(n_min, are_all_same, len_each_folder)

        if not are_all_same:
            len_each_folder = []
            for current_name in folder_main:
                current_folder = f"{self.source}/{current_name}/"
                len_current_folder = self.len_File(current_folder)
                while len_current_folder > n_min:
                    files = os.listdir(current_folder)
                    os.remove(f"{current_folder}{random.choice(files)}")
                    len_current_folder = self.len_File(current_folder)
                len_each_folder += [len_current_folder]
        else:
            print("OK, La cantidad de archivos en cada carpeta es la misma")

        print(n_min, are_all_same, len_each_folder)

        return n_min

    def len_File(self, dir=''):
        return len(os.listdir(self.source)) if dir == '' else len(os.listdir(dir))


if __name__ == "__main__":
    fm = File_Maneger("./res/trainingData")
    fm.dataset_testset_selector(0.85, "./res/dataset", "./res/testset")
