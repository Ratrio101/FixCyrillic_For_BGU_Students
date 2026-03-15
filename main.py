import os
import tkinter as tk
from tkinter import filedialog, messagebox

def fix_filename(wrong_name):
    try:
        return wrong_name.encode('cp1252').decode('cp1251')
    except Exception:
        return wrong_name

def show_about():
    messagebox.showinfo("Об авторе", "Программа для восстановления имен файлов.\nАвтор: Владислав Скибчик\nВерсия 1.1")

def show_help():
    help_text = (
        "1. Нажмите кнопку 'Выбрать файл'.\n"
        "2. Выберите файл с 'кракозябрами' в названии.\n"
        "3. Программа автоматически заменит их на кириллицу."
    )
    messagebox.showinfo("Помощь", help_text)

def select_and_rename_file():
    file_path = filedialog.askopenfilename(title="Выберите файл")
    if not file_path:
        return

    directory = os.path.dirname(file_path)
    old_name = os.path.basename(file_path)
    new_name = fix_filename(old_name)
    new_file_path = os.path.join(directory, new_name)

    try:
        if os.path.exists(new_file_path):
            messagebox.showerror("Ошибка", "Файл с таким именем уже существует!")
            return
        os.rename(file_path, new_file_path)
        messagebox.showinfo("Успех", f"Файл переименован в:\n{new_name}")
    except OSError as e:
        messagebox.showerror("Ошибка", f"Не удалось переименовать: {e}")

root = tk.Tk()
root.title("Восстановление кодировки")
root.geometry("400x150")

# --- СОЗДАНИЕ МЕНЮ ---
main_menu = tk.Menu(root)
root.config(menu=main_menu)

# Вкладка "Справка" (объединяем Помощь и Об авторе)
info_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Справка", menu=info_menu)
info_menu.add_command(label="Инструкция", command=show_help)
info_menu.add_separator() # Разделительная черта
info_menu.add_command(label="Об авторе", command=show_about)

# Можно добавить вкладку "Файл" для выхода
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Выход", command=root.quit)
# ---------------------

label = tk.Label(root, text="Нажмите кнопку для выбора и\nисправления имени файла", pady=20)
label.pack()

btn = tk.Button(root, text="Выбрать и исправить файл", command=select_and_rename_file)
btn.pack()

root.mainloop()