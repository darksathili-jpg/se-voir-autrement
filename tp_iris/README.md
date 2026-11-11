# TP IRIS V2.2 — audit correctif du 11 novembre 2026

## Base de référence conservée
`site_tp_iris_V2_calibration(1).zip`. Les six expériences, la BD, les guides, la calibration, les modes d’affichage et les validations sont conservés. Aucun remplacement de la scénographie.

## Correctifs essentiels
- La référence scientifique est désormais **la photo 2 réelle, isolée par masque circulaire** (sans génération ni invention de fibres). L’ancienne image d’iris synthétique reste seulement dans les fichiers de référence d’origine pour conservation, **elle n’est plus affichée comme photographie**.
- L’atelier charge 4 exemples photographiques embarqués dans le HTML par `data:image/jpeg;base64` : lecture des pixels autorisée même en ouverture directe `file://`, sans serveur ni Internet.
- La photo 2 complète est accessible à côté de la découpe, pour confronter les pixels et les reflets authentiques.
- L’atelier passe à un canevas carré, pour éviter une déformation visuelle des photographies.
- L’extension de traitement de pixels est explicitement facultative (20–30 min supplémentaires), distincte des 60 min de prise de vue.
- La démarche de lumière latérale en pièce sombre est présentée comme essai observé du professeur, pas comme consigne obligatoire en classe ; pas d’exposition directe à une torche, ni de distance universelle.
- La lecture de pixels bloquée affiche désormais un message d’erreur plutôt que d’échouer silencieusement.

## Utilisation
Décompresser le ZIP, conserver `index.html`, `atelier_pixels.html`, `assets/` dans le même dossier, ouvrir `index.html` en navigateur moderne. Accéder à la section « Filtres », ou ouvrir `atelier_pixels.html` indépendamment si les cadres intégrés sont interdits par la politique de l’établissement.

## Avant la séance
Ouvrir l’atelier, vérifier qu’une image d’iris circulaire **issue de la photo 2 réelle** s’affiche. Sélectionner « Niveaux de gris », tester le curseur puis le bouton « Réinitialiser ». Vérifier la bascule Clair/Projecteur, l’aperçu d’image locale, et les permissions d’enregistrement pour les exports.

## Réserve
Les tests automatisés réalisés via script sans navigateur ne prouvent pas l’affichage sur tous les ordinateurs. Le navigateur de cette session bloque la navigation web locale dans Playwright ; une recette complète dans ton Chrome/Edge demeure requise.


## V2.4 — Illustration de calibration (ajout ciblé)
- Affiche pédagogique ajoutée immédiatement après la consigne de calibration sur objet inerte.
- Fichier : `assets/calibration_macro_objet_inerte.png` (cliquer pour ouvrir et imprimer).
- Aucun remplacement des illustrations précédentes, aucune modification du code des exercices ou des filtres.
- Attention : la mention ×3 dans l’illustration est un exemple, le bon réglage dépend des essais réalisés sur le smartphone.


## V2.5 — Mire économique imprimable
La calibration contient une mire A4 noir et blanc : `assets/mire_iris_economie_A4.pdf` (fichier vectoriel conseillé), l'aperçu PNG et `mire_impression.html` (bouton imprimer). Imprimer à 100 % et vérifier une longueur de 50 mm. Les illustrations précédentes restent intactes.


## V2.7 — Remerciement à Nathalie
- Section « Merci, Nathalie ! » ajoutée juste avant le pied de page du TP principal.
- Illustration : `assets/hommage_nathalie_bd.png`.
- Image identifiée comme une illustration générée par IA, distincte d’une photographie authentique.
- Aucun formulaire, filtre ou exercice modifié volontairement.
- Avant toute diffusion publique, vérifier l’accord explicite de Nathalie pour la publication de ce portrait stylisé.
