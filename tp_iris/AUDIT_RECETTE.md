# Audit de mise en service — TP IRIS V2.2
Date : 11 novembre 2026

## Verdict
**Correctif livré, mais validation finale en classe encore conditionnée au test sur le matériel réel.** Les tests automatisés directs du module de filtres ont réussi dans Chromium via injection en mémoire. La navigation `file://` et `http://localhost` par Playwright est bloquée administrativement sur cette session : aucun contrôle bout en bout de l’ouverture de `index.html` dans ce contexte n'est revendiqué.

## Défauts détectés et corrigés
1. **Référence photographique trompeuse :** l'image synthétique d'iris était affichée comme référence. Remplacée par un extrait géométrique de la photographie n°2 réelle, sans génération de détails. L'image complète reste disponible.
2. **Lecture de pixels fragile hors ligne :** les JPEG relatifs d'un canevas peuvent devenir illisibles via `getImageData()` selon les règles d'origine des fichiers locaux. Les quatre démonstrations sont désormais intégrées dans la page comme données d'image ; aucun serveur requis.
3. **Cadrage inadéquat :** défaut centré sur l'œil complet. L'atelier démarre sur l'extrait circulaire de la photo 2, avec possibilité d'étudier aussi la photo complète.
4. **Déformation :** canvas rectangulaire 640×550 dans un conteneur carré. Corrigé en 640×640.
5. **Durée trompeuse :** le module ajouté dépassait la séance de 60 min. Il est marqué facultatif (20 à 30 min supplémentaires).
6. **Éclairage :** l'essai « super macro ×3 / pièce sombre / éclairage artificiel latéral » est documenté comme expérience du professeur, non comme méthode obligatoire pour les élèves ; lumière douce indirecte, sans flash/torche/laser dirigés vers l'œil.
7. **Distance sur la BD :** mention 20–30 cm illustratrice, non seuil de sécurité ou distance minimale de mise au point. Correction textuelle adjacent au visuel, sans altérer la BD approuvée.

## Tests exécutés
- syntaxe JavaScript des cinq scripts des deux pages : OK (`node --check`)
- ouverture du module HTML injecté en mémoire dans Chromium : OK, zéro exception JavaScript
- chargement des 4 photographies incorporées : OK, dimensions lues correctement
- 7 modes (original + six filtres) : OK, calcul de pixel observé pour chacun
- réinitialisation du filtre : OK
- questionnaire 4/4 : OK
- export PNG : OK, téléchargement observé
- intégrité de l'archive ZIP et présence des médias : contrôlées par script
- identité binaire des quatre images originales de la V2 : contrôlée par empreinte SHA-256

## Recette sur l'ordinateur de classe — à réaliser avant les élèves
1. Décompresser l'archive ; ouvrir **index.html**, vérifier la BD et les six étapes.
2. Basculer Sombre, Clair puis Projecteur. Contrôler surtout les contrastes sur vidéoprojecteur.
3. Aller aux filtres ; vérifier que l'iris circulaire provient de la photo 2, pas de l'image synthétique.
4. Choisir Photo 2 complète, puis Photo 1 et Photo 3 ; vérifier la mise à jour.
5. Sélectionner Niveaux de gris, Contraste, Flou, Netteté, Sobel, Fausses couleurs ; déplacer le curseur à chaque fois ; revenir à Original.
6. Importer une photo d'essai non personnelle ; vérifier l'inspecteur de pixels et le PNG.
7. Tester le bilan, le questionnaire, l'impression et la progression (retour possible au parcours après l'atelier).
8. Vérifier que les politiques du navigateur autorisent iframe, téléchargement et fichiers locaux. En cas d'interdiction du cadre, ouvrir **atelier_pixels.html** directement depuis le même dossier.
9. Aucun élève ne doit être photographié sans consentement et protocole d'établissement ; participation sur exemples possible ; ne pas publier les photographies d'iris.

## Limites et non-preuves
- La manipulation de l'iris extrait est un masquage circulaire **approximatif**, pas une segmentation biométrique fiable.
- Accentuation et contraste ne créent pas de détails optiques authentiques.
- La galerie d'origine présente l'image originale synthétique uniquement comme fichier conservé non affiché ; il ne faut pas l'utiliser pour une analyse scientifique.
- Les navigateurs, smartphones de la classe et le projecteur n'ont pas été testés physiquement dans cette session.
