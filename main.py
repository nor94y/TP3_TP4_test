# -*- coding: utf-8 -*-
from noeud import Noeud

# Construction de l'arbre exp(2 + y)
racine = Noeud("exp")
tronc  = Noeud("+")
tronc.ajouter_enfant(Noeud(2))
tronc.ajouter_enfant(Noeud("y"))
racine.ajouter_enfant(tronc)

# Q4 : Test de l'affichage polonais
print("Affichage polonais :", end=" ")
racine.afficher_polonais()
print("\n")  # Saut de ligne

# Q5 : Test de l'évaluation avec y = 3 (résultat attendu : exp(2+3) = exp(5) ≈ 148.41)
dictionnaire_variables = {"y": 3}
resultat = racine.evaluer(dictionnaire_variables)
print(f"Évaluation pour y=3 : {resultat}")

# Q6 : Test du tracé graphique pour y allant de -5 à 2
# On crée une liste de valeurs pour l'axe X
valeurs_y = [-5, -4, -3, -2, -1, 0, 1, 2]
print("Génération du graphique...")
racine.tracer("y", valeurs_y)
