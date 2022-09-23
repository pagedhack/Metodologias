from ctypes import windll
from tkinter import Button
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter.tix import COLUMN
from tkinter.ttk import Style
from turtle import width

def b_menu(window):
    b_menu = tk.Menu(window)
    
    window.config(menu = b_menu, width= 600, height= 500)

    menu_inicio = tk.Menu(b_menu, tearoff= 0)
    b_menu.add_cascade(label="Inicio", menu = menu_inicio)

    menu_inicio.add_command(label= "Registrar")
    menu_inicio.add_command(label= "Eliminar")
    menu_inicio.add_command(label= "Modificar")
    menu_inicio.add_command(label= "Salir", command= window.destroy)

    b_menu.add_cascade(label="Consulta")
    b_menu.add_cascade(label="Ayuda")
    b_menu.add_cascade(label="Cerrar Sesion")
    

class Frame(tk.Frame):
    def __init__(self, window = None):
        super().__init__(window, width= 600, height= 500)
        self.window = window
        self.pack()

        self.registro_shoe()
        self.def_camp()
        #self.tabla()

    def registro_shoe(self):

        #busquedad de zapato por imagen
        #img = tkinter.PhotoImage(file="img.png")
        #n_img = tkinter.Label(self.window , image= img)
        #n_img.place(x=100, y=100)
        #n_img.pack()

        #labels del registro de los zapatos

        self.label_code = tk.Label(self, text= "Codigo: ")
        self.label_code.config(font= ("Arial", 10))
        self.label_code.place(x= 50, y= 300)

        self.label_stock = tk.Label(self, text= "Stock: ")
        self.label_stock.config(font= ("Arial", 10))
        self.label_stock.place(x= 150, y= 50)

        self.label_Categoria = tk.Label(self, text= "Categoria: ")
        self.label_Categoria.config(font= ("Arial", 10))
        self.label_Categoria.place(x= 150, y= 100)

        self.label_model = tk.Label(self, text= "Modelo: ")
        self.label_model.config(font= ("Arial", 10))
        self.label_model.place(x= 150, y= 150)

        self.label_size = tk.Label(self, text= "Tamaño: ")
        self.label_size.config(font= ("Arial", 10))
        self.label_size.place(x= 150, y= 200)

        self.label_number = tk.Label(self, text= "Numero: ")
        self.label_number.config(font= ("Arial", 10))
        self.label_number.place(x= 150, y= 250)

        self.label_color = tk.Label(self, text= "Color: ")
        self.label_color.config(font= ("Arial", 10))
        self.label_color.place(x= 370, y= 200)


        #entradas del registro de zapatos
        self.code = tk.Entry(self.window)
        self.code.place(x=100, y=300)
        self.code.focus()
        
        self.stock = tk.Entry(self.window)
        self.stock.place(x=220, y=50)
        self.stock.config(state='disabled')
        self.stock.focus()     

        self.categoria = tk.Entry(self.window)
        self.categoria.place(x= 220, y=100)  
        self.categoria.config(state='disabled')
        self.categoria.focus()

        self.model = tk.Entry(self.window)
        self.model.place(x=220, y=150)
        self.model.config(state='disabled')
        self.model.focus()   

        self.size = tk.Entry(self.window)
        self.size.place(x=220, y=200)
        self.size.config(state='disabled')
        self.size.focus()   

        self.numbers = tk.Entry(self.window)
        self.numbers.place(x=220, y=250)
        self.numbers.config(state='disabled')
        self.numbers.focus()   

        self.color = tk.Entry(self.window)
        self.color.place(x=420, y=200)
        self.color.config(state='disabled')
        self.color.focus()

        #botones del registro
        self.nuevo = Button(self.window, text="Nuevo", command= self.hab_camp)
        self.nuevo.place(x=30, y=50)
        self.nuevo.config(padx=16, pady=3, font= ("Arial", 10, "bold"), cursor= "hand2")

        self.guardar = Button(self.window, text="Guardar")
        self.guardar.place(x=30, y=120)
        self.guardar.config(padx=13, pady=3, font= ("Arial", 10, "bold"), cursor= "hand2")

        self.cancelar = Button(self.window, text="Cancelar", command= self.def_camp)
        self.cancelar.place(x=30, y=190)
        self.cancelar.config(padx=13, pady=3, font= ("Arial", 10, "bold"), cursor= "hand2")


    def hab_camp(self):
        self.categoria.config(state="normal")
        self.model.config(state="normal")
        self.size.config(state="normal")
        self.numbers.config(state="normal")
        self.color.config(state="normal")
        self.stock.config(state="normal")

        self.guardar.config(state="normal")
        self.cancelar.config(state="normal")

    def def_camp(self):
        self.categoria.config(state="disabled")
        self.model.config(state="disabled")
        self.size.config(state="disabled")
        self.numbers.config(state="disabled")
        self.color.config(state="disabled")
        self.stock.config(state="disabled")

        self.guardar.config(state="disabled")
        self.cancelar.config(state="disabled")


    