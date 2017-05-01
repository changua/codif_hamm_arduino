from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import  serial  as s
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import time
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk, font
#---------End of imports

#----------Empieza la clase que alberga la Interfaz
class InterfazShield():
    def __init__(self):
        #------Atributos

        #Declarar Ventana
        self.raiz = Tk()
        self.raiz.config(bg="light blue")
        self.raiz.resizable(0,0)
        self.raiz.geometry("+350+50")
        #self.fig = plt.Figure(facecolor="LightBlue")
        #self.fig1 = plt.Figure(facecolor="LightBlue")

        #Declaracion de variables
        #self.variable_voltaje = DoubleVar(value=0.0)
        self.variable_menu = IntVar()
        #self.variable_senal = IntVar(value=1)
        #self.canal=IntVar()
        self.aux = IntVar()
        self.auxi=IntVar()
        self.tipo=IntVar(value=0)
        self.variable_canal = IntVar(value=0)
        #self.ser = s.Serial('/dev/ttyUSB0',9600)
        #Empieza las variables codigo del osciloscopio
        #self.xvalues = []
        #self.yvalues = []
        #self.ax1 = self.fig1.add_subplot(1, 1, 1)
        #self.ax1.set_ylim(-15,15)
        #self.line1, = self.ax1.plot(self.xvalues, self.yvalues, 'g')
        #Empieza las variables codigo del generador
        #self.xvalues1 = []
        #self.yvalues1 = []
        #self.ax = self.fig.add_subplot(1, 1, 1)
        #self.ax.set_ylim(-15,15)
        #self.line, = self.ax.plot(self.xvalues1, self.yvalues1, 'g')
        #self.x=0
        #Fuentes"light blue"
        self.arial50=font.Font(family="Arial",size=50)
        self.arial30=font.Font(family="Arial",size=30)
        self.arial15=font.Font(family="Arial",size=15)
        self.arial5=font.Font(family="Arial",size=5)
        #Widgets
        self.cuerpo = ttk.Frame(self.raiz, borderwidth=2,relief="ridge",)
        self.cuerpo_menu_principal = Frame(self.raiz,background="light blue")
        #self.menu1 = Radiobutton(self.cuerpo_menu_principal,text="Osciloscopio",background="light blue",fg="orange red",font=self.arial15,variable=self.variable_menu,value=1,indicatoron="off",command=self.comprobar,activebackground="orange red",selectcolor="light blue")
        #self.menu2 = Radiobutton(self.cuerpo_menu_principal,text="Generador   ",background="light blue",fg="orange red",indicatoron = 0,font=self.arial15,variable=self.variable_menu,value=2,command=self.comprobar,activebackground="orange red",selectcolor="light blue")
        self.cuerpo_principal1 = ttk.Frame(self.raiz, borderwidth=2,relief="ridge")
        self.panel_principal2 = PanedWindow(self.cuerpo_principal1,width=690,height=500,background="light blue")
        self.panel_principal3 = PanedWindow(self.cuerpo_principal1,width=690,height=500,background="light blue")
        self.creditos = ttk.Label(self.raiz,font = self.arial15,text = "Creado por:\n  Changua\n Campeche",foreground="orange red",background="light blue")
        self.msnvoltaje = ttk.Label(self.panel_principal3,text="Ingrese el voltaje :",font=self.arial15,foreground="orange red",background="light blue")
        #self.entrada = ttk.Entry(self.panel_principal3,textvariable=self.variable_voltaje,foreground="orange red")
        #self.submenu1 = LabelFrame(self.panel_principal3, text="Tipo de senal",foreground="orange red",background="light blue")
        #self.subm1_opcion1 = Radiobutton(self.submenu1,text="Senoidal        ",command=self.leer,fg="orange red",padx = 20,variable=self.variable_senal,value=1,background="light blue",indicatoron="off",activebackground="orange red",selectcolor="light blue")
        #self.subm1_opcion2 = Radiobutton(self.submenu1,text="Cuadrada        ",command=self.leer,fg="orange red",padx= 20,variable=self.variable_senal,value=2,background="light blue",indicatoron="off",activebackground="orange red",selectcolor="light blue")
        #self.subm1_opcion3 = Radiobutton(self.submenu1,text="Triangular      ",command=self.leer,fg="orange red",padx=20,variable=self.variable_senal,value=3,background="light blue",indicatoron="off",activebackground="orange red",selectcolor="light blue")
        #self.msnvoltaje2 = ttk.Label(self.panel_principal2,text="Osciloscopio",foreground="orange red",font=self.arial30,background="light blue")
        #self.msnvoltaje3 = ttk.Label(self.panel_principal3,text="Generador   ",foreground="orange red",font=self.arial30,justify="center",background="light blue")
        #self.canvas2 = FigureCanvasTkAgg(self.fig1,master=self.panel_principal2)
        #self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_principal3)
        #self.submenu2 = LabelFrame(self.panel_principal2, text="Canales",fg="orange red",background="light blue")
        #self.subm2_opcion1 = Radiobutton(self.submenu2,text="Canal 1          ",command=self.cambiar_canal,fg="orange red",padx = 20,variable=self.variable_canal,value=1,background="light blue",indicatoron="off",activebackground="orange red",selectcolor="light blue")
        #self.subm2_opcion2 = Radiobutton(self.submenu2,text="Canal 2          ",command=self.cambiar_canal,fg="orange red",padx= 20,variable=self.variable_canal,value=2,background="light blue",indicatoron="off",activebackground="orange red",selectcolor="light blue")

        #propiedades Widgets
        self.cuerpo.grid(column=0,row=0)
        self.cuerpo_menu_principal.grid(column=1,row=0,sticky="n")
        #self.menu1.grid(column=0,row=0,pady=10,padx=10)
        #self.menu2.grid(row=1,column=0)
        #self.cuerpo_principal1.grid(column=0,row=0,sticky="w")
        #self.panel_principal2.grid(column=0,row=0)
        #self.panel_principal3.grid(column=0,row=0)
        self.creditos.grid(column=1,row=0,sticky="s")
        self.msnvoltaje.place(x=40,y=85)
        #self.entrada.place(x=300,y=90,width=100)
        #self.canvas.get_tk_widget().place(height=300,width=400,x=40,y=145)
        #self.submenu1.place(width=150,height=100,x=480,y=145)
        #self.subm1_opcion1.pack(anchor=W)
        #self.subm1_opcion2.pack(anchor=W)
        #self.subm1_opcion3.pack(anchor=W)
        #self.msnvoltaje2.place(x=277,y=15)
        #self.msnvoltaje3.place(y=15,x=277)
        #self.canvas2.get_tk_widget().place(height=300,width=400,x=40,y=145)
        #self.submenu2.place(width=150,height=60,x=480,y=145)
        #self.subm2_opcion1.pack(anchor=W)
        #self.subm2_opcion2.pack(anchor=W)

        #termina el bucle de la interfaz y actualiza los datos de la grafica
        #self.h=0
        #self.ani_widget()
        #self.ani_widget1()
        self.raiz.mainloop()
        self.panel_principal2.lift()
        #Metodos
   # def comprobar(self):
    #    if  self.variable_menu.get()==1:

     #       self.auxi=1
      #      self.panel_principal2.lift()
       # else:

        #    self.auxi=0
         #   self.panel_principal3.lift()


 #   def leer(self):

  #      if  self.variable_senal.get()==1:
   #         print("senoidal")
    #        self.tipo=1
     #       self.am=self.variable_voltaje.get()
      #  elif self.variable_senal.get()==2:
       #         print("cuadrada")
        #        self.tipo=2
        #        self.am=self.variable_voltaje.get()
        #elif self.variable_senal.get()==3:
        #        print("triangular")
        #        self.tipo=3
        #        self.am=self.variable_voltaje.get()


    #def cambiar_canal(self):

     #   if  self.variable_canal.get()==1:
      #      self.canal=1

       # else:
        #    self.canal=0

    #def animate(self,i):
     #   if self.auxi==0:
      #      try:
       #         if self.tipo==1:

        #            self.data1 =self.am*np.sin(i/10)

         #       elif self.tipo==2:

          #          if self.x < 21:
           #             self.data1=0
            #            self.x=self.x+1
             #       elif self.x > 20 and self.x < 41:
              #          self.data1=self.am
               #         self.x=self.x+1
                #    else:
                 #       self.x=0
                  #      self.data1=0
                #elif self.tipo==3:

                 #   if self.x <= self.am:
                 #       self.data1=self.x
                 #       self.x=self.x+1
                 #   elif self.x == self.am+1 and self.data1 > 1:
                 #       self.data1=self.data1-1
                 #   else:
                 #       self.data1=0
                 #       self.x=0
                #else:
                 #   self.data1=0
                #self.yvalues1.append(self.data1)
                #self.xvalues1.append(i)
                #self.line.set_data(self.xvalues1, self.yvalues1)
                #self.ax.set_xlim(0, i+1)
                #self.datax=((5/24)*self.data1)-(5/2)
                #self.ser.write(str(self.datax).encode('ascii'))
                #self.ser.write(b'z')
            #except ValueError:
            #    pass
        #else:
        #    pass
    #def ani_widget(self):

     #   self.ani = animation.FuncAnimation(self.fig, self.animate, interval=100, blit=False)
     #   self.canvas.show()
     #   self.ser.reset_input_buffer()

    #def animate1(self,a):
     #   self.ser.reset_input_buffer()
     #   if self.auxi==1:
     #       try:
      #          if  self.canal==1:
       #             self.ser.write(b'a')
       #         elif    self.canal==0:
         #               self.ser.write(b'b')
        #        self.data = self.ser.readline()
          #      self.yvalue = float(self.data)
           #     self.yvalue = (4.8*self.yvalue)-12
            #    self.yvalues.append(self.yvalue)
             #   self.xvalues.append(a)
              #  self.line1.set_data(self.xvalues, self.yvalues)
               # self.ax1.set_xlim(0, a+1)
           # except ValueError:
          #      pass
        #else:
         #   pass
    #def ani_widget1(self):

     #   self.ani1 = animation.FuncAnimation(self.fig1, self.animate1, interval=100, blit=False)
       # self.canvas2.show()
      #  self.ser.reset_input_buffer()



#----------Finaliza la clase que alberga la Interfaz
if __name__ == '__main__':
   mi_interfaz = InterfazShield()
