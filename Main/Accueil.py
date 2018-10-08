'''
Created on 8 oct. 2018

@author: arsen
'''

from Main.SIR import *
from tkinter import *

class Accueil(Frame):
    
    """Notre fen�tre principale.
    Chaque bouton donne accès à l'interface d'une simulation"""
    
    def __init__(self, **kwargs):
        self.fenetre = Tk();
        Frame.__init__(self, self.fenetre, width=300, height=500, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        self.titre = Label(self, text="Modélisation Mathématique : Propagation des virus informatiques").pack()
        self.bouton_SIR = Button(self.fenetre, text="Modèle SIR", command=self.modeleSIR).pack()
        self.bouton_quitter = Button(self.fenetre, text="Quitter", command=self.quit).pack()
        
    def modeleSIR(self):
        SIR = ModeleSIR()
        SIR.mainloop()
        
        