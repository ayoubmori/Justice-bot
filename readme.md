# JusticeBot - L'IA Juge

JusticeBot est un projet simple mais puissant qui simule le raisonnement d'un juge. Il lit de courtes descriptions de cas juridiques fictifs, rend un verdict de **GUILTY** (Coupable) ou **NOT GUILTY** (Non coupable), et fournit une justification claire pour sa décision.

Ce projet a été développé avec une contrainte majeure : **aucune API externe ou LLM pré-entraîné** (comme GPT, Bard, etc.) n'a été utilisé pour la logique de décision. Tout le raisonnement est basé sur un algorithme de règles local, transparent et explicable.

## 🚀 Fonctionnalités

* Rend des verdicts binaires (`GUILTY` / `NOT GUILTY`).
* Génère des justifications claires et lisibles basées sur un ensemble de règles.
* Inclut un script pour générer un dataset de cas fictifs pour les tests.
* Fonctionne entièrement en local, sans connexion Internet ni clé API requise.

## ⚙️ Comment ça marche ?

L'architecture du projet est volontairement simple et repose sur trois composants principaux :

1.  **`rules.json`** : C'est le "cerveau" du bot. Ce fichier JSON contient des listes de mots-clés pour les preuves à charge (`guilty_evidence`) et à décharge (`innocent_evidence`), ainsi que les justifications correspondantes. La logique du bot peut être entièrement modifiée en éditant ce fichier.

2.  **`gnerete_dataset.py`** : Un script utilitaire pour générer un fichier `cases.json` contenant 250 cas fictifs. Il utilise les mots-clés de `rules.json` pour construire des scénarios variés.

3.  **`judgebot.py`** : Le script principal. Il charge les règles, prend une description de cas en entrée, recherche les mots-clés pertinents et applique une logique de décision hiérarchique pour déterminer le verdict et la justification. La règle principale est que **toute preuve d'innocence l'emporte sur une preuve de culpabilité**.

## 🛠️ Installation et Utilisation

Aucune installation complexe n'est requise, car le projet utilise les bibliothèques standard de Python.

**1. Clonez le dépôt :**
```bash
git clone [https://github.com/ayoubmori/Justice-bot.git](https://github.com/ayoubmori/Justice-bot.git)
cd JusticeBot
```

**2. Générez le dataset :**
Si vous souhaitez générer ou régénérer le fichier cases.json, exécutez :

```bash
python gnerete_dataset.py
```
Cela créera un fichier cases.json avec 250 nouveaux cas.

**3. Exécutez le JudgeBot :**
Pour obtenir un verdict, exécutez le script judgebot.py en lui passant une description de cas entre guillemets comme argument.

Exemple :

```bash
python judgebot.py "A woman was arrested with forged documents and a stolen credit card."
```
Sortie attendue :

Verdict: GUILTY
Justification: Evidence points to financial fraud or forgery.
Exemple avec preuve d'innocence :

```bash
python judgebot.py "While the suspect did punch the victim, the report states it was provoked into the fight."
```
Sortie attendue :

Verdict: NOT GUILTY
Justification: The action was taken in self-defense, which negates criminal intent.
Limitations
Ce projet est une simulation et a des limites intentionnelles :

Il est fragile : Le bot ne reconnaît que les mots-clés (keywords) exacts définis dans rules.json. Il ne comprend ni les synonymes ni le contexte.

Il ne "comprend" pas : Il s'agit d'un système de correspondance de mots-clés (keywords), et non d'une véritable IA capable de raisonnement sémantique.

Son évolutivité est manuelle : Pour ajouter de nouvelles règles, le fichier rules.json doit être modifié à la main.

---
Autor : Ayoub Taouabi