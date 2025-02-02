'''
Created on 24 sept. 2018

@author: arsen
'''

#bibliotheques
from tkinter import * 
import matplotlib.pyplot as plt


class ModeleSIR(Frame):
    
    def __init__(self, **kwargs):
        #interface
        self.fenetre = Tk()
        self.fenetre.title("Modèle SIR")
        Frame.__init__(self, self.fenetre, width=300, height=500, **kwargs)
        
        label1 = Label(self.fenetre, text="")
        label1.pack()
        
        self.temps = Scale(self.fenetre, orient='horizontal', from_=0, to=500,
                       resolution=20, tickinterval=20, length=350,
                       label="Entrez la durée de l'expérience : ")
        self.temps.pack()
        self.temps.set(100)
        
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
        
        self.tGuerison = Scale(self.fenetre, orient='horizontal', from_=0, to=0.2,
                       resolution=0.01, tickinterval=0.01, length=350,
                       label="Entrez le taux de guérison : ")
        self.tGuerison.pack()
        self.tGuerison.set(0.2)
        
        boutonValider = Button(self.fenetre, text="Valider", command= lambda: self.SIR(self.infect.get(),self.tInfect.get(),self.tGuerison.get(),self.temps.get()))
        boutonValider.pack()
    
    
    def SIR(self, infectee, tInfection, tGuerison, time):
    
        plt.clf()
        popInfectee = float(infectee)
        
        TEMPS = time
        
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
            popSuceptible = popSuceptible - (tauxInfection * popSuceptible * popInfectee/popTotale)
            popS.append(popSuceptible)
            
            #popInfectee = popInfectee + popSuceptible - (tauxGuerison * popInfectee)
            popInfectee = popInfectee + ((tauxInfection * popS[i-1] * popInfectee/popTotale) - (tauxGuerison * popInfectee))
            popI.append(popInfectee)
            
            popRetablie = popRetablie + tauxGuerison * popI[i-1]
            popR.append(popRetablie)
            
            popT.append(popSuceptible + popInfectee + popRetablie)
            
            
        for i in range(TEMPS):
            print("S : " + str(popS[i]))
            print("I : " + str(popI[i]))
            print("R : " + str(popR[i]))
            print("Population totale : " + str(popT[i]))
            print("********************")
            
        plt.title("Simulation SIR")
        plt.plot(temps, popS,label='Population Susceptible')
        plt.plot(temps, popI,label='Population Infectée')
        plt.plot(temps, popR, label='Population Retablie')
        plt.plot(temps, popT, label='Population Totale')
        plt.legend(loc='lower right');
        plt.show()
    
        
    
        
        
        
