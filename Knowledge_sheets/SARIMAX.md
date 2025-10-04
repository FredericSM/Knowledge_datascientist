# Create a comprehensive Markdown file covering AR, MA, ARMA, ARIMA, SARIMA, SARIMAX

md = r"""# Modèles de Séries Temporelles — AR · MA · ARMA · ARIMA · SARIMA · SARIMAX

> Ce document est un mémo complet et opérationnel pour un data scientist amené à modéliser des séries temporelles, avec un focus sur AR, MA, ARMA, ARIMA, SARIMA et SARIMAX. Il couvre l’intuition, les formules, les conditions (stationnarité / inversibilité), l’identification via ACF/PACF, l’estimation, le diagnostic, la prévision et les pièges courants. Les exemples de code sont fournis pour `statsmodels` en Python.

---

## Table des matières
1. [Notations & rappels](#notations--rappels)
2. [AR (Auto-Régressif)](#1-ar-auto-régressif)
3. [MA (Moyenne Mobile)](#2-ma-moyenne-mobile)
4. [ARMA (AR + MA)](#3-arma-ar--ma)
5. [ARIMA (ARMA après différenciation)](#4-arima-arma-après-différenciation)
6. [SARIMA (ARIMA saisonnier)](#5-sarima-arima-saisonnier)
7. [SARIMAX (SARIMA + exogènes)](#6-sarimax-sarima--exogènes)
8. [Workflow Box–Jenkins & diagnostics](#7-workflow-boxjenkins--diagnostics)
9. [Recettes Python (statsmodels)](#8-recettes-python-statsmodels)
10. [Glossaire rapide](#9-glossaire-rapide)

---

## Notations & rappels

- Série temporelle : $ \{y_t\}_{t=1..n} $.  
- Opérateur de retard (backshift) : $L y_t = y_{t-1}$.  
- Différenciation ordinaire : $ \Delta y_t = y_t - y_{t-1} = (1 - L) y_t $.  
- Différenciation d’ordre $d$ : $ \Delta^d = (1-L)^d $.  
- Différenciation saisonnière (période $s$) : $ \Delta_s y_t = y_t - y_{t-s} = (1 - L^s) y_t $.  
- Bruit blanc : $ \varepsilon_t \sim \text{i.i.d}(0, \sigma^2) $.  
- ACF : $ \rho_k = \text{Corr}(y_t, y_{t-k}) $.  
- PACF : corrélation partielle entre $y_t$ et $y_{t-k}$ en contrôlant les lags 1..$k-1$.

---

## 1. AR (Auto-Régressif)

### Définition
Modèle **AR(p)** :
$
y_t = c + \sum_{i=1}^{p} \phi_i\, y_{t-i} + \varepsilon_t
$

Forme opérateur : 
$
\Phi(L) y_t = c + \varepsilon_t, \,avec\, \Phi(L) = 1 - \sum_{i=1}^p \phi_i L^i.
$
### Intuition
- **Inertie** : la valeur d’aujourd’hui hérite d’une **mémoire longue** des valeurs passées (via rétroaction).

### Stationnarité (indispensable)
- Condition : **toutes les racines** de $\Phi(z)=0$ doivent être **hors du cercle unité** $(|z|>1)$.
- Cas AR(1) : $y_t = c + \phi y_{t-1} + \varepsilon_t$ est stationnaire si $|\phi|<1$.
- Pourquoi ? La rétroaction se contracte au fil des lags, empêchant l’explosion de la variance.

### Propriétés clés (AR(1))
- Moyenne : $ E[y_t] = \dfrac{c}{1-\phi} $.
- Variance : $ \mathrm{Var}(y_t) = \dfrac{\sigma^2}{1-\phi^2} $ (si $|\phi|<1$).
- ACF : décroissance géométrique $ \rho_k = \phi^k $.
- PACF : **cut-off** au lag $p$ (signatures d’identification).

### Estimation
- OLS (pour AR(p) écrit en régression), Yule–Walker, maximum de vraisemblance (MLE).
- Sélection d’ordre $p$ : AIC / AICc / BIC, PACF, validation temporelle.

### Prévision
- 1 pas : $ \hat{y}_{t+1|t} = \hat{c} + \sum_{i=1}^{p} \hat{\phi}_i y_{t+1-i} $.
- Multi-pas : itération récursive (utilise les prévisions précédentes).  
- Intervalles : via variance des erreurs de prévision sous hypothèses gaussiennes.

### Diagnostic & pièges
- Résidus : pas d’autocorrélation (Ljung–Box), variance homoscédastique, approx. normalité.  
- Si tendance / racine unitaire (ADF, KPSS) → **différencier** → ARIMA.  
- Overfitting si $p$ trop grand ; sous-modélisation si ACF/PACF résiduels non nuls.

---

## 2. MA (Moyenne Mobile)

### Définition
Modèle **MA(q)** :
\[
y_t = \mu + \varepsilon_t + \sum_{j=1}^{q} \theta_j\, \varepsilon_{t-j}
\]
Forme opérateur : $ y_t = \mu + \Theta(L)\varepsilon_t$, avec $ \Theta(L)= 1 + \sum_{j=1}^q \theta_j L^j$.

### Intuition
- **Chocs transitoires** : $y_t$ est un **filtrage fini** du bruit blanc ; un choc affecte $y$ pendant $q$ pas, puis s’éteint.

### Inversibilité (indispensable)
- Condition : **toutes les racines** de $ \Theta(z)=0 $ doivent être **hors du cercle unité** $(|z|>1)$.
- Pourquoi ? Permet une représentation **AR(∞)** stable : $\varepsilon_t = \Theta(L)^{-1} y_t$.  
  Exemple MA(1) : $ \varepsilon_t = y_t - \theta y_{t-1} + \theta^2 y_{t-2} - \dots $ converge si $|\theta|<1$.

### Propriétés
- Stationnaire **par construction** (combinaison finie de bruits).  
- Moyenne : $E[y_t]=\mu$.  
- Variance : $ \mathrm{Var}(y_t)=\sigma^2 \left( 1 + \sum_{j=1}^q \theta_j^2 \right)$.  
- **Signature ACF** : **cut-off** au lag $q$.  
- **PACF** : décroissance progressive.

### Estimation
- Pas d’OLS simple (les $\varepsilon$ ne sont pas observés).  
- MLE / méthodes numériques (Kalman, innovations).  
- Identification par ACF (cut-off) + AIC/BIC.

### Pièges
- Non-inversibilité → paramètres non identifiables (plusieurs MA équivalents).  
- Ordre $q$ trop grand : surparamétrisation, instabilité.

---

## 3. ARMA (AR + MA)

### Définition
Modèle **ARMA(p,q)** :
\[
y_t = c + \sum_{i=1}^{p} \phi_i y_{t-i} + \varepsilon_t + \sum_{j=1}^{q} \theta_j \varepsilon_{t-j}
\]
Forme opérateur : $ \Phi(L) y_t = c + \Theta(L) \varepsilon_t$.

### Conditions
- **Stationnarité** : racines de $\Phi(z)=0$ hors cercle unité.  
- **Inversibilité** : racines de $\Theta(z)=0$ hors cercle unité.

### Signatures ACF/PACF
- Ni ACF ni PACF **strictement tronquées** (vs AR seul / MA seul).  
- Décroissances “mixtes” → identification par essais guidés + AIC/BIC + diagnostics.

### Estimation & diagnostic
- MLE (souvent via état-espace / Kalman).  
- Vérifier résidus (Ljung–Box), racines (stabilité/inversibilité), normalité approx., hétéroscédasticité.  
- Si non stationnaire → passer à **ARIMA**.

---

## 4. ARIMA (ARMA après différenciation)

### Idée clé — le “I” (Integrated)
On rend la série **stationnaire** par **différenciation** avant d’appliquer ARMA :  
\[
ARIMA(p,d,q): \quad \Phi(L)\, \Delta^d y_t = c + \Theta(L)\, \varepsilon_t
\]

### Pourquoi la différenciation supprime la tendance ?
- $\Delta y_t = y_t - y_{t-1}$ supprime une tendance **linéaire**.  
- $\Delta^2 y_t = \Delta(\Delta y_t)$ supprime une tendance **quadratique**.  
- Analogie dérivée discrète : chaque $\Delta$ réduit le **degré** du polynôme de tendance d’1.  
  - Exemple : $y_t = t^2 \Rightarrow \Delta y_t = 2t-1 \Rightarrow \Delta^2 y_t = 2$.

### Choix de $d$
- Tester racine unitaire (ADF, KPSS, PP).  
- **Généralement $d \in \{0,1,2\}$**.  
- **Sur-différenciation** → introduit autocorrélations négatives, augmente la variance des erreurs → éviter.

### Formulations utiles
- **ARIMA(0,1,0)** : random walk, $ y_t = y_{t-1} + \varepsilon_t $.  
- **ARIMA(0,1,0) + drift** : random walk avec dérive.  
- **ARIMA(0,1,1)** : marche aléatoire + lissage exponentiel (équivalences).

### Estimation & prévision
- Estimation par MLE sur la série **différenciée**.  
- Prévisions **réintégrées** en cumulant les deltas (ajout de la tendance retirée).

### Diagnostics
- Résidus de $\Delta^d y$ ≈ bruit blanc.  
- Vérifier racines AR/MA (stationnarité/inversibilité **après** différenciation).

---

## 5. SARIMA (ARIMA saisonnier)

### Définition (multiplicatif)
\[
SARIMA(p,d,q)\,(P,D,Q)_s: \quad \Phi(L)\,\Phi_s(L^s)\, \Delta^d \Delta_s^D y_t = c + \Theta(L)\,\Theta_s(L^s)\, \varepsilon_t
\]
- $s$ = période saisonnière (p.ex. 12 mensuel, 24 horaire/journalier, 7 hebdo).  
- $D$ = degré de différenciation **saisonnière** $(1-L^s)^D$.

### Intuition
- On enlève **tendance** (par $\Delta^d$) **et** **saisonnalité** (par $\Delta_s^D$), puis on modélise ARMA sur les composantes restantes, avec des **termes AR/MA saisonniers**.

### Identification
- Pics de l’**ACF** aux multiples de $s$ → composante MA saisonnière ;  
  Pics du **PACF** aux multiples de $s$ → composante AR saisonnière.  
- Choisir $P,Q,D$ (saisonnier) + $p,q,d$ (non saisonnier) via AIC/BIC et diagnostics.

### Conditions
- Stationnarité : racines des polynômes AR (non saisonnier et saisonnier) **hors** du cercle unité.  
- Inversibilité : idem pour les polynômes MA.

### Pièges
- **Sur-différenciation saisonnière** ($D$ trop grand) → séries sur-bruitées.  
- Confondre **effets calendaires** et vraie saisonnalité (introduire des indicatrices si nécessaire).

---

## 6. SARIMAX (SARIMA + exogènes)

### Définition
\[
y_t = \text{SARIMA part} + X_t \beta + \varepsilon_t
\]
- $X_t \in \mathbb{R}^m$ : **variables exogènes** (température, promos, jours fériés, débit amont, etc.).  
- Matrice $X \in \mathbb{R}^{n \times m}$ : **vecteurs alignés dans le temps** (une ligne par $t$, une colonne par variable).

### Intuition & intérêt
- Ajouter des **facteurs explicatifs** exogènes améliore la précision et l’interprétabilité.  
- Attention : il faut connaître (ou prévoir) $X_{t+h}$ pour **prévoir** $y_{t+h}$.

### Paramétrage de $X$
- Alignement temporel strict (mêmes index que $y$).  
- Possibles **lags** ou **leads** de $X$ si causalité retardée/anticipée.  
- Parcimonie : éviter multicolinéarité, variables redondantes.  
- Risque d’**endogénéité** (exogènes corrélées à l’erreur) → prudence d’interprétation.

### Sous le capot
- Implémentation état-espace / filtre de **Kalman** (statsmodels).  
- Estimation MLE conjointe des paramètres SARIMA et des $\beta$.

---

## 7. Workflow Box–Jenkins & diagnostics

### Étapes recommandées
1. **Exploration** : tracés, saisonnalité, tendance, ruptures.  
2. **Stationnarité** : tests ADF/KPSS/PP ; décider $d$ (et $D$ si saisonnalité).  
3. **Identification** : ACF/PACF → hypothèses (p,q) et (P,Q).  
4. **Estimation** : MLE (ARIMA/SARIMA/SARIMAX).  
5. **Diagnostic** : résidus ~ bruit blanc (Ljung–Box), normalité approx., hétéroscédasticité, **racines** hors cercle unité.  
6. **Sélection** : AIC/AICc/BIC + backtesting (walk-forward).  
7. **Prévision & monitoring** : intervalles, dérive de performance, recalibrage périodique.

### Évaluation (metrics)
- MAE, RMSE, MAPE ; Pinball loss / quantiles pour prévisions probabilistes ; couverage des intervalles.  
- Backtesting **temps-réel** (validation glissante) plutôt que K-fold aléatoire.

### Pièges fréquents
- Confondre non-stationnarité **stochastique** (racine unitaire) avec **tendance déterministe** : la seconde peut parfois être retirée par régression de tendance plutôt que différenciation.  
- Sur-différenciation (variance accrue, ACF négative au lag 1).  
- Ignorer des **effets calendaires** (jours fériés, vacances) → passer par SARIMAX.  
- Oublier de fournir $X$ **futur** pour la prévision SARIMAX.  
- Ne pas vérifier les **racines** (stabilité/inversibilité).

---

## 8. Recettes Python (statsmodels)

> Nécessite `statsmodels` ≥ 0.13 en général.

### AR / ARMA / ARIMA
```python
import numpy as np
import statsmodels.api as sm

# Exemple ARIMA(p,d,q)
y = ...  # série 1D
model = sm.tsa.ARIMA(y, order=(p, d, q))
res = model.fit()
print(res.summary())

# Vérifier racines (stationnarité / inversibilité)
print("AR roots:", res.arroots)   # |root| > 1  => stationnaire
print("MA roots:", res.maroots)   # |root| > 1  => inversible

# Test Ljung–Box sur résidus
from statsmodels.stats.diagnostic import acorr_ljungbox
lb = acorr_ljungbox(res.resid, lags=[10, 20], return_df=True)
print(lb)
