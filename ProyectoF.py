# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:31:28 2020

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

#Se codifica una cadena de caracteres en binario
def PalabraBinario(cadena):
    simbolos = 'abcdefghijklmnñopqrstuvwxyz1234 '
    simbolos2 = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,0,1],[0,0,1,1,0],[0,0,1,1,1],[0,1,0,0,0],[0,1,0,0,1],[0,1,0,1,0],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,0,1],[0,1,1,1,0],[0,1,1,1,1],[1,0,0,0,0],[1,0,0,0,1],[1,0,0,1,0],[1,0,0,1,1],[1,0,1,0,0],[1,0,1,0,1],[1,0,1,1,0],[1,0,1,1,1],[1,1,0,0,0],[1,1,0,0,1],[1,1,0,1,0],[1,1,0,1,1],[1,1,1,0,0],[1,1,1,0,1],[1,1,1,1,0],[1,1,1,1,1]]
    nuevaC = []
    for letra in cadena:
        pos = simbolos.find(letra.lower())
        for i in range(5):
            nuevaC.append(simbolos2[pos][i])
    return nuevaC

def BinarioPalabra(cadena):
    simbolos = 'abcdefghijklmnñopqrstuvwxyz1234 '
    simbolos2 = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,0],[0,0,1,0,1],[0,0,1,1,0],[0,0,1,1,1],[0,1,0,0,0],[0,1,0,0,1],[0,1,0,1,0],[0,1,0,1,1],[0,1,1,0,0],[0,1,1,0,1],[0,1,1,1,0],[0,1,1,1,1],[1,0,0,0,0],[1,0,0,0,1],[1,0,0,1,0],[1,0,0,1,1],[1,0,1,0,0],[1,0,1,0,1],[1,0,1,1,0],[1,0,1,1,1],[1,1,0,0,0],[1,1,0,0,1],[1,1,0,1,0],[1,1,0,1,1],[1,1,1,0,0],[1,1,1,0,1],[1,1,1,1,0],[1,1,1,1,1]]
    nuevaC = []
    cont = 0
    temp = []
    for num in cadena:
        temp.append(num)
        cont += 1
        if cont == 5:
            pos = simbolos2.index(temp)
            nuevaC.append(simbolos[pos])
            cont = 0
            temp = []
    return nuevaC
    
#Se derfinen las reglas para las transiciones de estado de las celulas
def Reglas(vecC,pos1,pos2,pos3):
    regla = [1,0,0,0,1,1,1,0]
    if vecC[pos1] == 0 and vecC[pos2] == 0 and vecC[pos3] == 0:
        return regla[0]
    elif vecC[pos1] == 0 and vecC[pos2] == 0 and vecC[pos3] == 1:
        return regla[1]
    elif vecC[pos1] == 0 and vecC[pos2] == 1 and vecC[pos3] == 0:
        return regla[2]
    elif vecC[pos1] == 0 and vecC[pos2] == 1 and vecC[pos3] == 1:
        return regla[3]
    elif vecC[pos1] == 1 and vecC[pos2] == 0 and vecC[pos3] == 0:
        return regla[4]
    elif vecC[pos1] == 1 and vecC[pos2] == 0 and vecC[pos3] == 1:
        return regla[5]
    elif vecC[pos1] == 1 and vecC[pos2] == 1 and vecC[pos3] == 0:
        return regla[6]
    elif vecC[pos1] == 1 and vecC[pos2] == 1 and vecC[pos3] == 1:
        return regla[7]

#Función que determina si el automata celular será 0 o 1
def AutomataCelular(vecC,pos):
    if pos == 0:
        return Reglas(vecC,len(vecC)-1,pos,pos+1)
    elif pos == len(vecC)-1:
        return Reglas(vecC,pos-1,pos,0)
    else:
        return Reglas(vecC,pos-1,pos,pos+1)
    
#Se codifica una cadena con otra cadena y aplicandoles un XOR
def XOR(cadena1,cadena2):
    res = []
    for i in range(len(cadena1)):
        if cadena1[i]==1 ^ cadena2[i]==1:
            res.append(1)
        elif cadena2[i]==1 ^ cadena1[i]==1:
            res.append(1)
        else:
            res.append(0)
    return res
    
#Programa principal
def main():
    cad = str(input("Dame la cadena a codificar: "))
    cadena = PalabraBinario(cad)
    print("Cadena binarizada: ")
    print(cadena)
    print("\n")
    codigo = str(input("Dame la palabra código: "))
    codigo = PalabraBinario(codigo)
    print("Codigo binarizado: ")
    print(codigo)
    print("\n")
    
    numT = random.randint(0,50)
    print("Estado de celula inicial: ")
    print(numT)
    print("\n")
    numI = numT + len(cadena) - 1
    numC = random.randint(0,len(codigo)-1)
    print("Celula inicial escogida: ")
    print(numC)
    print("\n")
    print("Automata Celular: ")
    codigos = []
    for i in range(numI):
        vecN = []
        print(codigo)
        codigos.append(codigo)
        #Se produce el nuevo vector 
        for j in range(len(codigo)):
            vecN.append(AutomataCelular(codigo,j))
        codigo = vecN
    codigos.append(codigo)
    codigo = []
    for i in range(len(cadena)):
        codigo.append(codigos[i+numT][numC])
    print("\n")
    print("Codigo final: ")
    print(codigo)
    print("En caracteres: ")
    c = ''
    print(c.join(BinarioPalabra(codigo)))
    print("\n")
    print("Cadena binarizada: ")
    print(cadena)
    print("Mensaje: ")
    print(cad)
    print("\n")
    
    res = XOR(cadena,codigo)
    print("Cadena codificada: ")
    print(res)
    print("En caracteres: ")
    c = ''
    print(c.join(BinarioPalabra(res)))
    print("\n")
            
main()