# ./scripts/remove_pycache.py

import os
import shutil

def remove_pycache(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == "__pycache__":
                dir_path = os.path.join(root, dir)
                print("Removendo diretório:", dir_path)
                shutil.rmtree(dir_path)
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                print("Removendo arquivo:", file_path)
                os.remove(file_path)

if __name__ == "__main__":
    src_directory = "src"
    remove_pycache(src_directory)
