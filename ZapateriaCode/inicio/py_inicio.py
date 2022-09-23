from logging import root
from tkinter import Button, Entry, Label, Toplevel, messagebox
import tkinter as tk
import mysql.connector

from menu_admin.py_menu_admin import Frame, b_menu

class Login(tk.Frame):
    def __init__(self, window = None):
        super().__init__(window,width= 300, height= 300)
        self.window = window
        self.pack()

    def administrador(self, window):

        self.username = Entry(self.window)
        self.username.place(x=110, y=80)
        self.username.focus()   
        mi_Label = Label(window, text="Usuario: ") #Label user
        mi_Label.pack()
        mi_Label.config(font=('Arial', 10,"bold"))
        mi_Label.config(fg="black")
        mi_Label.place(x= 50, y= 80)

        self.password = Entry(self.window)
        self.password.place(x=110, y=150)
        mi_Label = Label(window, text="Contraseña: ") #Label pass
        mi_Label.pack()
        mi_Label.config(font=('Arial', 10)) 
        mi_Label.config(fg="black")  
        mi_Label.place(x= 30, y= 150)

        self.login = Button(self.window, text="Login", command=self.login)  # type: ignore
        self.login.place(x=80, y=190)

        self.register = Button(self.window, text="Register", command=self.register)  # type: ignore
        self.register.place(x=180, y=190)

        self.exit = Button(self.window, text="Exit", command=self.window.destroy)   # type: ignore
        self.exit.place(x=140, y=240)

    def login(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="123456789", database="shoes")
        cursor = connection.cursor()
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showwarning("Warning", "All fields are required")
        else:
            try:
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                values = (username, password)
                cursor.execute(query, values)
                user = cursor.fetchone()
                if user[0] == username and user[1] == password: # type: ignore
                    
                    pass
                else:
                    messagebox.showwarning("Warning", "Username or password incorrect")
            except:
                    messagebox.showinfo(message= "The user is registered", title= "Registered user")