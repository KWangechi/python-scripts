import os
import shutil
import sys
import tkinter as tk
import builtins
import time
from tkinter import filedialog


root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", root.quit)
root.withdraw();


start_time = time.time();

def open_dialog():
    source_folder = filedialog.askdirectory()
# create an elapsed time for the folder selection
    # elapsed_time = time.time() - start_time

    return source_folder

source_folder = None


while(source_folder is None):
    source_folder  = open_dialog();
    # print(source_folder)
    
    if(source_folder != ''):
        source_folder += '/'
        # print(source_folder)
        # source_folder = open_dialog() + '/'
        print(source_folder)
        # continue

    else:
        # root.mainloop()
        # root.quit()

        break
        # time.sleep(4)
        print('No file has been selected!!')
        # builtins.quit("Operation was cancelled, please select a file")


    # # rename the files that have already been copied
    # def rename_files(file_name, new_file_name):
    #     print('This will rename the files incase a copy is already there')


    # # function for extracting the file from the file system
    def copy_files(source_dir, destination_dir):
        shutil.copytree(source_dir, destination_dir)

        print('Directory' + destination_dir + 'has been copied successfully')

        # iterate in the new folder and rename the files
        for filename in os.listdir(destination_dir):
            if os.path.isfile(os.path.join(destination_dir, filename)):

                file_path = os.path.join(destination_dir, filename)
                print(file_path)

                # get the new filename
                file_name, file_ext = os.path.splitext(os.path.basename(file_path))

                # print(file_ext)
                new_file_name = file_name  + '(' + str(i+1) + ')' + file_ext

                # get the new file path
                new_file_path = os.path.join(destination_dir,
                                            new_file_name)
                # print(new_file_path)

                # rename the file
                os.rename(file_path, new_file_path)
                print('New File ' + new_file_name + 'has been successfully created!!');



    # # whatever is below this should just be in a function
    number_of_copies = int(input("Enter the number of copies you want...: "))

    # # create a function that changes the name of the folder and the files
    for i in range(number_of_copies):
        source_folder_path = os.path.dirname(
            source_folder
        )

        new_destination_dir_path = f"{source_folder_path}({i+1})"
        # print(new_destination_folder_path)

        # check if the destination directory exists
        if (os.path.exists(new_destination_dir_path)):
            print('Folder already exists. Program exit!!');
            continue

            copy_files(source_folder, new_destination_dir_path)
            
        else:
            copy_files(source_folder, new_destination_dir_path)
