from tkinter import INSIDE, Button, Image, PhotoImage
import tkinter as tk
from tkinter import ttk
from turtle import width

def b_menu(window):
    b_menu = tk.Menu(window)
    
    window.config(menu = b_menu, width= 600, height= 500)

    menu_inicio = tk.Menu(b_menu, tearoff= 0)
    b_menu.add_cascade(label="Ayuda")
    b_menu.add_cascade(label="Cerrar Sesion")
    

class Frame(tk.Frame):
    def __init__(self, window = None):
        super().__init__(window, width= 600, height= 500)
        self.window = window
        self.configure(bg="beige")
        
        self.pack()

        self.registro_shoe()
        #self.tabla()

    def registro_shoe(self):

        #busquedad de zapato por imagen
        #img = tkinter.PhotoImage(file="img.png")
        #n_img = tkinter.Label(self.window , image= img)
        #n_img.place(x=100, y=100)
        #n_img.pack()

        #labels y entradas de la consulta de los zapatos

        self.label_code = tk.Label(self, text= "Codigo: ")#label codigo
        self.label_code.config(font= ("Comic Sans MS", 12, "bold"))
        self.label_code.configure(bg="beige")
        self.label_code.place(x= 20, y= 45)
        self.code = tk.Entry(self.window)   #Entrada
        self.code = tk.Entry(justify=tk.CENTER, width=15, font=("bold"))
        self.code.place(bordermode=INSIDE, x=80, y=50, height=25)
        self.code.focus()
        #img = PhotoImage(file="lupa.gif")
        self.buscar = Button(self.window,text="Buscar", height=1, width=5) # type: ignore
        self.buscar.place(x=210, y=50)

        

        self.label_stock = tk.Label(self, text= "Stock: ")#label stock
        self.label_stock.config(font= ("Comic Sans MS", 12, "bold"))
        self.label_stock.configure(bg="beige")
        #self.label_stock.place(x= 150, y= 50)
        self.stock = tk.Entry(self.window)  #Entrada
        self.stock = tk.Entry(justify=tk.CENTER)
        #self.stock.place(x=220, y=50, height=25)
        self.stock.config(state="readonly")
        self.stock.focus()

        self.label_Categoria = tk.Label(self, text= "Categoria: ")#label
        self.label_Categoria.config(font= ("Arial", 12))
        self.label_Categoria.configure(bg="beige")
        self.label_Categoria.place(x= 150, y= 100)
        self.categoria = tk.Entry(self.window)  #Entrada
        self.categoria.place(x= 220, y=100)  
        self.categoria.config(state="readonly")
        self.categoria.focus()

        self.label_model = tk.Label(self, text= "Modelo: ")#label
        self.label_model.config(font= ("Arial", 10))
        self.label_model.configure(bg="beige")
        self.label_model.place(x= 150, y= 150)
        self.model = tk.Entry(self.window)  #Entrada
        self.model.place(x=220, y=150)
        self.model.config(state="readonly")
        self.model.focus()

        self.label_size = tk.Label(self, text= "Tamaño: ")#label
        self.label_size.config(font= ("Arial", 10))
        self.label_size.configure(bg="beige")
        self.label_size.place(x= 150, y= 200)
        self.size = tk.Entry(self.window)  #Entrada
        self.size.place(x=220, y=200)
        self.size.config(state="readonly")
        self.size.focus()   

        self.label_number = tk.Label(self, text= "Numero: ")#label
        self.label_number.config(font= ("Arial", 10))
        self.label_number.configure(bg="beige")
        self.label_number.place(x= 150, y= 250)
        self.numbers = tk.Entry(self.window)  #Entrada
        self.numbers.place(x=220, y=250)
        self.numbers.config(state="readonly")
        self.numbers.focus()

        self.label_color = tk.Label(self, text= "Color: ")#label
        self.label_color.config(font= ("Arial", 10))
        self.label_color.configure(bg="beige")
        self.label_color.place(x= 370, y= 200) 
        self.color = tk.Entry(self.window)  #Entrada
        self.color.place(x=420, y=200)
        self.color.config(state="readonly")
        self.color.focus() 

        


        

    def hab_camp(self):
        self.categoria.config(state="normal")
        self.model.config(state="normal")
        self.size.config(state="normal")
        self.numbers.config(state="normal")
        self.color.config(state="normal")
        self.stock.config(state="normal")

    def def_camp(self):
        self.categoria.config(state="disabled")
        self.model.config(state="disabled")
        self.size.config(state="disabled")
        self.numbers.config(state="disabled")
        self.color.config(state="disabled")
        self.stock.config(state="disabled")
