'''
Created on 24 sept. 2018

@author: arsen
'''

#bibliotheques
from numpy import *
import matplotlib.pyplot as plt

#entree des parametres

popSuceptible = float(input("Entrez le pourcentage de personnes suceptibles d'etre infectees (0 - 1) : "))
#popInfectee = float(input("Entrez le pourcentage de personnes infectees"))
tauxInfection = float(input("Entrez le taux d'infection : "))
#nombre jours durant lequel une personne reste infecte
tauxGuerison = float(input("Entrez le taux de guerison : "))
popInfectee = (1 - popSuceptible)
popRetablie = 0

temps = []
for i in range(50):
    temps.append(i)
    
popS = []
popI = []
popR = []

popS.append(popSuceptible)
popI.append(popInfectee)
popR.append(popRetablie)

for i in range(49):
    popSuceptible = 1 - (tauxGuerison * popSuceptible * popInfectee)
    popS.append(popSuceptible)    
    popRetablie = 1 - (popInfectee * tauxGuerison)
    popR.append(popRetablie)
    #popInfectee = - popSuceptible - popInfectee / (1/tauxGuerison)
    popInfectee = 1 - (popSuceptible - popRetablie)
    popI.append(popInfectee)

plt.plot(temps, popS)
plt.plot(temps, popI)
plt.plot(temps, popR)
plt.show()

for i in range(50):
    print("S : " + str(popS[i]))
    print("I : " + str(popI[i]))
    print("R : " + str(popR[i]))
    print("********************")
    
    
    
