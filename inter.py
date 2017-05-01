import serial as s
import sys
import time
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk,font

class InterfazHamm():
    def __init__(self):
       self.raiz = Tk()
       self.raiz.config(bg="light blue")
       self.raiz.resizable(0,0)
       self.raiz.geometry("550x450")
       #Variable
       self.Emisor = StringVar()
       self.Receptor = StringVar()
       #self.ser = s.Serial('/dev/ttyUSB0',9600)
       #Fuentes
       self.Arial50 = font.Font(family="Arial",size=50)
       self.Arial30 = font.Font(family="Arial",size=30)
       self.Arial15 = font.Font(family="Arial",size=15)
       #Widgets
       self.cuerpo = ttk.Frame(self.raiz,borderwidth=2,relief="ridge",)
       self.cuerpo_menu_principal = Frame(self.raiz,background="light blue")
       self.cuerpo_principal1 = ttk.Frame(self.raiz,borderwidth=3,relief="ridge")
       self.cuerpo_principal2 = ttk.Frame(self.raiz,borderwidth=3,relief="ridge")
       self.panel_principal1 = PanedWindow(self.cuerpo_principal1,width=690,height=500,background="light blue")
       self.panel_principal2 = PanedWindow(self.cuerpo_principal2,width=690,height=500,background="light blue")
       self.creditos = ttk.Label(self.raiz,font=self.Arial15,text="Creado por:\n Changua\n Campeche\n Borracho",foreground="orange red",background="light blue")
       self.ingreso_text = ttk.Label(self.panel_principal1,text="Mensaje: ",font=self.Arial15,foreground="orange red",background="light blue",borderwidth=43)
       self.texto = ttk.Entry(self.panel_principal1,textvariable=self.Emisor,foreground="orange red")
       self.enviar = ttk.Button(self.panel_principal1,text="Enviar",command=self.prueba) #falta hacer la funcion para poner el metodo del comando.
       self.limpiar = ttk.Button(self.raiz,text="limpiar chat")
       self.chat = ttk.Label(self.panel_principal2,textvariable=self.Receptor,font=self.Arial15,foreground="orange red",background="white",borderwidth=150)
       #poscionamiento de elementos
       self.cuerpo.grid(column=0,row=0)
       self.cuerpo_menu_principal.grid(column=1,row=0,sticky="n")
       self.cuerpo_principal1.grid(column=0,row=0,sticky="w")
       self.cuerpo_principal2.grid(column=0,row=1)
       self.panel_principal1.grid(column=0,row=0)
       self.panel_principal2.grid(column=0,row=0)
       self.creditos.grid(column=1,row=1,sticky="s,e")
       self.limpiar.grid(column=1,row=0,padx=10,pady=10)
       self.ingreso_text.grid(column=0,row=1,sticky="e")
       self.texto.grid(column=1,row=1,sticky="w,e")
       self.enviar.grid(column=2,row=1,sticky="e")
       self.chat.pack()
       #inicio de interfaz
       self.Receptor=self.Emisor.get()
       self.aux=0
       self.raiz.mainloop()
    def prueba(self):
        self.Receptor=self.Emisor.get()
        self.chat = ttk.Label(self.panel_principal2,textvariable=self.Receptor)
        self.chat.pack()
        self.aux=+1
        print(self.Receptor)
if __name__== '__main__':
    mi_interfaz = InterfazHamm()
