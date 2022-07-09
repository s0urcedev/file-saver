from io import TextIOWrapper
import sys
import os
import py7zr
import shutil
from password_generatror import get_password

if len(sys.argv) == 2:
    file_name: str = sys.argv[1]
else:
    file_name: str = input("Enter file/dir name: ")

dir_path: str = os.path.dirname(os.path.abspath(file_name)).replace("\\\\", "/")

is_cfg_file: bool = False

try:
    try:
        text_file: TextIOWrapper= open(dir_path.replace('\\', '/') + '/' + 'KEY.cfg', "r")
        is_cfg_file = True
        key: str = str(int(text_file.read(), 16))
        text_file.close()
    except:
        key: str = input("Enter keys: ")
        if key[0]!='0' and key[1]!='x':
            key = '0x'+key
        key = str(int(key, 16))
    
    keys: list = [int(key[0]),
                  int(key[1]),
                  int(key[2]),
                  int(key[3]),
                  int(key[4]),
                  int(key[5]),
                  int(key[6]),
                  int(key[7]),
                  int(key[8]),
                  int(key[9]),
                  int(key[10]),
                  int(key[11])]

    password_final: str = get_password(file_name, keys)

    try:
        archive: py7zr.SevenZipFile = py7zr.SevenZipFile(dir_path.replace('\\', '/') + '/' + file_name.split('.')[0] + '_archive.7z', 'r', password=password_final)
        try:
            archive.extractall(dir_path.replace('\\', '/') + '/' + file_name.split('.')[0])
            archive.close()
            os.remove(dir_path.replace('\\', '/') + '/' + file_name.split('.')[0] + '_archive.7z')
            if is_cfg_file == True:
                os.remove(dir_path.replace('\\', '/') + '/KEY.cfg')
            print('FINISHED, ALL IS CORRECT')
            input("Press enter to exit...")
        except Exception:
            print("UNCORRECT OPTIONS")
            shutil.rmtree(dir_path.replace('\\', '/') + '/' + file_name.split('.')[0], ignore_errors=True)
            input("Press enter to exit...")
    except Exception:
        print("UNCORRECT FILE OR PATH")
        input("Press enter to exit...")
except Exception:
    print("UNCORRECT FILE OR PATH")
    input("Press enter to exit...")