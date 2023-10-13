from tkinter import messagebox
import tkinter as tk
import requests

def open_about_window():
    """
        Открывает окно "О программе" и отображает описание программы.

        Описание:
            Эта функция создает новое окно "О программе" и отображает в нем описание программы.
            Описание программы загружается из файла data_utils/program_description.txt и выводится в текстовое поле окна.

    """
    about_window = tk.Toplevel()
    about_window.title("О программе")
    about_text = tk.Text(about_window, height=30, width=103)
    about_text.pack()
    with open("../data_utils/program_description.txt", "r", encoding="utf-8") as f:
        about_text.insert(tk.END, f.read())

def get_version():
    """
        Получает версию программы из GitHub репозитория и отображает ее в сообщении.

        Описание:
            Эта функция отправляет GET-запрос к GitHub API, чтобы получить информацию о последнем релизе программы.
            Если запрос успешен, версия программы извлекается из данных о релизе
            и отображается в информационном диалоговом окне. В случае ошибки при выполнении запроса,
            отображается сообщение об ошибке.

    """
    url = "https://api.github.com/repos/Krnvaa/Rotating_line_segment/releases/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()
        release_data = response.json()
        version = release_data.get("tag_name", "Версия не найдена")
        messagebox.showinfo("Версия", f"Версия программы: {version}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка при получении версии: {e}")