import networkx as nx
from collections import defaultdict

class AnalyseurGraphe:
    def __init__(self, graphe):
        self.graphe = graphe
    
    def calculer_degres(self):
        """Calcule le degré de chaque sommet"""
        return dict(self.graphe.degree())
    
    def calculer_distribution_degres(self):
        """Calcule la distribution des degrés"""
        degres = self.calculer_degres()
        distribution = defaultdict(int)
        
        for degre in degres.values():
            distribution[degre] += 1
        
        return dict(distribution)
    
    def top5_sommets_degre(self):
        """Retourne les 5 sommets avec les plus hauts degrés"""
        degres = self.calculer_degres()
        return sorted(degres.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def calculer_proximites(self):
        """Calcule la somme des distances pour chaque sommet"""
        proximites = {}
        
        for sommet in self.graphe.nodes():
            # Calcul des plus courts chemins depuis ce sommet
            chemins = nx.single_source_dijkstra_path_length(self.graphe, sommet, weight='poids')
            # Somme des distances vers tous les autres sommets
            somme_distances = sum(chemins.values())
            proximites[sommet] = somme_distances
        
        return proximites
    
    def calculer_distribution_proximite(self):
        """Calcule la distribution des proximités"""
        proximites = self.calculer_proximites()
        distribution = defaultdict(int)
        
        for proximite in proximites.values():
            # Arrondir pour créer des bins dans l'histogramme
            bin_proximite = round(proximite / 100) * 100
            distribution[bin_proximite] += 1
        
        return dict(distribution)
    
    def top5_sommets_proximite(self):
        """Retourne les 5 sommets avec les plus hautes valeurs de proximité"""
        proximites = self.calculer_proximites()
        return sorted(proximites.items(), key=lambda x: x[1], reverse=True)[:5]