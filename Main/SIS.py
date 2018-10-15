'''
Created on 15 oct. 2018

@author: arsen
'''
'''
Created on 24 sept. 2018

@author: arsen
'''

#bibliotheques
from numpy import *
from tkinter import * 
import matplotlib.pyplot as plt


class ModeleSIS(Frame):
    
    def __init__(self, **kwargs):
        #interface
        self.fenetre = Tk()
        self.fenetre.title("Modèle SIS")
        Frame.__init__(self, self.fenetre, width=300, height=500, **kwargs)
        
        label1 = Label(self.fenetre, text="")
        label1.pack()
        
        self.infect = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le pourcentage de personnes suceptibles d'être infectées : ")
        self.infect.pack()
        self.infect.set(0.5)
        
        self.tInfect = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le taux d'infection : ")
        self.tInfect.pack()
        self.tInfect.set(0.5)
        
        self.tGuerison = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le taux de guérison : ")
        self.tGuerison.pack()
        self.tGuerison.set(0.2)
        
        self.tNaissance = Scale(self.fenetre, orient='horizontal', from_=0, to=1,
                       resolution=0.1, tickinterval=0.1, length=350,
                       label="Entrez le taux de naissances : ")
        self.tNaissance.pack()
        self.tNaissance.set(0.2)
        
        boutonValider = Button(self.fenetre, text="Valider", command= lambda: self.SIS(self.infect.get(),self.tInfect.get(),self.tGuerison.get(), self.tNaissance.get()))
        boutonValider.pack()
    
    
    def SIS(self, infectee, tInfection, tGuerison, tNaissance):
    
        plt.clf()
        popInfectee = float(infectee)
        
        
        tauxInfection = float(tInfection)
        
        #nombre jours durant lequel une personne reste infecte
        tauxGuerison = float(tGuerison)
        tauxNaissance = float(tNaissance)
        popTotale = 50
        
        
        popSuceptible = popTotale - popTotale * popInfectee;
        popInfectee = popTotale * popInfectee
        tNG = tauxNaissance+tauxGuerison
        temps = []
        for i in range(100):
            temps.append(i)
            
        popS = []
        popI = []
        popT = []
        
        popS.append(popSuceptible)
        popI.append(popInfectee)
        
        popT.append(popSuceptible + popInfectee)
        
        for i in range(1,100):
            popSuceptible = popSuceptible -((tauxInfection/popTotale)*popSuceptible*popInfectee )+(tNG*popInfectee)
            popS.append(popSuceptible)
            
            popInfectee = popInfectee + ((tauxInfection/popTotale)*popS[i-1]*popInfectee) - (tNG* popInfectee)
            popI.append(popInfectee)
            
            
            popT.append(popSuceptible + popInfectee)
            
            
        for i in range(100):
            print("S : " + str(popS[i]))
            print("I : " + str(popI[i]))
            print("Population totale : " + str(popT[i]))
            print("********************")
            
        plt.title("Simulation SIS")
        plt.plot(temps, popS,label='Population Susceptible')
        plt.plot(temps, popI,label='Population Infectée')
        plt.plot(temps, popT, label='Population Totale')
        plt.legend(loc='lower right');
        plt.show()
    
        
    
        
        
        
