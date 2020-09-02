# -*- coding: utf-8 -*-
"""
Classes + EA fcts

"""
import utilsEC
import numpy as np
import operator
import pandas as pd
import random
import matplotlib.pyplot as plt
import copy

class Map:
    def __init__(self,taille,cities):
        self.taille= taille
        self.Matrix = [[0 for i in range(taille)] for j in range(taille)] 

        self.cities=cities

    def initCities(self):
        
        i=0
        for c in (self.cities):
            x,y=c.getXY()
            i=i+1
            self.Matrix[x][y]=(i)

    def showMap(self):
        print()
        st="     "
        for j in range(self.taille):
            st=st+str(j)+"  "
        print(st)
        print("--------------------"*2)
        for i in range(self.taille):
            print(i,"|",self.Matrix[i])
        print()   
            
########################################  
    
    
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def getXY(self):
        return (self.x, self.y)
    
    

###########################
class FitEval: #Eval function minimize route distance
    def __init__(self, path):
        self.path=path
        self.distance=0
        self.fitness= 0

        
    def affichePath(self):
        
        chemin=city.repr__()+"--> "
        
        print(chemin)
    def routeDistance(self):
        if self.distance==0:
                
            pathDistance=0
            for i in range(len(self.path)):
                fromCity = self.path[i]
                toCity = None
                
                if i+1< len(self.path):
                    toCity=self.path[i+1]
                else:
                    toCity= self.path[0]
                    
                pathDistance+= fromCity.distance(toCity)
            self.distance=pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness==0:
            self.fitness= 1/ float(self.routeDistance())
        return self.fitness
        
        
                
            
            


def rankingPaths(popPaths):
    
    fitnessRes={}
    for pathID,path in popPaths.items():
        fitnessRes[pathID]=( FitEval(path).routeFitness() )
    
    return sorted(fitnessRes.items(), key = operator.itemgetter(1), reverse = True)
  

def checkStat(popRanked,eliteSize):
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    print(df)
      
def selection(popRanked,eliteSize):
    """
    ELITISM SELECTION
    
    """
    
    tmp = list(popRanked[:eliteSize])
    #print(tmp)
    
    matingParents=[]
    
    for i in range(int(eliteSize//2)):
        tup0=random.choice(tmp)
        tmp.remove(tup0)
        tup1=random.choice(tmp)
        tmp.remove(tup1)
        
        matingParents.append((tup0,tup1))
    
    #print("Here parents:",matingParents)
    return matingParents



    
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    start=parent1[0]
    sublistP1=parent1[1:]
    sublistP2=parent2[1:]
    
    geneA = random.randint(0,len(sublistP1))#int(random.random() * len(parent1))
    geneB = random.randint(0,len(sublistP2))#int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    
    
    endGene = max(geneA, geneB)
      
    for i in range(startGene, endGene):
        
        childP1.append(sublistP1[i])
        
    childP2 = [item for item in sublistP2 if item not in childP1]
      
    child = childP1 + childP2
    child.insert(0, start)

    return child  

def matingPar(listParents,paths,eliteSize):
    """

    """
    
    tmp=[]
    for p1,p2 in (listParents):
        p1_ind=p1[0]
        
        p2_ind=p2[0]
        #utilsEC.showPathList(paths[p1_ind])

        #utilsEC.showPathList(paths[p2_ind])

        
        child = breed(paths[p1_ind],paths[p2_ind])

        #utilsEC.showPathList(child)
        tmp.append(child)

    return tmp #list des fils (crossover)



def mutationPopulation(population , mutation_rate ):
    
    #start = individual_path[0]
    
    #print(start)
    #print("MuTATION")
    #utilsEC.showPath(population)
    #print(population)
    alea = None
    for k,v in population.items():
        alea = random.random()
        
        #print("AVANT V:",alea)
        #utilsEC.showPathList(v)
        if alea <= mutation_rate :
            #print("MUTATION HAPPENED")
            index1 = random.randint(1,len(v)-1)
            
            index2 = random.randint(1,len(v)-1)
            while index1==index2:
                index2= random.randint(1,len(v)-1) 
            utilsEC.swap(index1,index2,v)

        #utilsEC.showPathList(v)
        #print() 
            
        

    
#####################################------------------------##################   
#####MAIN:
""" ### VARIABLES:"""
N=50 #Size matrix NxN
C=35 #numbercity 25
cities= utilsEC.generateRandomCoordinates(tailleMatrix=N-1,numberCities=C)
#print(cities)

mutation_rate=0.1 # 5%
sizePop=100
eliteSize=15
numberGenerations=1000

tabCities=tab=[]

plotX_generations=[]
plotY_average_fitness=[]
plotZ_bestFIT=[]
""" Start:"""

for c in cities:
    #print(c)
    tabCities.append(City(c[0],c[1]))



aff=""
for city in tabCities:
    aff=aff+city.repr__()+" "
#print("Les villes sont: ",aff)
#print()


Mapa = Map(N,tabCities)
Mapa.initCities()
#Mapa.showMap()



#Initial Population of paths: initpop : Dictionnary
initPop= utilsEC.generateRandomPopulation(sizePop, tabCities )

#print("PATHS:",initPop)
#utilsEC.showPath(initPop)
print("START OF EVOL ALGO: ")
ranking = rankingPaths(initPop)
utilsEC.averageDic(ranking)    
"""VERIF STAT DEBUT"""
checkStat(ranking,eliteSize)

print()


#LOOP CONDITION x GENERATIONS:

for i in range(numberGenerations):
    #Select parents
    #print(">>>On regarde mnt la selection des parents: ")
    
    parents=selection(ranking,eliteSize)
    #On a mnt les fils:
    
    fils_crossOver=matingPar(parents,initPop,eliteSize)
    
    #On procede a la "Survivor selection" remplacer les faibles :
    
    weakest=ranking[-len(fils_crossOver):]

    for fit in weakest:
        #print("Fit:",fit," and fitness:", initPop[fit[0]])
        
        #utilsEC.showPathList(initPop[fit[0]])
        fils = fils_crossOver.pop()
        initPop[fit[0]]= fils
        
    #utilsEC.showPath(initPop)
    ranking=(rankingPaths(initPop))
    
    """Mutation part:"""
    mutationPopulation(initPop,mutation_rate)
    
    
    plotX_generations.append(i)
    plotY_average_fitness.append(utilsEC.averageDic(ranking))
    plotZ_bestFIT.append(1/(ranking[0][1]))
    
print()
"""VERIF STAT END"""
checkStat(ranking,eliteSize)
print(len(plotX_generations), len(plotY_average_fitness),len(plotZ_bestFIT))
utilsEC.averageDic(ranking)    

utilsEC.plot_2_Graph(plotX_generations,plotY_average_fitness,plotZ_bestFIT,"Generations","Distance")
#utilsEC.plot_1_Graph(plotX_generations,plotY_average_fitness,"Generations","Distance")