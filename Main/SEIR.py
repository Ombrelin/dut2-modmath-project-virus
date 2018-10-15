'''
Created on 9 oct. 2018

@author: arsen
'''

#bibliotheques
from numpy import *
from tkinter import * 
import matplotlib.pyplot as plt


class ModeleSEIR(Frame):
    
    def __init__(self, **kwargs):
        #interface
        self.fenetre = Tk()
        Frame.__init__(self, self.fenetre, width=300, height=500, **kwargs)
        
        label1 = Label(self.fenetre, text="")
        label1.pack()
        
        self.dureeImun = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le taux de durée de l'immunité : ")
        self.dureeImun.pack()
        self.dureeImun.set(0.3)
        
        self.infect = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le pourcentage de personnes suceptibles d'etre infectees (0 - 1) : ")
        self.infect.pack()
        self.infect.set(0.5)
        
        self.tInfect = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le taux d'infection (0 - 1) : ")
        self.tInfect.pack()
        self.tInfect.set(0.5)
        
        self.tGuerison = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le taux de guérison (0 - 1) : ")
        self.tGuerison.pack()
        self.tGuerison.set(0.2)
        
        boutonValider = Button(self.fenetre, text="Valider", command= lambda: self.SEIR(self.infect.get(),self.tInfect.get(),self.tGuerison.get(), self.dureeImun.get()))
        boutonValider.pack()
    
    
    def SEIR(self, infectee, tInfection, tGuerison, tDureeImun):
    
        plt.clf()
        popInfectee = float(infectee)
        
        TEMPS = 1000
        
        tauxInfection = float(tInfection)
        
        #nombre jours durant lequel une personne reste infecte
        tauxGuerison = float(tGuerison)
    
        popTotale = 50
        
        
        popSuceptible = popTotale - popTotale * popInfectee;
        popInfectee = popTotale * popInfectee
        popRetablie = 0
        
        temps = []
        for i in range(TEMPS):
            temps.append(i)
            
        popS = []
        popI = []
        popR = []
        popT = []
        
        popS.append(popSuceptible)
        popI.append(popInfectee)
        popR.append(popRetablie)
        popT.append(popSuceptible + popInfectee + popRetablie)
        
        for i in range(1,TEMPS):
            popSuceptible = popSuceptible - (tauxInfection * popSuceptible * popInfectee/popTotale) + tDureeImun*popRetablie/popTotale
            popS.append(popSuceptible)
            
            popInfectee = popInfectee + ((tauxInfection * popS[i-1] * popInfectee/popTotale) - (tauxGuerison * popInfectee))
            popI.append(popInfectee)
            
            popRetablie = popRetablie + tauxGuerison * popI[i-1] - tDureeImun*popR[i-1]/popTotale
            popR.append(popRetablie)
            
            popT.append(popSuceptible + popInfectee + popRetablie)
            
            
        for i in range(TEMPS):
            print("S : " + str(popS[i]))
            print("I : " + str(popI[i]))
            print("R : " + str(popR[i]))
            print("Population totale : " + str(popT[i]))
            print("********************")
            
        plt.title("Simulation SEIR")
        plt.plot(temps, popS,label='Population Susceptible')
        plt.plot(temps, popI,label='Population Infectée')
        plt.plot(temps, popR, label='Population Rétablie')
        plt.plot(temps, popT, label='Population Totale')
        plt.legend(loc='lower right');
        plt.show()
    
        