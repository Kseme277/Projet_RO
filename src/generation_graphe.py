import networkx as nx
import random
import csv

class GenerateurGraphe:
    def __init__(self):
        self.graphe = None
    
    def generer_graphe(self, nombre_sommets, probabilite_lien=0.1):
        """Génère un graphe aléatoire avec le nombre spécifié de sommets"""
        self.graphe = nx.erdos_renyi_graph(nombre_sommets, probabilite_lien, directed=False)
        
       
        for u, v in self.graphe.edges():
            distance = random.randint(1, 6)  
            self.graphe[u][v]['poids'] = distance
        
        return self.graphe
    
    def sauvegarder_graphe(self, graphe, nom_fichier):
        """Sauvegarde le graphe au format CSV"""
        with open(nom_fichier, 'w', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerow(['sommet_i', 'sommet_j', 'distance'])
            
            for u, v, data in graphe.edges(data=True):
                writer.writerow([u, v, data['poids']])
                # Pour un graphe non orienté, on peut aussi écrire dans l'autre sens
                # writer.writerow([v, u, data['poids']])
        
        print(f"Graphe sauvegardé dans {nom_fichier}")