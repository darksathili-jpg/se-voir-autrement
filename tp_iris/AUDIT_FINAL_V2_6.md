# IRIS/LAB — Audit final V2.6 (11 novembre 2026)

## Critères de livraison
- Référence : V2 originale / V2.5. Aucun des fichiers d’illustrations ni des photos sources n’a été modifié.
- **BLOQUANT CORRIGÉ** : en V2.5, la section d’intelligence artificielle était située **après** le conteneur `.wrap` et après le pied de page. Elle occupait toute la largeur de l’écran, ses trois colonnes débordaient et elle semblait constituer une seconde page non intégrée. La V2.6 la replace dans `.wrap`, **avant le pied de page**.
- **CORRIGÉ** : les trois images scientifiques de comparaison passent de `object-fit: cover` à `contain`, pour éviter de masquer des régions par recadrage implicite. Les légendes précisent la distinction entre fichier initial du smartphone, recadrage et interprétation générative.
- **CORRIGÉ** : comportement responsive de la grille à trois, deux puis une colonne selon largeur ; contrôles de contraste des légendes en mode clair et vidéoprojecteur.
- **CORRIGÉ** : distinction entre les consignes de photographie oculaire clinique de l’Iowa (différentes) et celles de sécurité choisies pour l’atelier ; aucune mise en évidence de faisceau lumineux direct dans le protocole scolaire.
- **PRÉCISÉ** : l’essai « pièce sombre + latérale + ×3 » décrit le matériel de l’enseignant et ne devient pas une règle universelle.
- **PRÉCISÉ** : les activités IA sont un approfondissement ; programme SNT en vigueur en 2026 : BO spécial n°1 du 22 janvier 2019 (source Éduscol).

## Limites à ne pas masquer
- La scène BD reste une illustration pédagogique, pas une mesure de distance ni un protocole de sécurité certifié.
- Une photographie produite par smartphone est déjà susceptible de traitements internes : la désignation « brute » ne signifie pas données RAW du capteur.
- L'image issue d'IA n'est pas une reconstitution anatomique fidèle. Aucune conclusion biologique ou identification biométrique n'en est tirée.
- Le TP ne doit pas exiger de photo personnelle d’un élève. Aucune photo d’élève ne doit être téléchargée vers une plateforme d’IA sans cadre institutionnel explicite.
- Le PDF mire est une cible pédagogique, pas une validation métrologique d’un système optique ou de la sécurité oculaire.

## Références vérifiées
- Éduscol, programme SNT en vigueur (février 2026) : https://eduscol.education.gouv.fr/5841/programmes-et-ressources-en-sciences-numeriques-et-technologie-voie-gt
- Ministère, révision 2027 : https://www.education.gouv.fr/le-conseil-superieur-des-programmes/revision-du-programme-de-sciences-numeriques-et-technologie-snt-de-seconde-505738
- Apple, mode macro basé sur l’ultra grand angle (modèles compatibles) : https://support.apple.com/fr-fr/guide/iphone/iphfaacf2eb0/ios
- University of Iowa Health Care : https://uihc.org/educational-resources/how-capture-images-and-video-your-eyes
- CNIL, autorisation de diffusion des photos d’élèves : https://cnil.fr/fr/cnil-direct/question/utilisation-des-photos-des-eleves-faut-il-laccord-des-parents
- MDN, règles d’accès aux pixels Canvas : https://developer.mozilla.org/fr/docs/Web/HTML/How_to/CORS_enabled_image

## Recette matérielle à effectuer au lycée
1. Extraire l’archive (ne pas ouvrir index.html directement à l'intérieur du ZIP), puis ouvrir index.html dans Chrome ou Edge.
2. Essayer les trois thèmes, à 100 % de zoom, et sur vidéoprojecteur.
3. Télécharger et imprimer la mire PDF : A4, taille réelle, vérifier à la règle la barre de 50 mm.
4. Importer une image locale dans le TP principal ; puis ouvrir l'atelier de pixels et vérifier les filtres et l'export PNG.
5. Vérifier la grille IA en bout de page : A/B/C entières, dans la même zone centrée, avant le pied de page.
6. En cas de problème avec `file://`, tester l’ouverture depuis le dossier avec un serveur local en dernier recours ; ne pas déclarer le mode hors ligne validé tant que la recette n'est pas faite sur le poste réel.
