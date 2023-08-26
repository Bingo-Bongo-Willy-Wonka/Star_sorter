"""
Делаем калькулятор через ткинтер
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numexpr as n


def add(x):
    entry.insert(string=x, index="end")
    return


def make(x):
    return tk.Button(window, text=x, font=("arial", 20),
                     bd=0, fg="#FFFFFF", bg="#2E2E2E", activebackground="#1C1C1C", activeforeground="#FFFFFF",
                     command=lambda: add(x))


def equal():
    try:
        itog = str(n.evaluate(entry.get()))
        entry.delete(0, "end")
        entry.insert(0, itog)
        print(itog)
    except:
        messagebox.showinfo("Ошибка", "Неверный ввод")
        entry.delete(0, "end")


def c():
    entry.delete(0, "end")


window = Tk()
window.title("Calculator")
window.geometry("320x420+900+100")
window.resizable(False, False)
window.config(bg="#1C1C1C")
#
# photo = tk.PhotoImage(file="Calc_photo_2.png")
# window.iconphoto(False, photo)

for i in range(6):
    window.grid_rowconfigure(i, minsize=65)

for i in [0, 1, 4, 5]:
    window.grid_columnconfigure(i, minsize=80)

for i in [2, 3]:
    window.grid_columnconfigure(i, minsize=40)

make("1").grid(column=0, row=1, stick="nswe", padx=5, pady=5)

make("2").grid(column=1, row=1, stick="nswe", padx=5, pady=5)

make("3").grid(column=2, row=1, columnspan=2, stick="nswe", padx=5, pady=5)

make("4").grid(column=0, row=2, stick="nswe", padx=5, pady=5)

make("5").grid(column=1, row=2, stick="nswe", padx=5, pady=5)

make("6").grid(column=2, row=2, columnspan=2, stick="nswe", padx=5, pady=5)

make("7").grid(column=0, row=3, stick="nswe", padx=5, pady=5)

make("8").grid(column=1, row=3, stick="nswe", padx=5, pady=5)

make("9").grid(column=2, row=3, columnspan=2, stick="nswe", padx=5, pady=5)

make("0").grid(column=1, row=4, stick="nswe", padx=5, pady=5)

make(".").grid(column=0, row=4, stick="nswe", padx=5, pady=5)

make("(").grid(column=2, row=4, stick="nswe", padx=5, pady=5)

make(")").grid(column=3, row=4, stick="nswe", padx=5, pady=5)

make("c").grid(column=0, row=5, stick="nswe", padx=5, pady=5)

make("+").grid(column=4, row=1, stick="nswe", padx=5, pady=5)

make("-").grid(column=4, row=2, stick="nswe", padx=5, pady=5)

make("*").grid(column=4, row=3, stick="nswe", padx=5, pady=5)

make("/").grid(column=4, row=4, stick="nswe", padx=5, pady=5)

make("**").grid(column=4, row=5, stick="nswe", padx=5, pady=5)

tk.Button(window, text="=", font=("arial", 20),
          bd=0, fg="#FFFFFF", bg="#2E2E2E", activebackground="#1C1C1C", activeforeground="#FFFFFF", command=equal). \
    grid(column=1, row=5, columnspan=3, stick="nswe", padx=5, pady=5)

tk.Button(window, text="c", font=("arial", 20),
          bd=0, fg="#FFFFFF", bg="#2E2E2E", activebackground="#1C1C1C", activeforeground="#FFFFFF", command=c) \
    .grid(column=0, row=5, stick="nswe", padx=5, pady=5)

entry = tk.Entry(window, font=("arial", 20), fg="#FFFFFF", bg="#1C1C1C", highlightthickness="3")
entry.grid(column=0, row=0, columnspan=5, stick="nswe")

window.mainloop()

