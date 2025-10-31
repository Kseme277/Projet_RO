# Projet Marketing - Analyse de Réseau de Clients

## Membres du groupe
- **Igre Urbain** - Chef de projet
- **Bilogue seme** - Développeuse principale  
- **Eddy Giovanni** - Analyste de données

## Description du projet
Ce projet analyse un réseau de contacts entre clients pour une campagne marketing. Il génère un graphe aléatoire de 250 clients, effectue diverses analyses de centralité et simule des campagnes de propagation virale.

##  Objectifs
- Générer un réseau aléatoire de contacts clients
- Analyser la structure du réseau (degrés, proximité)
- Identifier les clients les plus influents
- Simuler des campagnes marketing virales
- Évaluer l'impact de la suppression des clients les plus centraux

## Structure du projet
```
projet_marketing/
├── data/                   # Fichiers de données générés
│   ├── reseau_clients.csv
│   └── reseau_clients_reduit.csv
├── src/                    # Code source
│   ├── __init__.py
│   ├── generation_graphe.py
│   ├── analyse_graphe.py
│   ├── simulation_propagation.py
│   └── visualisation.py
├── output/                 # Graphiques générés
│   ├── histogramme_degres.png
│   └── histogramme_proximite.png
├── main.py                 # Script principal
├── requirements.txt        # Dépendances
└── README.md
```

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### 1. Cloner le dépôt
```bash
git clone https://github.com/Kseme277/Projet_RO.git
cd Projet_RO
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Exécution du projet

### Lancer l'analyse complète
```bash
python main.py
```

### Exécution étape par étape
```python
# Dans un interpréteur Python
from main import main
main()
```

## Résultats attendus

### Sorties générées

#### Fichiers de données :
- **`data/reseau_clients.csv`** : Graphe original avec 250 sommets
- **`data/reseau_clients_reduit.csv`** : Graphe après suppression des 10 sommets les plus centraux

#### Visualisations :
- **`output/histogramme_degres.png`** : Distribution des degrés des sommets
- **`output/histogramme_proximite.png`** : Distribution des valeurs de proximité

#### Sortie console - Résultats détaillés :

```
=== Génération du graphe ===
Graphe sauvegardé dans data/reseau_clients.csv

=== Analyse du graphe original ===
Distribution des degrés: {2: 15, 3: 28, 4: 35, ...}
Top 5 sommets par degré: [(42, 12), (17, 11), (89, 10), ...]
Distribution de proximité: {1500: 8, 1600: 12, 1700: 25, ...}
Top 5 sommets par proximité: [(156, 2450), (89, 2380), (42, 2300), ...]

=== Simulation de propagation ===
Sommets touchés après 5 jours depuis 42: 87
Sommets touchés après 7 jours depuis 201: 156

=== Suppression des 10 sommets ===
Sommets à supprimer: {42, 17, 89, 156, 201, ...}

=== Analyse du graphe réduit ===
Nouveau top degrés: [(132, 8), (67, 7), (189, 7), ...]
Nouveau top proximité: [(132, 1800), (189, 1750), (67, 1700), ...]
Sommets touchés après 4 jours depuis 132: 45
Sommets touchés après 3 jours depuis 201: 28
```

### Métriques calculées

1. **Distribution des degrés** : Nombre de sommets pour chaque valeur de degré
2. **Top 5 sommets par degré** : Clients avec le plus de connexions directes
3. **Distribution de proximité** : Répartition des sommes des distances
4. **Top 5 sommets par proximité** : Clients avec les plus grandes sommes de distances
5. **Propagation après 5 jours** : depuis le sommet de plus haut degré
6. **Propagation après 7 jours** : depuis le sommet de plus basse proximité
7. **Nouvelle propagation après 4 jours** : sur le graphe réduit
8. **Nouvelle propagation après 3 jours** : sur le graphe réduit



##  Bibliothèques utilisées

- **networkx** : Manipulation et analyse de graphes
- **matplotlib** : Génération de graphiques et histogrammes
- **collections** : Structures de données avancées
- **csv** : Gestion des fichiers de données
- **random** : Génération aléatoire

## Concepts implémentés

- **Graphes aléatoires** (modèle Erdős-Rényi)
- **Centralité des sommets** (degré, proximité)
- **Parcours en largeur** (BFS) pour la propagation
- **Plus courts chemins** (algorithme de Dijkstra)
- **Analyse de réseau** et marketing viral

