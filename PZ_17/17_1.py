# соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("All Fields Form")

# Title
title_label = tk.Label(root, text="ALL FIELDS FORM", font=("Helvetica", 16, "bold"), fg="blue", anchor="w")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Textfield
tk.Label(root, text="Textfield", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
textfield = tk.Entry(root, width=40)
textfield.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Textarea
tk.Label(root, text="Textarea", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
textarea = tk.Text(root, height=5, width=30)
textarea.grid(row=2, column=1, padx=10, pady=5)

# Email Address
tk.Label(root, text="Email Address", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=3, column=1, padx=10, pady=5)

# Dropdown
tk.Label(root, text="Dropdown", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
options = ["Option 1", "Option 2", "Option 3"]
dropdown = ttk.Combobox(root, values=options)
dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="w")
dropdown.current(0)

# Radio Buttons
tk.Label(root, text="Radio Button", font=("Helvetica", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="w")
radio_var = tk.StringVar()
tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1").grid(row=5, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2").grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Checkboxes
tk.Label(root, text="Checkbox", font=("Helvetica", 12)).grid(row=7, column=0, padx=10, pady=5, sticky="w")
chk_var1 = tk.BooleanVar()
chk_var2 = tk.BooleanVar()
chk_var3 = tk.BooleanVar()
tk.Checkbutton(root, text="Option 1", variable=chk_var1).grid(row=7, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Option 2", variable=chk_var2).grid(row=8, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Option 3", variable=chk_var3).grid(row=9, column=1, padx=10, pady=5, sticky="w")

# Password field
tk.Label(root, text="Password", font=("Helvetica", 12)).grid(row=10, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(root, show="*", bg="yellow", width=40)
password_entry.grid(row=10, column=1, padx=10, pady=5)

# Number field
tk.Label(root, text="Number Field", font=("Helvetica", 12)).grid(row=11, column=0, padx=10, pady=5, sticky="w")
number_entry = tk.Entry(root, width=40)
number_entry.grid(row=11, column=1, padx=10, pady=5)

tk.Label(root, text="Mathematical Captcha", font=("Helvetica", 12)).grid(row=12, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="6 + 8 =", font=("Helvetica", 8, "bold")).grid(row=12, column=1, padx=10, pady=5, sticky="w")

def on_entry_click(event):
    if captcha_entry.get() == 'Enter sum':
        captcha_entry.delete(0, "end")  # Удалить все содержимое
        captcha_entry.insert(0, '')  # Убедиться, что поле пустое
        captcha_entry.config(fg='black')

def on_focusout(event):
    if captcha_entry.get() == '':
        captcha_entry.insert(0, 'Enter sum')
        captcha_entry.config(fg='grey')

captcha_entry = tk.Entry(root, fg='grey', width=10)
captcha_entry.grid(row=12, column=1, padx=50, pady=5, sticky="w")
captcha_entry.insert(0, 'Enter sum')
captcha_entry.bind('<FocusIn>', on_entry_click)
captcha_entry.bind('<FocusOut>', on_focusout)


# Google Captcha
tk.Label(root, text="Google Captcha", font=("Helvetica", 12)).grid(row=13, column=0, padx=10, pady=5, sticky="w")

# Placeholder для отображения капчи как на картинке
captcha_frame = tk.Frame(root, bd=1, relief="solid")
captcha_frame.grid(row=13, column=1, padx=10, pady=5, sticky="w")

# Checkbox для подтверждения
tk.Checkbutton(captcha_frame, text="I'm not a robot", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Загружаемое изображение (например, логотип капчи)
captcha_image_path = "captcha_image.png"
img = Image.open(captcha_image_path)
img = img.resize((50, 50))  # Изменение размера изображения
img = ImageTk.PhotoImage(img)
image_label = tk.Label(captcha_frame, image=img)
image_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")
image_label.image = img  # Необходимо сохранить ссылку на изображение

# Submit button
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 12), fg="white", bg="dodgerblue")
submit_button.grid(row=14, column=1, padx=10, pady=20, sticky="w")

root.mainloop()
