#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:40:14 2020




@author: pereiragama
"""
import matplotlib.pyplot as plt
import random
def generateRandomCoordinates(tailleMatrix,numberCities):
    
    tab=set()
    
    while len(tab)<numberCities:
        i = random.randint(0,tailleMatrix)
        
        j = random.randint(0,tailleMatrix)
        
        if (i,j) not in tab:
            tab.add((i,j))
    
    return tab
    
    
    

def generateRandomPopulation(populationSize,cities):
    Dico= {}
    
    
    start= cities[0]
    alea = cities[1:]

    for i in range(populationSize):

        random.shuffle(alea)#melange array index 1:end
        
        alea.insert(0,start) # add starting point
        
        
        Dico[i+1]=(alea)

        alea=cities[1:]

        
    return Dico



def showPath(initPop):
    """
    for route in initPop:
        chemin=""
        for city in route:
            chemin+=city.repr__()+"--> "
            
        print(chemin)
    """
    for k,v in initPop.items():
        chemin=""
        for city in v:
            chemin+=city.repr__()+"--> "
            
        print(chemin)


def showPathList(L):
    chmein=""
    for c in L:
        chmein+=c.repr__()+"---> "
        
    print(chmein)
        
   
    
def averageDic(L):
    sumFit=0
    for k,v in L:
        sumFit+=v
    #print(">>>>The average fitness of pop is :",sumFit/len(L))
    return 1/(sumFit/len(L))


def swap(ind1,ind2,L):
    tmp =L[ind1]
    
    L[ind1]= L[ind2]
    L[ind2]=tmp
    
    return L

def plot_2_Graph(listX, listY,listZ , titleX, titleY,titleZ=None):
    
    """AFFICHAGE PLOT"""
    plt.plot(listX, listY)
    plt.plot(listX, listZ)
    plt.xlabel(titleX)
    plt.ylabel(titleY)
    
    plt.title("Distance en fonction des générations (orange: best candidate evol / blue: average pop")    
    plt.show()
    
def plot_1_Graph(listX, listY, titleX, titleY):
    
    """AFFICHAGE PLOT"""
    plt.plot(listX, listY)
    
    plt.xlabel(titleX)
    plt.ylabel(titleY)

    plt.show()
    
