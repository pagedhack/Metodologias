from functools import _lru_cache_wrapper
from struct import pack
from tkinter import CENTER, INSIDE, X, Button, Image, PhotoImage
import tkinter as tk
from tkinter import ttk
from tkinter.tix import Tree
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

        self.consulta_shoe()
        self.tabla()

    def consulta_shoe(self):

        #self.label_titulo = tk.Label(self, text= "-Consultas-")
        #self.label_titulo.config(font= ("Comic Sans MS", 12, "bold"))
        #self.label_titulo.configure(bg="blue")
        #self.label_titulo.pack(anchor=CENTER)
        #self.label_titulo.place(x= 0, y= 0, width=500)
        

    #labels y entradas de la consulta de los zapatos

        #code
        self.label_code = tk.Label(self, text= "Codigo: ")#label codigo
        self.label_code.config(font= ("Comic Sans MS", 12, "bold"))
        self.label_code.configure(bg="beige")
        self.label_code.place(x= 20, y= 30)

        self.code = tk.Entry(self.window)   #Entrada
        self.code = tk.Entry(justify=tk.CENTER, width=10, font=("bold"))
        self.code.place(bordermode=INSIDE, x=80, y=33, height=25)
        self.code.focus()

        image = PhotoImage('lupa.gif')
        self.buscar = Button(self.window,text="Buscar",height=1, width=5) # type: ignore
        self.buscar.place(x=173, y=33)

        
        #stock
        self.label_stock = tk.Label(self, text= "Stock: ")#label stock
        self.label_stock.config(font= ("Comic Sans MS", 10, "bold"))
        self.label_stock.configure(bg="beige")
        self.label_stock.place(x= 250, y= 30)

        self.stock = tk.Entry(self.window)  #Entrada
        self.stock = tk.Entry(justify=tk.CENTER, width=10)
        self.stock.place(bordermode=INSIDE,x=305, y=33, height=20)
        self.stock.config(state="readonly")
        self.stock.focus()

        #categoria
        self.label_Categoria = tk.Label(self, text= "Categoria: ")#label
        self.label_Categoria.config(font= ("Comic Sans MS", 10, "bold"))
        self.label_Categoria.configure(bg="beige")
        self.label_Categoria.place(x= 400, y= 30)

        self.categoria = tk.Entry(self.window)  #Entrada
        self.categoria = tk.Entry(justify=CENTER,width=10)
        self.categoria.place(bordermode=INSIDE, x= 480, y=30, height=25)  
        self.categoria.config(state="readonly")
        self.categoria.focus()

        #modelo
        self.label_model = tk.Label(self, text= "Modelo: ")#label
        self.label_model.config(font= ("Comic Sans MS", 10, "bold"))
        self.label_model.configure(bg="beige")
        self.label_model.place(x= 20, y= 100)

        self.model = tk.Entry(self.window)  #Entrada
        self.model = tk.Entry(justify=CENTER,width=10)
        self.model.place(bordermode=INSIDE, x= 100, y=100, height=25) 
        self.model.config(state="readonly")
        self.model.focus()

        #size
        self.label_size = tk.Label(self, text= "Tamaño: ")#label
        self.label_size.config(font= ("Comic Sans MS", 10, "bold"))
        self.label_size.configure(bg="beige")
        self.label_size.place(x= 20, y= 150)

        self.size = tk.Entry(self.window)  #Entrada
        self.size = tk.Entry(justify=CENTER,width=10)
        self.size.place(bordermode=INSIDE, x= 100, y=150, height=25) 
        self.size.config(state="readonly")
        self.size.focus()   

        #numero
        self.label_number = tk.Label(self, text= "Numero: ")#label
        self.label_number.config(font= ("Comic Sans MS", 10, "bold"))
        self.label_number.configure(bg="beige")
        self.label_number.place(x= 20, y= 200)

        self.numbers = tk.Entry(self.window)  #Entrada
        self.numbers = tk.Entry(justify=CENTER,width=10)
        self.numbers.place(bordermode=INSIDE, x= 100, y=200, height=25) 
        self.numbers.config(state="readonly")
        self.numbers.focus()

        #color
        self.label_color = tk.Label(self, text= "Color: ")#label
        self.label_color.config(font= ("Comic Sans MS", 10, "bold"))
        self.label_color.configure(bg="beige")
        self.label_color.place(x= 20, y= 250) 

        self.color = tk.Entry(self.window)  #Entrada
        self.color = tk.Entry(justify=CENTER,width=10)
        self.color.place(bordermode=INSIDE, x= 100, y=250, height=25) 
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

    def tabla(self):

        self.table = ttk.Treeview(self, 
            columns = ('Codigo', 'Stock', 'Categoria', 'Modelo', 'Tamaño', 'Numero', 'Color'))
        
        self.table.heading('#0', text='Codigo')
        self.table.heading('#1', text='Stock')
        self.table.heading('#2', text='Categoria')
        self.table.heading('#3', text='Modelo')
        self.table.heading('#4', text='Tamaño')
        self.table.heading('#5', text='Numero')
        self.table.heading('#6', text='Color')

        

 #busquedad de zapato por imagen
        #img = tkinter.PhotoImage(file="img.png")
        #n_img = tkinter.Label(self.window , image= img)
        #n_img.place(x=100, y=100)
        #n_img.pack()