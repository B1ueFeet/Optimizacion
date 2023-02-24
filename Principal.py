import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import re
import ProgramacionLineal as pl


def hallar_numericos(s):
  ##verifica si existen las x e y 
  if 'x' in s and 'y' in s:
    ##Separa los numeros de un str
    s_numeric = [float(s) for s in re.findall(r'-?\d+\.?\d*', s)]
    #ORDENA LOS VALORES DE X E Y
    if s.find('x') > s.find('y'):
      s_numeric = list(reversed(s_numeric))
    return s_numeric
  else:
    print('Ingrese un string valido')
    return None, None
# Crear la ventana principal
root = tk.Tk()
# Maximizar la ventana
root.state("zoomed")
#root.geometry("400x300")

#Crear lo que se usara en la parte 1
lst_z = []
lst_r1 = []
lst_r2 = []
lst_r3 = []
intervalo_z1 = []
intervalo_z2 = []
intervalo_r1 = []
intervalo_r2 = []
intervalo_r3 = []
punto_optimo = []
z_optimo = 0.
minimax = tk.BooleanVar()


# Crear un notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='true')

# Crear la pestaña 1
parte_uno = ttk.Frame(notebook)
notebook.add(parte_uno, text='Parte     Uno')

# Crear la pestaña 2
parte_dos = ttk.Frame(notebook)
notebook.add(parte_dos, text='Parte Dos')
# crear varios frames
frame_datos = tk.Frame(parte_uno, bg='blue', bd=5)
frame_datos2 = tk.Frame(parte_dos, bg='blue', bd=5)
frame_grafica = tk.Frame(parte_uno, bg='red', bd=5)
frame_grafica2 = tk.Frame(parte_dos, bg='red', bd=5)
frame_deslizadores = tk.Frame(parte_uno, bg='green', bd=5)

# para el frame de ingreso de datos
tk.Label(frame_datos, text="Ingrese los datos, luego presione el Boton resolver").grid(sticky= 'W',padx=5,row=0, column=0, columnspan=2)
tk.Label(frame_datos, text="Z: ").grid(sticky= 'E',padx=5,row=1, column=0)
tk.Label(frame_datos, text="Restriccion 1: ").grid(sticky= 'E',padx=5,row=2, column=0)
tk.Label(frame_datos, text="Restriccion 2: ").grid(sticky= 'E',padx=5,row=3, column=0)
tk.Label(frame_datos, text="Restriccion 3: ").grid(sticky= 'E',padx=5,row=4, column=0)

tk.Label(frame_datos2, text="Ingrese los datos, luego presione el Boton Calcular").grid(sticky= 'W',padx=5,row=0, column=0, columnspan=2)
tk.Label(frame_datos2, text="Funcion").grid(sticky= 'E',padx=5,row=1, column=0)
tk.Label(frame_datos2, text="Error").grid(sticky= 'E',padx=5,row=2, column=0)

ent_Z = tk.Entry(frame_datos, width=40)
ent_r1 = tk.Entry(frame_datos, width=40)
ent_r2 = tk.Entry(frame_datos, width=40)
ent_r3 = tk.Entry(frame_datos, width=40)

ent_Z.grid(padx=5, row=1, column=1)
ent_r1.grid(padx=5, row=2, column=1)
ent_r2.grid(padx=5, row=3, column=1)
ent_r3.grid(padx=5, row=4, column=1)

ent_Z.insert(0,"2x + 3y")
ent_r1.insert(0,"10x +5y <= 600")
ent_r2.insert(0,"6x + 20y <=600")
ent_r3.insert(0,"8x + 10y <= 600")

ent_polinomio = tk.Entry(frame_datos2, width=40)
ent_error = tk.Entry(frame_datos2, width=40)

ent_polinomio.grid(padx=5, row=1, column=1)
ent_error.grid(padx=5, row=2, column=1)

ent_polinomio.insert(0,"2x + 3y")
ent_error.insert(0,"10x +5y <= 600")

maximizar = tk.Checkbutton(frame_datos, text="Maximizar: False\nMinimizar: True", variable=minimax)
maximizar.grid(padx=5,pady=10, row=5, column=0)



btn_resolver = tk.Button(frame_datos,text="Resolver", width=40 )
btn_resolver.grid(padx=5, pady=10, row=6, column=0, columnspan=2)


tk.Label(frame_deslizadores, text="Se obtuvieron los siguientes resultados: ").grid(sticky= 'W',padx=5,row=0, column=0, columnspan=2)
tk.Label(frame_deslizadores, text="Z optimo: {}".format(z_optimo)).grid(sticky= 'W',padx=5,row=1, column=0)
tk.Label(frame_deslizadores, text="Punto optimo {}".format(punto_optimo)).grid(sticky= 'W',padx=5,row=2, column=0)
tk.Label(frame_deslizadores, text="Analisis de Sensibilidad").grid(sticky= 'W',padx=5,pady=10,row=3, column=0, columnspan=2)

# Optimalidad
sld_z1 = tk.Scale(frame_deslizadores, from_=0, to=10, orient=tk.HORIZONTAL,length=330)
sld_z1.grid(sticky= 'W',   padx=5,row=5, column=0, columnspan=2)
sld_z2 = tk.Scale(frame_deslizadores, from_=0, to=10, orient=tk.HORIZONTAL,length=330)
sld_z2.grid(sticky= 'W',   padx=5,row=7, column=0, columnspan=2)
# Factibilidad
tk.Label(frame_deslizadores, text="Intervalo Factibilidad de R1: {}".format(intervalo_r1)).grid(sticky= 'W',padx=5,row=8, column=0, columnspan=2)
sld_r1 = tk.Scale(frame_deslizadores, from_=0, to=10, orient=tk.HORIZONTAL,length=330)
sld_r1.grid(sticky= 'W',    padx=5,row=9, column=0, columnspan=2)
tk.Label(frame_deslizadores, text="Intervalo Factibilidad de R2: {}".format(intervalo_r2)).grid(sticky= 'W',padx=5,row=10, column=0, columnspan=2)
sld_r2 = tk.Scale(frame_deslizadores, from_=0, to=10, orient=tk.HORIZONTAL,length=330)
sld_r2.grid(sticky= 'W',    padx=5,row=11, column=0, columnspan=2)
tk.Label(frame_deslizadores, text="Intervalo Factibilidad de R3: {}".format(intervalo_r3)).grid(sticky= 'W',padx=5,row=12, column=0, columnspan=2)
sld_r3 = tk.Scale(frame_deslizadores, from_=0, to=10, orient=tk.HORIZONTAL,length=330)
sld_r3.grid(sticky= 'W',    padx=5,row=13, column=0, columnspan=2)

valor=2

fig = Figure(figsize=(6, 4), dpi=150)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0, sticky= 'W', rowspan=2, columnspan=2)



# Configurar la disposición del frame en la ventana
frame_datos.grid(row=0, column=0,sticky= 'N')
frame_datos2.grid(row=0, column=0,sticky= 'N')
frame_grafica.grid(row=0, column=1, sticky= 'N', rowspan=2, pady= 50, padx= 20)
frame_grafica2.grid(row=0, column=1, sticky= 'N', rowspan=2, pady= 50, padx= 20)
frame_deslizadores.grid(row=1, column=0, sticky='N')


def actualizar_grafico():
    global sld_z2,sld_z1,canvas,fig

    z= hallar_numericos(ent_Z.get())
    r1 = hallar_numericos(ent_r1.get())
    r2 = hallar_numericos(ent_r2.get())
    r3 = hallar_numericos(ent_r3.get())
    print('aqui se actualiza el grafico')
    z1_value = tk.DoubleVar()
    z2_value = tk.DoubleVar()
    r1_value = tk.DoubleVar()
    r2_value = tk.DoubleVar()
    r3_value = tk.DoubleVar()

    def update_graph(*args):
        ax.clear()
                
        z1 = z1_value.get()
        z2 = z2_value.get()
        R1 = r1_value.get()
        R2 = r2_value.get()
        R3 = r3_value.get()

        lst_z_copy = lst_z[:]
        lst_r1_copy = lst_r1[:]
        lst_r2_copy = lst_r2 [:]
        lst_r3_copy = lst_r3 [:]
        
        lst_z_copy[0] = z1
        lst_z_copy[1] = z2
        lst_r1_copy[2] = R1
        lst_r2_copy[2] = R2
        lst_r3_copy[2] = R3
        todos = get_values(lst_z_copy,lst_r1_copy,lst_r2_copy,lst_r3_copy)
        # Aquí se hace la actualización de la gráfica
        # Para este ejemplo, se grafica una función seno
        t = np.linspace(0, 100, 100)
        s0 = (todos[0] - z1*t)/z2
        s1 = (R1 - r1[0] * x) / r1[1]
        s2 = (R2 - r2[0] * x) / r2[1]
        s3 = (R3 - r3[0] * x) / r3[1]
        ax.clear()
        ax.plot(t, s0, label= 'Z: ', color='red')
        ax.plot(t, s1, label= 'R1: ', color='lightskyblue')
        ax.plot(t, s2, label= 'R2: ', color='mediumorchid')
        ax.plot(t, s3, label= 'R3: ', color='yellowgreen')
        if minimax.get():
            ax.fill_between(t,  s1, color='lightskyblue', alpha=1.00)
            ax.fill_between(t,  s2, color='mediumorchid', alpha=0.70)
            ax.fill_between(t,  s3, color='yellowgreen',  alpha=0.40) 
        else:
            ax.fill_between(t,  s1, np.max(y1), color='lightskyblue', alpha=1.00)
            ax.fill_between(t,  s2, np.max(y2), color='mediumorchid', alpha=0.70)
            ax.fill_between(t,  s3, np.max(y3), color='yellowgreen',  alpha=0.40) 
        ax.set_xlim(0, None)
        ax.set_ylim(0, None)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Modelo de Programación Lineal')
        ax.legend()
        ax.plot(todos[1][0], todos[1][1], 'ro')
        canvas.draw()
        
        

        # Graficar las restricciones y la región de factibilidad
        
    x = np.linspace(0, 100, 100)
    y0= (z_optimo - z[0]*x)/z[1]
    y1 = (r1[2] - r1[0] * x) / r1[1]
    y2 = (r2[2] - r2[0] * x) / r2[1]
    y3 = (r3[2] - r3[0] * x) / r3[1]

    ax = fig.add_subplot()
    ax.clear()
    ax.plot(x, y0, label= 'Z: ', color='red')
    ax.plot(x, y1, label= 'R1: ', color='lightskyblue')
    ax.plot(x, y2, label= 'R2: ', color='mediumorchid')
    ax.plot(x, y3, label= 'R3: ', color='yellowgreen')
    if minimax.get():
        ax.fill_between(x,  y1, color='lightskyblue', alpha=1.00)
        ax.fill_between(x,  y2, color='mediumorchid', alpha=0.70)
        ax.fill_between(x,  y3, color='yellowgreen',  alpha=0.40) 
    else:
        ax.fill_between(x,  y1, np.max(y1), color='lightskyblue', alpha=1.00)
        ax.fill_between(x,  y2, np.max(y2), color='mediumorchid', alpha=0.70)
        ax.fill_between(x,  y3, np.max(y3), color='yellowgreen',  alpha=0.40) 
    ax.set_xlim(0, None)
    ax.set_ylim(0, None)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Modelo de Programación Lineal')
    ax.legend()
    ax.plot(punto_optimo[0], punto_optimo[1], 'ro')
    
    canvas.draw()

    sld_z1.config(from_=intervalo_z1[0], to=intervalo_z1[1], resolution=0.01, variable=z1_value,
         orient=tk.HORIZONTAL, label="Intervalo Optimalidad de z1: {}".format(intervalo_z1),
         command=update_graph)
    sld_z2.config(from_=intervalo_z2[0], to=intervalo_z2[1], resolution=0.01, variable=z2_value,
         orient=tk.HORIZONTAL, label="Intervalo Optimalidad de z2: {}".format(intervalo_z2),
         command=update_graph)


    sld_r1.config(from_= intervalo_r1[0], to=intervalo_r1[1], resolution=0.01, variable=r1_value,
         orient=tk.HORIZONTAL, label="Intervalo Factibilidad de R1: {}".format(intervalo_r1),
         command=update_graph)
    sld_r2.config(from_=intervalo_r2[0], to=intervalo_r2[1], resolution=0.01, variable=r2_value,
         orient=tk.HORIZONTAL, label="Intervalo Factibilidad de z2: {}".format(intervalo_r2),
         command=update_graph)
    sld_r3.config(from_=intervalo_r3[0], to=intervalo_r3[1], resolution=0.01, variable=r3_value,
         orient=tk.HORIZONTAL, label="Intervalo Factibilidad de z1: {}".format(intervalo_r3),
         command=update_graph)
    
    sld_z1.set(z[0])
    sld_z2.set(z[1])

    sld_r1.set(r1[2])
    sld_r2.set(r2[2])
    sld_r3.set(r3[2])

def asignar_valores():
    global z_optimo, punto_optimo, intervalo_r1, intervalo_r2, intervalo_r3, intervalo_z1, intervalo_z2
    z_optimo, punto_optimo,dual, optimalidad, factibilidad =get_values(lst_z,lst_r1,lst_r2,lst_r3)
    intervalo_z1= optimalidad[0]
    intervalo_z2 = optimalidad[1]
    intervalo_r1= factibilidad[0]
    intervalo_r2 = factibilidad[1]
    intervalo_r3 = factibilidad[2]

def get_values(z, r1, r2, r3 ):
    problema = pl.Programacion_lineal(z,r1,r2,r3, minimax.get())
    z_optimo , punto_optimo = problema.get_optimo()
    dual, optimalidad, factibilidad = problema.get_intervalos()
    return z_optimo, punto_optimo, dual, optimalidad, factibilidad

def resolver():
    global lst_z,lst_r1,lst_r2,lst_r3, fig
    fig.clear()
    lst_z = hallar_numericos(ent_Z.get())
    lst_r1 = hallar_numericos(ent_r1.get())
    lst_r2 = hallar_numericos(ent_r2.get())
    lst_r3 = hallar_numericos(ent_r3.get())
    print('**********************************************************************++')
    print(lst_r1)
    print('**********************************************************************++')
    asignar_valores()
    actualizar_grafico()

btn_resolver.config(command= resolver)
# Iniciar el loop principal
root.mainloop()


