# 📊 Évaluation des modèles de prévision

---

## 1. RMSE — Root Mean Squared Error
$
\mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i-\hat y_i)^2}
$

- Unité : même que $y$.  
- Pénalise fortement les grosses erreurs.  
- Sensible aux outliers.  
- Utile si **grosses erreurs = gros coûts**.  

---

## 2. MAE — Mean Absolute Error
$
\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i-\hat y_i|
$

- Unité : même que $y$.  
- Plus robuste que RMSE aux outliers.  
- Mesure l’**erreur typique**.  
- Moins discriminant si les modèles sont proches.  

---

## 3. MAPE — Mean Absolute Percentage Error
$
\mathrm{MAPE} = \frac{100}{n}\sum_{i=1}^n \left|\frac{y_i-\hat y_i}{y_i}\right|
$

- Unité : % (sans dimension).  
- Lisible pour le business (“erreur moyenne = X%”).  
- Problèmes :  
  - indéfini si $y_i=0$,  
  - biaisé pour petites valeurs,  
  - asymétrique.  
- Variantes : **SMAPE**, **WAPE/WMAPE**.  

---

## 4. CRPS — Continuous Ranked Probability Score
$
\mathrm{CRPS}(F,y) = \int_{-\infty}^{\infty}\big(F(z) - \mathbf{1}\{y \le z\}\big)^2 dz
$

ou

$
\mathrm{CRPS}(F,y) = \mathbb{E}_F[|X-y|] - \tfrac{1}{2}\mathbb{E}_F[|X-X'|]
$

- Unité : même que $y$.  
- Évalue la qualité des **prévisions probabilistes**.  
- Généralise le MAE au cas probabiliste.  
- Mesure à la fois **justesse** et **calibration**.  

---

## 5. COVERAGE & Largeur des intervalles
- **Coverage** :  
$
\mathrm{Coverage}_\alpha = \frac{1}{n}\sum_{i=1}^n \mathbf{1}\{L_i \le y_i \le U_i\}
$

- **Largeur moyenne** :  
$
\mathrm{AvgWidth}_\alpha = \frac{1}{n}\sum (U_i - L_i)
$

- Vérifie si les intervalles de prédiction contiennent la vérité avec la bonne fréquence.  
- Bon modèle = coverage ≈ niveau nominal (ex. 95%) **et** largeur minimale.  

---

# 📋 Tableau comparatif

| **Métrique** | **Formule** | **Unité** | **Points forts** | **Limites** | **Cas d’usage typiques** |
|--------------|-------------|-----------|------------------|-------------|--------------------------|
| **RMSE** | \(\sqrt{\frac{1}{n}\sum (y-\hat y)^2}\) | Même que \(y\) | Sensible aux grosses erreurs, discriminant | Très sensible aux outliers | Prévision de charges critiques, énergie, finance |
| **MAE** | \(\frac{1}{n}\sum |y-\hat y|\) | Même que \(y\) | Robuste, interprétation simple | Ne différencie pas assez les grosses erreurs | Prévision ventes/logistique avec bruit |
| **MAPE** | \(\frac{100}{n}\sum \big|\frac{y-\hat y}{y}\big|\) | % | Sans unité, lisible en business | Indéfini si \(y=0\), biais sur petites valeurs | Reporting business, comparaisons produits |
| **CRPS** | \(\int (F(z)-\mathbf{1}\{y \le z\})^2 dz\) | Même que \(y\) | Évalue distributions probabilistes, calibration | Plus complexe à calculer | Météo, énergie, finance (prévisions probabilistes) |
| **Coverage** | \(\frac{1}{n}\sum \mathbf{1}\{L \le y \le U\}\) | % (fréquence) | Vérifie la calibration des intervalles | Doit être complété par la largeur | Qualité des intervalles de prédiction (forecasting) |