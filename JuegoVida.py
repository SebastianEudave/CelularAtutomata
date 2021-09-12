# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:50:14 2020

@author: 
    Jonathan Edgardo Castelo López
    Sebastián Eudave Patiño
    Erick Emmanuel Gutierrez Jiménez
    Alejandro Pérez Velasco
    
    ICI 7mo
    
    Automatas II
    
    Porfesor: Francisco Javier Ornelas Zapata
    
    Programa Juego de la vida
"""
import random
        
#Función que determina si el automata celular será 0 o 1
def AutomataCelular(tamV,tamVF,vecI,j,k):
    suma = 0
    if j != 0:
        suma += vecI[j-1][k]
        if k!= 0:
            suma += vecI[j-1][k-1]
        if k != tamV-1:
            suma += vecI[j-1][k+1]
    if j != tamV-1:
        suma += vecI[j+1][k]
        if k!= 0:
            suma += vecI[j+1][k-1]
        if k != tamV-1:
            suma += vecI[j+1][k+1]
    if k != 0:
        suma += vecI[j][k-1]
    if k != tamVF-1:
        suma += vecI[j][k+1]
    if suma == 3:
        return 1
    elif suma == 2 and vecI[j][k] == 1:
        return 1
    elif suma < 3:
        return 0
    elif suma > 3 :
        return 0
    
    
def Imprimir(vecI,tamV,tamVF,numI):
    print("\n")
    print("Juego en el instante %i " %numI)
    for i in range(tamV):
        stri = ' '
        for j in range(tamVF):
            stri += str(vecI[i][j]) + ' '
        print(stri)

#Programa principal
def main():
    numI = 30
    #Se define el tamaño del tablero
    while True:
        try:
            
            tamV = int(input("Número de columnas para el juego: "))
            if tamV < 2:
                print("Introduce un número mayor a 1 por favor")
            else:
                break
        except:
            print("Introduce un número entero por favor")
    while True:
        try:
            tamVF = int(input("Número de filas en el juego: "))
            if tamVF < 2:
                print("Introduce un número mayor a 1 por favor")
            else:
                break
        except:
            print("Introduce un número entero por favor")
    vecI = []
    
    #De manera aleatoria se llena el tablero
    for i in range(tamV):
        fila = []
        for j in range(tamVF):
            fila.append(random.randint(0, 1))
        vecI.append(fila)
        
    #Se crean los nuevos tableros con la variable numI como crterio de paro, que indica los instantes a procesar
    for i in range(numI):
        vecN = []
        Imprimir(vecI,tamV,tamVF,i)
        #Se produce el nuevo tablero 
        for j in range(tamV):
            fila = []
            for k in range(tamVF):
                fila.append(AutomataCelular(tamV,tamVF,vecI,j,k))
            vecN.append(fila)
        vecI = vecN
            
            
main()