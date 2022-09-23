from cgitb import text
from tkinter import messagebox
from tkinter import ttk
from turtle import width
import tkinter as tk

from inicio.py_inicio import Login

#from menu_admin.py_menu_admin import Frame, b_menu
#from menu_consulta.py_menu_cons import Frame,b_menu

def main():
    window = tk.Tk()
    window.title("Zapateria")
    window.resizable(False,False)
    window.iconbitmap('img/icono (1).ico')

    #b_menu(window)
    #app = Frame(window= window)

    app = Login(window= window)

    app.mainloop()

if __name__ == "__main__":
    main()
