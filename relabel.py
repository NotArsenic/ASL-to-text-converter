import os
import shutil


def copy_files_with_new_names(folder_path, destination_folder):

    files = os.listdir(folder_path)
    files.sort()


    os.makedirs(destination_folder, exist_ok=True)


    count = 0
    for file_name in files:

        _, file_extension = os.path.splitext(file_name)


        new_file_name = f"{count}{file_extension}"


        shutil.copy2(os.path.join(folder_path, file_name), os.path.join(destination_folder, new_file_name))

        count += 1



source_folder = r"C:\Users\Chaitanya\PycharmProjects\SignRecog_asl1\data\unnamed data\A"
destination_folder = r"C:\Users\Chaitanya\PycharmProjects\SignRecog_asl1\data\dest\A"
copy_files_with_new_names(source_folder, destination_folder)
