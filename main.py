# Импорт модулей и библиотек
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def fix_filename(wrong_name):
    """Преобразует строку из неправильной кодировки в нормальную. Актуально для файлов, скачиваемых с сетевого диска университета"""
    try:
        # Кодируем в байты как cp1252, затем декодируем как cp1251
        return wrong_name.encode('cp1252').decode('cp1251')
    except Exception as e:
        print(f"Ошибка перекодировки: {e}")
        return wrong_name

# Выбор и переименование файла.
def select_and_rename_file():
    # 1. Выбор файла
    file_path = filedialog.askopenfilename(
        title="Выберите файл с битой кодировкой"
    )

    if not file_path:
        return

    # Получаем директорию, старое имя и расширение
    directory = os.path.dirname(file_path)
    old_name = os.path.basename(file_path)

    # 2. Исправление имени
    new_name = fix_filename(old_name)
    new_file_path = os.path.join(directory, new_name)

    # 3. Переименование
    try:
        if os.path.exists(new_file_path):
            messagebox.showerror("Ошибка", "Файл с таким именем уже существует!")
            return

        os.rename(file_path, new_file_path)
        messagebox.showinfo("Успех", f"Файл переименован в:\n{new_name}")

    except OSError as e:
        messagebox.showerror("Ошибка", f"Не удалось переименовать: {e}")


# Настройка графического интерфейса
root = tk.Tk()
root.title("Восстановление кодировки файлов")
root.geometry("400x150")

label = tk.Label(root, text="Нажмите кнопку для выбора и\nисправления имени файла", pady=20)
label.pack()

btn = tk.Button(root, text="Выбрать и исправить файл", command=select_and_rename_file)
btn.pack()

root.mainloop()