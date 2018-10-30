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
        self.fenetre.title("Modèle SIRS")
        Frame.__init__(self, self.fenetre, width=500, height=700, **kwargs)
        
        label1 = Label(self.fenetre, text="")
        label1.pack()
        
        self.temps = Scale(self.fenetre, orient='horizontal', from_=0, to=5000,
                       resolution=10, tickinterval=10, length=700,
                       label="Entrez la durée de l'expérience : ")
        self.temps.pack()
        self.temps.set(100)
        
        self.dureeImun = Scale(self.fenetre, orient='horizontal', from_=0, to=.2,
                       resolution=.01, tickinterval=.01, length=700,
                       label="Entrez le taux de durée de l'immunité : ")
        self.dureeImun.pack()
        self.dureeImun.set(0.1)
        
        self.infect = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=700,
                       label="Entrez le pourcentage de personnes suceptibles d'etre infectees (0 - 1) : ")
        self.infect.pack()
        self.infect.set(0.5)
        
        self.tInfect = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=700,
                       label="Entrez le taux d'infection (0 - 1) : ")
        self.tInfect.pack()
        self.tInfect.set(0.5)
        
        self.tGuerison = Scale(self.fenetre, orient='horizontal', from_=0, to=.2,
                       resolution=.01, tickinterval=.01, length=700,
                       label="Entrez le taux de guérison (0 - 1) : ")
        self.tGuerison.pack()
        self.tGuerison.set(0.1)
        
        boutonValider = Button(self.fenetre, text="Valider", command= lambda: self.SEIR(self.infect.get(),self.tInfect.get(),self.tGuerison.get(), self.dureeImun.get(), self.temps.get()))
        boutonValider.pack()
    
    
    def SEIR(self, infectee, tInfection, tGuerison, tDureeImun, time):
    
        plt.clf()
        popInfectee = float(infectee)
        
        TEMPS = time
        
        tauxInfection = float(tInfection)
        
        #nombre jours durant lequel une personne reste infecte
        tauxGuerison = float(tGuerison)
    
        popTotale = 500
        
        
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
            popSuceptible = popSuceptible - (tauxInfection * popSuceptible * popInfectee/popTotale) + tDureeImun*popRetablie#/popTotale
            popS.append(popSuceptible)
            
            popInfectee = popInfectee + ((tauxInfection * popS[i-1] * popInfectee/popTotale) - (tauxGuerison * popInfectee))
            popI.append(popInfectee)
            
            #popSuceptible = 0
            #popInfectee = 0
            
            popRetablie = popRetablie + tauxGuerison * popI[i-1] - tDureeImun*popR[i-1]#/popTotale
            #popRetablie = popRetablie + tauxGuerison * 0 - tDureeImun*popRetablie/popTotale
            popR.append(popRetablie)
            
            popT.append(popSuceptible + popInfectee + popRetablie)
            
            
        for i in range(TEMPS):
            print("S : " + str(popS[i]))
            print("I : " + str(popI[i]))
            print("R : " + str(popR[i]))
            print("Population totale : " + str(popT[i]))
            print("********************")
            
        plt.title("Simulation SIRS")
        plt.plot(temps, popS,label='Population Susceptible')
        plt.plot(temps, popI,label='Population Infectée')
        plt.plot(temps, popR, label='Population Rétablie')
        plt.plot(temps, popT, label='Population Totale')
        plt.legend(loc='upper right');
        plt.show()
    
        