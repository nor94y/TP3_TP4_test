# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math  # Nécessaire pour math.exp()

class Noeud:
    """
    creation de la classe noeud
    """
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []
    """
    creation de la fonction ajouter_enfant
    """
    def ajouter_enfant(self, nouveau_noeud):
        self.enfants.append(nouveau_noeud)
    """
    affichage des noeud sous un format polonais prefixéé
    """
    def afficher_polonais(self):
        # Ajout de end=" " pour que tout s'affiche sur la même ligne
        print(self.valeur, end=" ")
        for i in self.enfants:  
            i.afficher_polonais()
    
    """
    evaluation mathematique des operands et operations
    """
        
    def evaluer(self, dico):
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)
        
        elif isinstance(self.valeur, str) and self.valeur not in ["+", "-", "*", "exp"]:
            if self.valeur not in dico:
                raise ValueError("La variable n'existe pas dans le dictionnaire")
            else: 
                return float(dico[self.valeur])
            
        elif self.valeur == "+":
            return self.enfants[0].evaluer(dico) + self.enfants[1].evaluer(dico) 
        
        elif self.valeur == "-":
            return self.enfants[0].evaluer(dico) - self.enfants[1].evaluer(dico) 
        
        elif self.valeur == "*":
            return self.enfants[0].evaluer(dico) * self.enfants[1].evaluer(dico) 

        # AJOUT DE EXP : c'est un opérateur unaire, il n'a qu'un seul enfant (indice 0)
        elif self.valeur == "exp":
            return math.exp(self.enfants[0].evaluer(dico))

        else: 
            raise ValueError("Opérateur inconnu")
            
    def tracer(self, variable, valeur):
        liste = []
        for k in valeur:
            # Correction ici : utilisation des deux-points : pour le dictionnaire
            liste.append(self.evaluer({variable: k}))
            
        # Correction ici : correspond au nom de votre paramètre "valeur"
        plt.plot(valeur, liste)
        plt.show()
