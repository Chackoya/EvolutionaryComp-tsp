# -*- coding: utf-8 -*-
"""
Evolutionary Computation: TSP
Algumas partes mais tecnicas foram inspiradas pelo artigo (objetivo era so de me ver em pratica algumas noçoes(selection;mutation;crossover etc) 
e manipular alguns parametros))

https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35

"""
import geneticAlgo
import utilsEC

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
    tabCities.append(geneticAlgo.City(c[0],c[1]))



aff=""
for city in tabCities:
    aff=aff+city.repr__()+" "
#print("Les villes sont: ",aff)
#print()


Mapa = geneticAlgo.Map(N,tabCities)
Mapa.initCities()
#Mapa.showMap()



#Initial Population of paths: initpop : Dictionnary
initPop= utilsEC.generateRandomPopulation(sizePop, tabCities )

#print("PATHS:",initPop)
#utilsEC.showPath(initPop)
print("START OF EVOL ALGO: ")
ranking = geneticAlgo.rankingPaths(initPop)
utilsEC.averageDic(ranking)    
"""VERIF STAT DEBUT"""
geneticAlgo.checkStat(ranking,eliteSize)

print()


#LOOP CONDITION x GENERATIONS:

for i in range(numberGenerations):
    #Select parents
    #print(">>>On regarde mnt la selection des parents: ")
    
    parents=geneticAlgo.selection(ranking,eliteSize)
    #On a mnt les fils:
    
    fils_crossOver=geneticAlgo.matingPar(parents,initPop,eliteSize)
    
    #On procede a la "Survivor selection" remplacer les faibles :
    
    weakest=ranking[-len(fils_crossOver):]

    for fit in weakest:
        #print("Fit:",fit," and fitness:", initPop[fit[0]])
        
        #utilsEC.showPathList(initPop[fit[0]])
        fils = fils_crossOver.pop()
        initPop[fit[0]]= fils
        
    #utilsEC.showPath(initPop)
    ranking=(geneticAlgo.rankingPaths(initPop))
    
    """Mutation part:"""
    geneticAlgo.mutationPopulation(initPop,mutation_rate)
    
    
    plotX_generations.append(i)
    plotY_average_fitness.append(utilsEC.averageDic(ranking))
    plotZ_bestFIT.append(1/(ranking[0][1]))
    
print()
"""VERIF STAT END"""
geneticAlgo.checkStat(ranking,eliteSize)
print(len(plotX_generations), len(plotY_average_fitness),len(plotZ_bestFIT))
utilsEC.averageDic(ranking)    

utilsEC.plot_2_Graph(plotX_generations,plotY_average_fitness,plotZ_bestFIT,"Generations","Distance")
#utilsEC.plot_1_Graph(plotX_generations,plotY_average_fitness,"Generations","Distance")