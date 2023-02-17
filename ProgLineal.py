from docplex.mp.model import Model
import numpy as np
import matplotlib.pyplot as plt

class ProgLineal():
    def __init__(self, z,r1,r2,r3):
        print(r3 == None)
        if r3 == None:
            self.g =0
            self.h =0
            self.l3=0
        else:
            self.g =r3[0]
            self.h =r3[1]
            self.l3=r3[2]
        self.a =z[0]
        self.b =z[1]
        self.c =r1[0]
        self.d =r1[1]
        self.l1=r1[2]
        self.e =r2[0]
        self.f =r2[1]
        self.l2=r2[2]
        print('acabo de asignar datos')

    def encontrar_solucion(self, opt):
        print('tratando de resolverlo')
        self.mdl= Model('Optimizacion')
        self.x = self.mdl.continuous_var(name='x')
        self.y = self.mdl.continuous_var(name='y')
        if opt:
            self.mdl.maximize(self.a*self.x + self.b*self.y)
        else:
            self.mdl.maximize(self.a*self.x + self.b*self.y)
        
        self.mdl.add_constraint(self.c*self.x + self.d*self.y <= self.l1 )
        self.mdl.add_constraint(self.e*self.x + self.f*self.y <= self.l2 )
        self.mdl.add_constraint(self.g*self.x + self.h*self.y <= self.l3 )
        self.solution = self.mdl.solve(log_output = True)
        print('acabo de resolver')
        self.solution.display()
        
    def analisis_sensibilidad(self):

        ##precio sombra
        n_const = self.mdl.number_of_constraints
        const = [self.mdl.get_constraint_by_index(i) for i in range(n_const)]
        resticciones = self.mdl.slack_values(const)
        self.precio_sombra = self.mdl.dual_values(const)

        ##optimabilidad
        cpx = self.mdl.get_engine().get_cplex()
        self.optimabilidad = cpx.solution.sensitivity.objective()
        self.factibilidad = cpx.solution.sensitivity.rhs()
        var_list = [self.mdl.get_var_by_name('x'),self.mdl.get_var_by_name('y')]

        ##IMPRESIONES EN CONSOLA

        ##Variables de olgura
        print('\nvariables de olgura')
        for n in range(n_const):
            print('La variable de olgura de la restriccion {} es: {}'.format(str(const[n]), str(resticciones[n])))
        ##Precio sombra
        print('\nPRECIOS SOMBRA')
        for n in range(n_const):
            print('El precio sombra de la restriccion {} es: {}'.format(str(const[n]), str(self.precio_sombra[n])))
        ##optimabilidad
        print('\nOTIMABILIDAD')
        for n in range(len(var_list)):
            print('La variable {}: {}'.format(str(var_list[n]), str(self.optimabilidad[n])))
        ##Factibilidad
        print('\nFACTIBILIDAD')
        for n in range(n_const):
            print('La resticcion {}: {}'.format(str(const[n]), str(self.factibilidad[n])))
        return (self.precio_sombra, self.optimabilidad,self.factibilidad)
    def graficar(self):
        # Obtener los valores óptimos de X y Y
        opt_X = self.solution.get_value(self.x)
        opt_Y = self.solution.get_value(self.y)

        # Definir los puntos de las restricciones
        x = np.linspace(0, 10, 100)
        y1 = (self.l1 - self.c*x)/self.d
        y2 = (self.l2 - self.e*x)/self.f
        y3 = (self.l3 - self.g*x)/self.h
        
        # Graficar las restricciones y la región de factibilidad
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='2*X + Y <= 8')
        ax.plot(x, y2, label='X + 3*Y <= 8')
        ax.fill_between( x, np.maximum(y1, 0), np.minimum(y2, (8 - x)/3), where=(y1 <= y2), alpha=0.2)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Modelo de Programación Lineal')
        ax.legend()
        # Agregar el punto óptimo a la gráfica
        ax.plot(opt_X, opt_Y, 'ro')
        plt.show()
        return plt