# -*- coding: utf-8 -*-
"""PL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TktKLbuOSRbkksFteb8HYv7qE7rHQnPW
"""

import numpy as np
import matplotlib.pyplot as plt
import re
import decimal

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

class Programacion_lineal():
  def __init__(self, z,r1,r2,r3, min_max):
    ## DEFINICION DE CONSTANTES
    ## PARA Z
    self.z = list(z )
    ## PARA R1
    self.r1 = list(r1)
    ## PARA R2
    self.r2 = list(r2)
    ## PARA R3
    self.r3 = list(r3)
    ##Para las soluciones
    self.optimos = {}
    ## True = minimizacion False = maximizacion
    self.min_max = min_max


  def evaluar_z(self, punto):
    return self.z[0]* punto[0] + self.z[1]* punto[1]

  def evaluar_r(self, R, punto):
    print('Evaluando {}'.format(self.imprimir_ecuacion(R)) )
    primer_miembro = R[0]*punto[0] + R[1]*punto[1]
    if self.min_max:
      condicion = (primer_miembro <= R[2])
    else:
      condicion = (primer_miembro >= R[2])
    ##Evaluacion de la Restriccion
    if condicion:
      return True
    return False

  def graficar(self, str1, str2, str3):
    x = np.linspace(0, 100, 100)
    y1 = (self.r1[2] - self.r1[0] * x) / self.r1[1]
    y2 = (self.r2[2] - self.r2[0] * x) / self.r2[1]
    y3 = (self.r3[2] - self.r3[0] * x) / self.r3[1]
    

    # Graficar las restricciones y la región de factibilidad
    fig, ax = plt.subplots()
    ax.plot(x, y1, label= 'R1: ' + str1, color='lightskyblue')
    ax.plot(x, y2, label= 'R2: ' + str2, color='mediumorchid')
    ax.plot(x, y3, label= 'R3: ' + str3, color='yellowgreen')
    if self.min_max:
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

    # Agregar el punto óptimo a la gráfica
    ax.plot(self.punto[0], self.punto[1], 'ro')

    plt.show()
  
  def interseccion(self, R1, R2):
    print('Encontrando Puntos de Interseccion')

    a1 = R1[0]
    b1 = R1[1]
    c1 = R1[2]
 
    a2 = R2[0]
    b2 = R2[1]
    c2 = R2[2]

    print(self.imprimir_ecuacion(R1))
    print(self.imprimir_ecuacion(R2))
     
    numerador_y = a2*c1 - a1*c2
    denominador_y = a2*b1 - a1*b2
 
    # método ce cálculo de la posición de rectas:
    paralelas = a1*b2 == a2*b1
    if paralelas:
      coincidentes = a1*c2 == a2*c1
      if coincidentes:
        print('Rectas coincidentes')
      else:
        print('Rectas paralelas')
    else:
    # son secantes. calculo el punto de intersección
      if a1 == 0:
        y = c1/b1
        x = (c2-b2*y)/a2
      else:
        y = numerador_y/denominador_y
        x = (c1-b1*y)/a1
 
      print('Punto intersección: (%s, %s)' % (x, y))
      return (x,y)
  

  def evaluar_puntos(self):
    print('Evaluando')
    for p in self.obtener_puntos():
      print('Esta dentro del for en el punto {}'.format(p))
      if (self.evaluar_r(self.r1,p) and self.evaluar_r(self.r2,p) and self.evaluar_r(self.r3,p)):
        print('va agregar punto {}'.format(p))
        self.optimos[self.evaluar_z(p)] = p

  def get_optimo(self):
    self.evaluar_puntos()
    print(self.optimos)
    dict_ordenado = sorted(self.optimos.keys())
    print(dict_ordenado)
    if self.min_max:
      self.z_optimo = max(dict_ordenado)
      self.punto = self.optimos[max(dict_ordenado)]
    else:
      self.z_optimo = min(dict_ordenado)
      self.punto = self.optimos[min(dict_ordenado)]
    print('z optimo: {} en el punto {}'.format(self.z_optimo, self.punto))
    return self.z_optimo, self.punto

  def imprimir_ecuacion(self, R):
    string = ''
    if R[0] != 0:
        string += '%sx' % R[0]
    if R[1] > 0:
        string += ' + %sy ' % R[1]
    elif R[1] < 0:
        string += ' %sy ' % R[1]
    string += ' = %s' % R[2]
    return string

  def interseccion_ejes(self, R):
    print('Interseccion con los ejes')
    a = R[0]
    b = R[1]
    c = R[2]
    lista = []

    print(self.imprimir_ecuacion(R))
    y = 0
    x = (c)/a
    lista.append((x,y))

    x = 0
    y = c/b
    lista.append((x,y))

    print(lista)

    return lista

  def obtener_puntos(self):
    puntos = self.interseccion_ejes(self.r1) + self.interseccion_ejes(self.r2) + self.interseccion_ejes(self.r3)
    puntos.append(self.interseccion(self.r1,self.r2)) 
    puntos.append(self.interseccion(self.r1,self.r3))
    puntos.append(self.interseccion(self.r2,self.r3))
    print('\n*********************** Todos los puntos****************')
    print(puntos)
    return puntos   

  def restaurar(self):
    self.optimos = self.optimo_antiguo
    self.punto = self.punto_antiguo
    self.r1[2]= self.resticciones_antiguo[0]
    self.r2[2]= self.resticciones_antiguo[1]
    self.r3[2]= self.resticciones_antiguo[2]
    self.optimos = {}

  def bateria(self):
    self.optimo_antiguo = self.z_optimo
    self.punto_antiguo = self.punto
    self.resticciones_antiguo = [self.r1[2], self.r2[2], self.r3[2]]
    self.optimos_antiguos = self.optimos

  def get_dual(self):
    
    self.bateria()
    self.duales = []
    self.optimos = {}
    print(self.optimos)
    ##R1
    self.r1[2] +=1
    optimo_dual, punto_dual = self.get_optimo()
    self.duales.append((optimo_dual-self.optimo_antiguo))
    self.restaurar()
    ##R2
    self.r2[2]+=1
    optimo_dual, punto_dual = self.get_optimo()
    self.duales.append((optimo_dual-self.optimo_antiguo))
    self.restaurar()
    ##R3
    self.r3[2]+=1
    optimo_dual, punto_dual = self.get_optimo()
    self.duales.append((optimo_dual-self.optimo_antiguo))
    self.restaurar()

    return self.duales
  
  def encontrar_rectas(self):
    intersecciones = [self.interseccion(self.r1,self.r2), self.interseccion(self.r1,self.r3), self.interseccion(self.r2,self.r3)]
    rectas = [(self.r1,self.r2),(self.r1,self.r3), (self.r2,self.r3)]
    rectas_sin_u = [self.r3, self.r2, self.r1]
    for i, interseccion,  in enumerate(intersecciones):
      print('************************* el pinche punto **********************')
      print(self.punto , interseccion)
      if self.punto == interseccion:
        print('************************* sin usar **********************')
        print(rectas_sin_u[i])
        return [rectas[i], rectas_sin_u[i]]
    
  def optimalidad(self):
    self.int_optimalidad = []
    rectas=self.encontrar_rectas()[0]
    print('**************************** las pinches rectas  ***************************************+')
    print(rectas)
    self.int_optimalidad.append(self.obtener_intervalo_o(rectas[0], rectas[1], self.z[1], 0))
    self.int_optimalidad.append(self.obtener_intervalo_o(rectas[1], rectas[0], self.z[0], 1))
    print('optimalidad: '.format(self.int_optimalidad))
    self.restaurar()
    return self.int_optimalidad
  
  def obtener_intervalo_o(self, R1, R2, zn, op):
    if op==0:
      min= (R1[0]/R1[1]*zn)
      max= (R2[0]/R2[1]*zn)
    else:
      max= (R1[1]/R1[0]*zn)
      min= (R2[1]/R2[0]*zn)
    if (R1[0]/R1[1])<= (R2[0]/R2[1]):
      print('intervalo: {}'.format((min,max)))
      return (min,max)
    else:
      print('intervalo: {}'.format((max,min)))
      return (max,min)


  def obtener_intervalo_f(self, R1, R2 ):
    intersecciones = [self.interseccion_ejes(R1), self.interseccion_ejes(R2)]
    if self.min_max:
      val_x = min(intersecciones[0][0][0], intersecciones[1][0][0])
      val_y = min(intersecciones[0][1][1], intersecciones[1][1][1])
    else:
      val_x = max(intersecciones[0][0][0], intersecciones[1][0][0])
      val_y = max(intersecciones[0][1][1], intersecciones[1][1][1])
    return(val_x, val_y)

  def calcular_restriccion(self, val_x, val_y, R):
    restriccion = R[0]* val_x + R[1] * val_y
    return restriccion 

      
  def factibilidad(self):

      self.int_factibilidad = []

      rectas=self.encontrar_rectas()
      print('**************************** las rectas *****************')
      print(rectas[0], rectas[1])
      intervalo_lim= (self.interseccion_ejes(rectas[0][0]), self.interseccion_ejes(rectas[0][1]))
      intervalo_interseccion = (self.interseccion(rectas[1], rectas[0][0]), self.interseccion(rectas[1], rectas[0][1]))
      print('**************************** esta el perro intervalo limite *****************')
      print(intervalo_lim)

      print('**************************** esta el perro intervalo interseccion *****************')
      print(intervalo_interseccion)
      infinito = 1000
      if rectas[1] == self.r1:
        intervalo = (self.calcular_restriccion(self.punto[0], self.punto[1], rectas[1]) , infinito)
        self.int_factibilidad.append(intervalo)

        intervalo = (self.calcular_restriccion(intervalo_lim[1][1][0], intervalo_lim[1][1][1], rectas[0][0]) , 
                   self.calcular_restriccion(intervalo_interseccion[0][0], intervalo_interseccion[0][1], rectas[0][0]))
        self.int_factibilidad.append(intervalo)

        intervalo = (self.calcular_restriccion(intervalo_lim[0][0][0], intervalo_lim[0][0][1], rectas[0][1]) , 
                   self.calcular_restriccion(intervalo_interseccion[0][0], intervalo_interseccion[0][1], rectas[0][1]))
        self.int_factibilidad.append(intervalo)

      elif rectas[1] == self.r2:
        intervalo = (self.calcular_restriccion(intervalo_lim[1][1][0], intervalo_lim[1][1][1], rectas[0][0]) , 
                   self.calcular_restriccion(intervalo_interseccion[0][0], intervalo_interseccion[0][1], rectas[0][0]))
        self.int_factibilidad.append(intervalo)

        intervalo = (self.calcular_restriccion(self.punto[0], self.punto[1], rectas[1]) , infinito)
        self.int_factibilidad.append(intervalo)

        intervalo = (self.calcular_restriccion(intervalo_lim[0][0][0], intervalo_lim[0][0][1], rectas[0][1]) , 
                   self.calcular_restriccion(intervalo_interseccion[0][0], intervalo_interseccion[0][1], rectas[0][1]))
        self.int_factibilidad.append(intervalo)


      elif rectas[1] == self.r3:
        intervalo = (self.calcular_restriccion(intervalo_lim[1][1][0], intervalo_lim[1][1][1], rectas[0][0]) , 
                   self.calcular_restriccion(intervalo_interseccion[1][0], intervalo_interseccion[1][1], rectas[0][0]))
        self.int_factibilidad.append(intervalo)

        intervalo = (self.calcular_restriccion(intervalo_lim[0][0][0], intervalo_lim[0][0][1], rectas[0][1]) , 
                   self.calcular_restriccion(intervalo_interseccion[0][0], intervalo_interseccion[0][1], rectas[0][1]))
        self.int_factibilidad.append(intervalo)

        intervalo = (self.calcular_restriccion(self.punto[0], self.punto[1], rectas[1]) , infinito)
        self.int_factibilidad.append(intervalo)

      print('************************ el perro intervalo ************************')
      print(self.int_factibilidad)

      
      return self.int_factibilidad

  def get_intervalos(self):
    return self.get_dual(),self.optimalidad(), self.factibilidad()

