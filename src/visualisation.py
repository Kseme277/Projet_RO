import matplotlib.pyplot as plt
import os

class Visualiseur:
    def __init__(self):
        # Création du dossier output s'il n'existe pas
        if not os.path.exists('output'):
            os.makedirs('output')
    
    def generer_histogramme_degres(self, distribution_degres, nom_fichier):
        """Génère un histogramme de la distribution des degrés"""
        plt.figure(figsize=(10, 6))
        plt.bar(distribution_degres.keys(), distribution_degres.values())
        plt.xlabel('Degré')
        plt.ylabel('Nombre de sommets')
        plt.title('Distribution des degrés dans le graphe')
        plt.grid(True, alpha=0.3)
        plt.savefig(nom_fichier)
        plt.close()
        print(f"Histogramme des degrés sauvegardé: {nom_fichier}")
    
    def generer_histogramme_proximite(self, distribution_proximite, nom_fichier):
        """Génère un histogramme de la distribution de proximité"""
        plt.figure(figsize=(10, 6))
        plt.bar(distribution_proximite.keys(), distribution_proximite.values())
        plt.xlabel('Somme des distances (proximité)')
        plt.ylabel('Nombre de sommets')
        plt.title('Distribution de proximité dans le graphe')
        plt.grid(True, alpha=0.3)
        plt.savefig(nom_fichier)
        plt.close()
        print(f"Histogramme de proximité sauvegardé: {nom_fichier}")