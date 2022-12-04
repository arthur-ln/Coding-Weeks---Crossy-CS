# Crossy CS

Projet Coding-Weeks semaine 2

Bienvenue dans ce projet !

Nous sommes Pauline Elizalde, Basile Heurtault, Ruben Cizallet, Chenghao Lyu, Arthur Leene et Diane Dufetelle élèves en première année à CS

## Principe du projet 
Coder une version simplifiée du jeu Crossy Roads qui consiste à contrôler un personnage avançant case par case devant éviter un certain nombre d'obstacles (arbres qui bloquent, traverser une route sans se faire écraser, traverser une rivière sans tomber dans l'eau en passant sur des rondins). L'écran avance de plus en plus vite pour forcer le personnage à avancer ; s'il n'avance pas assez vite et sort de l'écran, alors il meurt. 

_Quoi?_
Ecran de jeu dans lequel seront placés différents obstacles (arbres, voitures, rivière) à franchir
L'utilisateur joue via le déplacement d'un personnage dans cet écran en lui demandant une direction parmi (bas, haut, droite, gauche)
Le jeu se termine lorsque le personnage entre en collision avec une voiture ou tombe dans la rivière ou lorsqu'il n'avance pas assez vite

_Pourquoi?_ 
Jouer à un jeu de type arcade

_Pour qui?_
Utilisateur souhaitant se distraire en jouant à un jeu de type arcade

### Notre fonctionnement : qualité du code

- Utilisation de la bibliothèque pygame
- Dossier "graphic" contenant les différents éléments graphiques, le joueur, les voitures
- Dossier "game_crossyCS" avec les différents fichiers : __init__.py, game.py, main.py, player.py, textual_crossyCS.py
- Différentes classes (player, car) 
- Utilisation de sprites (mouvement, gérer les collisions avec rect (rectangle de l'espace occupé par le sprite))
- On a généré une carte tmx (package pytmx)
- Package pyscroll pour le déplacement du joueur
- Utilisation de tiles pour gérer la position, la taille des différents éléments et le déplacement dans la map

### Sous-tâches
- Carte graphique
- Apparition et déplacement du joueur
- Différents obstacles et collision
- Déplacement des voitures et collision
- Ecran défilant pour forcer le joueur à avancer
- Si le joueur entre en collision avec une voiture, tombe dans la rivière ou sort de l'écran défilant alors il y a game over (apparition d'un écran "game over")
- Ecran d'accueil à presser pour pouvoir jouer proposant différentes options : plusieurs niveaux de jeu, plusieurs musiques

### Nos différents MVP
- Grille type 2048 (file grid_crossyCS.py) avec le joueur réprésenté par une croix. Il avance avec les commandes up, down, right, left. La grille s'auto-regénère si il se déplace trop sur la gauche ou la droite. Il y a fin du jeu si le joueur atteint le haut de la grille > Mais MVP non réutilisable avec pygame
- Deuxième MVP : sans les tiles et sans carte graphique mais avec des voitures se déplaçant et la possibilité de déplacer le personnage, génère des routes de manière aléatoire et il y a du son (déplacement, collision avec une voiture)
- Troisième MVP : notre MVP final avec les tiles
