from src.generation_graphe import GenerateurGraphe
from src.analyse_graphe import AnalyseurGraphe
from src.simulation_propagation import SimulateurPropagation
from src.visualisation import Visualiseur
import networkx as nx

def main():
    # Génération du graphe
    print("=== Génération du graphe ===")
    generateur = GenerateurGraphe()
    graphe = generateur.generer_graphe(250)
    generateur.sauvegarder_graphe(graphe, "data/reseau_clients.csv")
    
    
    print("\n=== Analyse du graphe original ===")
    analyseur = AnalyseurGraphe(graphe)
    
    
    distribution_degres = analyseur.calculer_distribution_degres()
    print("Distribution des degrés:", distribution_degres)
    
    
    top5_degres = analyseur.top5_sommets_degre()
    print("Top 5 sommets par degré:", top5_degres)
    
    
    distribution_proximite = analyseur.calculer_distribution_proximite()
    print("Distribution de proximité:", distribution_proximite)
    
    
    top5_proximite = analyseur.top5_sommets_proximite()
    print("Top 5 sommets par proximité:", top5_proximite)
    
    
    print("\n=== Simulation de propagation ===")
    simulateur = SimulateurPropagation(graphe)
    
    
    sommet_haut_degre = top5_degres[0][0]
    propagation_5j = simulateur.simuler_propagation(sommet_haut_degre, 5)
    print(f"Sommets touchés après 5 jours depuis {sommet_haut_degre}: {propagation_5j}")
    
    
    sommet_basse_proximite = min([(s, p) for s, p in analyseur.calculer_proximites().items()], 
                                key=lambda x: x[1])[0]
    propagation_7j = simulateur.simuler_propagation(sommet_basse_proximite, 7)
    print(f"Sommets touchés après 7 jours depuis {sommet_basse_proximite}: {propagation_7j}")
    
    
    print("\n=== Suppression des 10 sommets ===")
    sommets_a_supprimer = set([s[0] for s in top5_degres] + [s[0] for s in top5_proximite])
    print(f"Sommets à supprimer: {sommets_a_supprimer}")
    
    graphe_reduit = graphe.copy()
    graphe_reduit.remove_nodes_from(sommets_a_supprimer)
    
   
    generateur.sauvegarder_graphe(graphe_reduit, "data/reseau_clients_reduit.csv")
    
    
    print("\n=== Analyse du graphe réduit ===")
    analyseur_reduit = AnalyseurGraphe(graphe_reduit)
    simulateur_reduit = SimulateurPropagation(graphe_reduit)
    
   
    nouveau_top_degres = analyseur_reduit.top5_sommets_degre()
    nouveau_top_proximite = analyseur_reduit.top5_sommets_proximite()
    
    print("Nouveau top degrés:", nouveau_top_degres)
    print("Nouveau top proximité:", nouveau_top_proximite)
    
   
    nouveau_sommet_haut_degre = nouveau_top_degres[0][0]
    propagation_4j = simulateur_reduit.simuler_propagation(nouveau_sommet_haut_degre, 4)
    print(f"Sommets touchés après 4 jours depuis {nouveau_sommet_haut_degre}: {propagation_4j}")
    
    
    nouveau_sommet_basse_proximite = min([(s, p) for s, p in analyseur_reduit.calculer_proximites().items()], 
                                       key=lambda x: x[1])[0]
    propagation_3j = simulateur_reduit.simuler_propagation(nouveau_sommet_basse_proximite, 3)
    print(f"Sommets touchés après 3 jours depuis {nouveau_sommet_basse_proximite}: {propagation_3j}")
    
    
    print("\n=== Génération des visualisations ===")
    visualiseur = Visualiseur()
    visualiseur.generer_histogramme_degres(distribution_degres, "output/histogramme_degres.png")
    visualiseur.generer_histogramme_proximite(distribution_proximite, "output/histogramme_proximite.png")
    
    print("\n=== Analyse terminée ===")

if __name__ == "__main__":
    main()