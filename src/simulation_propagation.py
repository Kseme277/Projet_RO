import networkx as nx
from collections import deque

class SimulateurPropagation:
    def __init__(self, graphe):
        self.graphe = graphe
    
    def simuler_propagation(self, sommet_depart, jours):
        """
        Simule la propagation pendant un nombre donné de jours
        Chaque arête prend 1 journée à traverser
        """
        if sommet_depart not in self.graphe:
            return 0
        
        visites = set([sommet_depart])
        file_attente = deque([(sommet_depart, 0)])  # (sommet, jours écoulés)
        
        while file_attente:
            sommet_actuel, jours_ecoules = file_attente.popleft()
            
            if jours_ecoules >= jours:
                continue
            
            for voisin in self.graphe.neighbors(sommet_actuel):
                if voisin not in visites:
                    visites.add(voisin)
                    file_attente.append((voisin, jours_ecoules + 1))
        
        return len(visites)