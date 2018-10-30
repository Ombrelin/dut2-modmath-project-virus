'''
Created on 8 oct. 2018

@author: arsen
'''

from Main.SIR import *
from Main.SEIR import *
from Main.SIS import *
from tkinter import *

class Accueil(Frame):
    
    """Notre fenêtre principale.
    Chaque bouton donne accès à l'interface d'une simulation"""
    
    def __init__(self, **kwargs):
        self.fenetre = Tk();
        self.fenetre.title("Modélisation Mathématique : Propagation de virus Informatiques")
        Frame.__init__(self, self.fenetre, width=300, height=500, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        self.titre = Label(self, text="Modélisation Mathématique : Propagation des virus informatiques").pack()
        self.bouton_SIR = Button(self.fenetre, text="Modèle SIR", command=self.modeleSIR).pack()
        self.boutonSEIR = Button(self.fenetre, text="Modèle SIRS", command=self.modeleSEIR).pack()
        self.boutonSIS = Button(self.fenetre, text="Modèle SIS", command=self.modeleSIS).pack()
        self.bouton_quitter = Button(self.fenetre, text="Quitter", command=self.quit).pack()
        
    def modeleSIR(self):
        SIR = ModeleSIR()
        SIR.mainloop()
        
    def modeleSEIR(self):
        SEIR = ModeleSEIR()
        SEIR.mainloop()
        
    def modeleSIS(self):
        SIS = ModeleSIS()
        SIS.mainloop()