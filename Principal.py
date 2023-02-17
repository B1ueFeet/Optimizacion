import tkinter as tk
from tkinter import ttk
import ProgLineal
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

def hallar_numericos(s):
    # verifica si existen las x e y
    if 'x' in s and 'y' in s:
        # Separa los numeros de un str
        s_numeric = [float(s) for s in re.findall(r'-?\d+\.?\d*', s)]
        # ORDENA LOS VALORES DE X E Y
        if s.find('x') > s.find('y'):
            s_numeric = list(reversed(s_numeric))
        return tuple(s_numeric)
    else:
        print('Ingrese un string valido')
        return None


class Parte_Uno(ttk.Frame):
    # Constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Z = ttk.Entry(self)
        self.Z.pack()
        self.R1 = ttk.Entry(self)
        self.R1.pack()
        self.R2 = ttk.Entry(self)
        self.R2.pack()
        self.R3 = ttk.Entry(self)
        self.R3.pack()

        self.resolver = ttk.Button(
            self, text="Resolver", command=self.resolver_simplex)
        self.resolver.pack()

        self.z_optimo = ttk.Label(self)
        self.z_optimo.pack()
        self.precios_sombra = ttk.Label(self)
        self.precios_sombra.pack()
        self.factibilidad = ttk.Label(self)
        self.factibilidad.pack()
        
        self.optimabilidad = ttk.Label(self)
        self.optimabilidad.pack()

        self.fig = Figure(figsize=(10,10), dpi=100)

        canvas = FigureCanvasTkAgg(self.fig)
        

    def resolver_simplex(self):
        print('Resolviendo Problema')
        print(hallar_numericos(self.Z.get()))
        print(hallar_numericos(self.R1.get()))
        print(hallar_numericos(self.R2.get()))
        print(hallar_numericos(self.R3.get()))
        a = ProgLineal.ProgLineal(hallar_numericos(self.Z.get()), hallar_numericos(self.R1.get()),
                                  hallar_numericos(self.R2.get()), hallar_numericos(self.R3.get()))
        a.encontrar_solucion(True)
        b = a.analisis_sensibilidad()
        c=a.graficar

        # self.greet_label["text"] = \ "¡Hola, {}!".format(self.name_entry.get())


class Parte_Dos(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

       

class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Trabajo de Optimizacion")

        self.panel_pestañas = ttk.Notebook(self)

        self.parte_uno = Parte_Uno(self.panel_pestañas)
        self.panel_pestañas.add(
            self.parte_uno, text="Parte Uno", padding=10)

        self.parte_dos = Parte_Dos(self.panel_pestañas)
        self.panel_pestañas.add(
            self.parte_dos, text="Parte Dos", padding=10)

        self.panel_pestañas.pack(padx=10, pady=10)
        self.pack()


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
