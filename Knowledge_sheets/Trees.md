# Comparatif des modèles d’arbres de décision et ensembles

| Modèle                | Principe de base                                    | Aire de décision                           | Forces ✅                                                                 | Limites ⚠️                                                                 |
|------------------------|-----------------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Decision Tree**      | Partition récursive de l’espace en régions (CART).  | Blocs rectangulaires, prédiction constante. | Simple, interprétable, capte interactions non-linéaires.                  | Haute variance, surajustement, peu robuste seul.                           |
| **Random Forest**      | Bagging + sélection aléatoire de variables.         | Moyenne de partitions instables.           | Variance ↓, robuste, peu de tuning, bon baseline.                         | Moins interprétable, frontières moins fines que boosting.                  |
| **GBM**                | Boosting séquentiel (1er ordre, gradient).          | Somme de petits arbres → frontière complexe.| Réduit biais, flexible (pertes variées), très performant.                 | Plus lent, plus sensible au surajustement, tuning nécessaire.              |
| **XGBoost**            | GBM + régularisation L1/L2 + gradient + hessien.   | Frontières complexes mais régularisées.     | Rapide, stable, régularisé, gère missing, top en Kaggle.                  | Beaucoup d’hyperparamètres, tuning fin nécessaire.                         |
| **LightGBM**           | GBM optimisé (leaf-wise, histogrammes, EFB, GOSS). | Frontières complexes, croissance déséquilibrée. | Ultra rapide, memory-efficient, scalable gros datasets.                   | Plus sensible à l’overfitting (leaf-wise), moins stable sur petits jeux.   |
| **CatBoost**           | GBM + encodage intelligent des catégorielles.      | Frontières régulières (arbres symétriques). | Parfait pour données catégorielles, régularisation implicite, GPU optimisé.| Plus lent que LightGBM sur données purement numériques, adoption moindre. |

---

## Points clés
- **Variance vs Biais** : Random Forest ↓ variance ; GBM/XGBoost/LightGBM/CatBoost ↓ biais.  
- **XGBoost** : régularisation forte, stable.  
- **LightGBM** : vitesse et scalabilité (big data).  
- **CatBoost** : meilleur sur variables catégorielles.  
