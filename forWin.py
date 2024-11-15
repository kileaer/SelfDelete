# Для использования нужны права администратора!
import os
import shutil
import random

def overwrite_file(file_path, passes=3):
    """Перезаписывает файл несколько раз случайными данными."""
    file_size = os.path.getsize(file_path)
    with open(file_path, 'ba+') as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(file_size))
            f.flush()
            os.fsync(f.fileno())
    os.remove(file_path)

def overwrite_directory(directory_path, passes=3):
    """Перезаписывает все файлы в директории несколько раз случайными данными."""
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            overwrite_file(file_path, passes)
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)
    os.rmdir(directory_path)

def overwrite_disk(disk_path, passes=3):
    """Перезаписывает весь диск несколько раз случайными данными."""
    if not os.path.exists(disk_path):
        print(f"Путь {disk_path} не существует.")
        return

    if os.path.isfile(disk_path):
        overwrite_file(disk_path, passes)
    elif os.path.isdir(disk_path):
        overwrite_directory(disk_path, passes)
    else:
        print(f"Путь {disk_path} не является файлом или директорией.")

def main():
    print("Внимание! Эта программа полностью очистит указанный диск или раздел без возможности восстановления данных.")
    disk_path = input("Введите путь к диску или разделу, который нужно очистить (например, C:\\): ").strip()
    confirm = input("Вы уверены, что хотите очистить этот диск или раздел? (да/нет): ").strip().lower()
    
    if confirm == 'да':
        overwrite_disk(disk_path)
        print("Очистка завершена.")
    else:
        print("Очистка отменена.")

if __name__ == "__main__":
    main()
