# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:27:57 2020

@author: 
    Jonathan Edgardo Castelo López
    Sebastián Eudave Patiño
    Erick Emmanuel Gutierrez Jiménez
    Alejandro Pérez Velasco
    
    ICI 7mo
    
    Automatas II
    
    Porfesor: Francisco Javier Ornelas Zapata
    
    Programa triángulo de Sierpinski AC
"""
import random
        
#Función que determina si el automata celular será 0 o 1
def AutomataCelular(tamV,vecI,pos):
    tamV = int(tamV)
    if pos == 0:
        if vecI[0]+vecI[1] == 1:
            return 1
        else:
            return 0
    if pos == tamV-1:
        if vecI[tamV-2]+vecI[tamV-1] == 1:
            return 1
        else:
            return 0
    if vecI[pos-1]+vecI[pos]+vecI[pos+1] == 1:
        return 1
    else:
        return 0
    
    
#Programa principal
def main():
    numI = 30
    while True:
        try:
            #Se define el tamaño del vector inicial
            tamV = int(input("Tamaño del vector inicial: "))
            if tamV < 2:
                print("Introduce un número mayor a 1 por favor")
            else:
                break
        except:
            print("Introduce un número entero por favor")
    vecI = []
    
    #De manera aleatoria se llena el vector inicial
    for i in range(int(tamV)):
        vecI.append(random.randint(0, 1))
        
    #Se crean los nuevos vectores con la variable numI como crterio de paro
    for i in range(numI):
        vecN = []
        print(vecI)
        #Se produce el nuevo vector 
        for j in range(int(tamV)):
            vecN.append(AutomataCelular(tamV,vecI,j))
        vecI = vecN
            
            
main()