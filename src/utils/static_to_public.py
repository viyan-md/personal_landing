from os import path
from os import listdir, mkdir, makedirs
from shutil import copy, rmtree

def create_clean_public():
    public_path = "public"

    if path.exists(public_path):
        rmtree(public_path)

    mkdir(public_path)

##main function
def copy_static_to_public():
    create_clean_public()

    public_path = "public"
    static_path = "static"

    def copy_folder_contents(src_folder, dst_folder):
        if not path.isdir(src_folder):
            raise ValueError(f"{src_folder} is not a valid directory.")
        
        if not path.exists(dst_folder):
            makedirs(dst_folder)

        for entry in listdir(src_folder):
            src_path = path.join(src_folder, entry)
            dst_path = path.join(dst_folder, entry)

            if path.isdir(src_path):
                copy_folder_contents(src_path, dst_path)  
            else:
                copy(src_path, dst_path)

    copy_folder_contents(static_path, public_path)
