'''
Created on 24 sept. 2018

@author: arsen
'''

#bibliotheques
from numpy import *
import matplotlib.pyplot as plt

#entree des parametres

#popSuceptible = float(input("Entrez le pourcentage de personnes suceptibles d'etre infectees (0 - 1) : "))
popInfectee = float(input("Entrez le pourcentage de personnes infectees : "))


tauxInfection = float(input("Entrez le taux d'infection : "))
#nombre jours durant lequel une personne reste infecte
tauxGuerison = float(input("Entrez le taux de guerison : "))
#popInfectee = (1 - popSuceptible)
popTotale = 50


popSuceptible = popTotale - popTotale * popInfectee;
popInfectee = popTotale * popInfectee
popRetablie = 0

temps = []
for i in range(100):
    temps.append(i)
    
popS = []
popI = []
popR = []
popT = []

popS.append(popSuceptible)
popI.append(popInfectee)
popR.append(popRetablie)
popT.append(popSuceptible + popInfectee + popRetablie)

for loop in range(99):
    '''
    #popInfectee = - popSuceptible - popInfectee / (1/tauxGuerison)
    popInfectee = popTotale - (popSuceptible - popRetablie)
    popI.append(popInfectee) 
    popRetablie = (popInfectee * tauxGuerison) + popRetablie
    popR.append(popRetablie)
    popSuceptible = popTotale - (tauxInfection * popSuceptible * (popInfectee/popTotale))
    popS.append(popSuceptible)
    '''
    '''
    popSuceptible =  -tauxInfection * popSuceptible * popInfectee
    popS.append(popSuceptible)
    
    popInfectee = -popSuceptible - (tauxGuerison * popInfectee)
    popI.append(popInfectee)
    
    popRetablie = tauxGuerison * popInfectee
    popR.append(popRetablie)
    '''
    
    popSuceptible = popSuceptible - (tauxInfection * popSuceptible * popInfectee/popTotale)
    popS.append(popSuceptible)
    
    #popInfectee = popInfectee + popSuceptible - (tauxGuerison * popInfectee)
    popInfectee = popInfectee + (tauxInfection * popSuceptible * popInfectee/popTotale) - (tauxGuerison * popInfectee)
    popI.append(popInfectee)
    
    popRetablie = popRetablie + tauxGuerison * popInfectee
    popR.append(popRetablie)
    
    popT.append(popSuceptible + popInfectee + popRetablie)
    
plt.title("Simulation SIR")
plt.plot(temps, popS)
plt.plot(temps, popI)
plt.plot(temps, popR)
plt.plot(temps, popT)
plt.show()

for i in range(100):
    print("S : " + str(popS[i]))
    print("I : " + str(popI[i]))
    print("R : " + str(popR[i]))
    print("Population totale : " + str(popT[i]))
    print("********************")
    
    
    
