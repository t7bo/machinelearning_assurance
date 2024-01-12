# Projet de Machine Learning - Prédiction des charges d'assurance

## Objectif du Projet

L'objectif de ce projet est de développer un modèle de machine learning basé sur la régression linéaire pour prédire les charges d'assurance que de nouveaux clients pourraient supporter s'ils souscrivent chez nous. En utilisant un ensemble de données d'assurance existant, le modèle sera formé sur des caractéristiques telles que l'âge, le sexe, le tabagisme, la région géographique, etc.

## Données

Les données d'assurance utilisées dans ce projet sont stockées dans le fichier `donnees_assurance.csv`. Celles-ci comprennent des informations sur les clients existants, y compris le coût réel des charges d'assurance associées.

## Prérequis

Assurez-vous d'installer les bibliothèques nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

## Structure du Projet

- `data.csv` et `clean_data.csv`: Fichiers contenant les données d'assurance utilisées pour l'entraînement du modèle.
- `analyses.ipynb`: Jupyter Notebook d'analyse univariée et bivariée
- `machine_learning.ipynb`: Jupyter Notebook pour l'entraînement du modèle de régression linéaire.
- `app.py`: Script Python & StreamLit pour faire des prédictions avec le modèle entraîné en temps réel.
- `requirements.txt`: Fichier contenant les dépendances du projet.

## Entraînement du Modèle

Pour entraîner le modèle, exécutez le script `app.py`. Le modèle entraîné sera sauvegardé dans le fichier `modele_assurance.pkl`.

```bash
python train_model.py
```

## Faire des Prédictions

Utilisez le script `predict.py` pour faire des prédictions avec le modèle entraîné.

```bash
python predict.py
```

## Conclusion

Ce projet vise à fournir une solution de prédiction des charges d'assurance pour les nouveaux clients. N'hésitez pas à ajuster les caractéristiques du modèle ou à explorer d'autres algorithmes de régression pour améliorer les performances.
