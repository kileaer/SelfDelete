"""Пример запуска:
sudo python3 forLinux.py"""
# Тебе пригодится права суперпользователя sudo
import os
import subprocess

def shred_disk(disk_path, passes=3, remove=False):
    """Перезаписывает диск или раздел несколькими разами случайными данными."""
    if not os.path.exists(disk_path):
        print(f"Путь {disk_path} не существует.")
        return

    if not os.path.isblock(disk_path):
        print(f"Путь {disk_path} не является блочным устройством.")
        return

    try:
        print(f"Начинаем перезапись {disk_path} {passes} раз(а)...")
        subprocess.run(['shred', '-v', '-n', str(passes), disk_path], check=True)
        print(f"Перезапись {disk_path} завершена.")

        if remove:
            print(f"Удаляем метаданные и файловую систему на {disk_path}...")
            subprocess.run(['mkfs.ext4', '-F', disk_path], check=True)
            print(f"Метаданные и файловая система на {disk_path} удалены.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при перезаписи {disk_path}: {e}")

def main():
    print("Внимание! Эта программа полностью очистит указанный диск или раздел без возможности восстановления данных.")
    disk_path = input("Введите путь к диску или разделу, который нужно очистить (например, /dev/sdb1): ").strip()
    confirm = input("Вы уверены, что хотите очистить этот диск или раздел? (да/нет): ").strip().lower()
    
    if confirm == 'да':
        passes = int(input("Введите количество проходов перезаписи (рекомендуется 3-5): ").strip())
        remove_fs = input("Хотите удалить метаданные и файловую систему? (да/нет): ").strip().lower() == 'да'
        shred_disk(disk_path, passes, remove_fs)
        print("Очистка завершена.")
    else:
        print("Очистка отменена.")

if __name__ == "__main__":
    main()
