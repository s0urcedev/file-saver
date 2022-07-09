import sys
import os
import py7zr
import random
from password_generatror import get_password

if len(sys.argv) == 2:
    file_name: str = sys.argv[1]
else:
    file_name: str = input("Enter file/dir name: ")

dir_path: str = os.path.dirname(os.path.abspath(file_name)).replace("\\\\", "/")

keys: list = []
while True:
    print("1. Generate me key code, please")
    print("2. I already have key code")
    mode: str = input("Choose(1 or 2): ")
    if mode in ['1', '1.', '1)', 'one', 'One', 'ONE', 'first', 'First', 'FIRST', '1st']:
        keys = [random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 4),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9),
                random.randint(1, 9)]
        break
    elif mode in ['2', '2.', '2)', 'two', 'Two', 'TWO', 'second', 'Second', 'SECOND', '2nd']:
        key: str = input("Enter your code: ")
        if key[0] != '0' and key[1] != 'x':
            key = '0x' + key
        if len(str(int(key, 16))) == 12:
            for i in range(0, 12):
                keys.append(int(str(int(key, 16))[i]))
            break
        else:
            print("UNCORRECT CODE")
    else:
        print("UNCORRECT ENTER")

password_final: str = get_password(file_name, keys)

try:
    text_file = open(dir_path.replace('\\', '/') + '/' + 'KEY.cfg', "w")
    text_file.write(hex(int(str(keys[0])
                    + str(keys[1])
                    + str(keys[2])
                    + str(keys[3])
                    + str(keys[4])
                    + str(keys[5])
                    + str(keys[6])
                    + str(keys[7])
                    + str(keys[8])
                    + str(keys[9])
                    + str(keys[10])
                    + str(keys[11]))))
    text_file.close()
    try:
        archive = py7zr.SevenZipFile(dir_path.replace('\\', '/') + '/' + file_name.split('.')[0] + '_archive.7z', 'w', password=password_final)
        archive.writeall(dir_path.replace('\\', '/') + '/' + file_name, file_name)
        archive.close()
        print(f"Your code: "
                            + hex(int(str(keys[0])
                            + str(keys[1])
                            + str(keys[2])
                            + str(keys[3])
                            + str(keys[4])
                            + str(keys[5])
                            + str(keys[6])
                            + str(keys[7])
                            + str(keys[8])
                            + str(keys[9])
                            + str(keys[10])
                            + str(keys[11])))[2:])
        input("Press enter to exit...")
    except Exception:
        print("UNCORRECT FILE OR PATH")
        input("Press enter to exit...")
except Exception:
    print("UNCORRECT FILE OR PATH")
    input("Press enter to exit...")