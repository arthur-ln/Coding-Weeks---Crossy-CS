# list fera réference à la liste qui contient les éléments, grid fera réference à la grille affichée proprement

def create_list(hauteur, largeur):  # on crée la liste vide
    list = [[0 for j in range(largeur)] for i in range(hauteur)]
    return list


def adapted_list_with_char():  # liste de départ avec le personnage placé à sa position initiale
    list = create_list(10, 7)
    list[7][3] = 1
    return list


def line_equal(largeur, grid):  # crée une ligne de = pour la grille
    for k in range(largeur):
        grid = grid+" ==="
    grid = grid + "\n"
    return grid


# crée une interligne entre les deux lignes de égal
def interline(largeur, grid, list, hauteur_position):
    for largeur_position in range(largeur):
        value = list[hauteur_position][largeur_position]
        if value == 0:
            grid = grid+"|   "
        elif value == 1:
            grid = grid+"| X "
    grid = grid+"|\n"
    return grid


def display_grid(list):  # affiche la grille obtenue
    largeur = len(list[0])
    hauteur = len(list)
    grid = ""
    for hauteur_position in range(hauteur):
        grid = line_equal(largeur, grid)
        grid = interline(largeur, grid, list, hauteur_position)
    grid = line_equal(largeur, grid)
    return grid


def get_position_char(list):
    largeur = len(list[0])
    hauteur = len(list)
    for hauteur_position in range(hauteur):
        for largeur_position in range(largeur):
            if list[hauteur_position][largeur_position] == 1:
                return hauteur_position, largeur_position


def new_hauteur_line_right(list):
    largeur = len(list[0])
    hauteur = len(list)
    # la ligne que l'on va insérer sur la droite
    insert_line = [0 for i in range(hauteur)]
    for hauteur_position in range(hauteur):
        for largeur_position in range(largeur-1):
            list[hauteur_position][largeur_position] = list[hauteur_position][largeur_position+1]
        list[hauteur_position][largeur-1] = insert_line[hauteur_position]
    return list


def new_hauteur_line_left(list):
    largeur = len(list[0])
    hauteur = len(list)
    # la ligne que l'on va insérer sur la droite
    insert_line = [0 for i in range(hauteur)]
    for hauteur_position in range(hauteur):
        # pour la boucle il faut retenir une valeur value_mem à chaque fois
        value_mem = list[hauteur_position][0]
        list[hauteur_position][0] = insert_line[hauteur_position]
        for largeur_position in range(1, largeur):
            list[hauteur_position][largeur_position], value_mem = value_mem, list[hauteur_position][largeur_position]
    return list


def new_largeur_line_up(list):  # analogue de new_hauteur_line_left
    largeur = len(list[0])
    hauteur = len(list)
    insert_line = [0 for i in range(largeur)]
    value_mem = list[0]
    list[0] = insert_line
    for hauteur_position in range(1, hauteur):
        list[hauteur_position], value_mem = value_mem, list[hauteur_position]
    return list


def new_largeur_line_down(list):  # analogue de new_hauteur_line_right
    largeur = len(list[0])
    hauteur = len(list)
    insert_line = [0 for i in range(largeur)]
    list[hauteur-1] = insert_line
    for hauteur_position in range(hauteur-1):
        list[hauteur_position] = list[hauteur_position+1]
    return list


def interchange_position(list, hauteur_position, largeur_position, direction):
    if direction == "down":
        list[hauteur_position][largeur_position], list[hauteur_position+1][largeur_position] = list[
            hauteur_position+1][largeur_position], list[hauteur_position][largeur_position]
    elif direction == "up":
        list[hauteur_position][largeur_position], list[hauteur_position-1][largeur_position] = list[
            hauteur_position-1][largeur_position], list[hauteur_position][largeur_position]
    elif direction == "right":
        list[hauteur_position][largeur_position], list[hauteur_position][largeur_position+1] = list[
            hauteur_position-1][largeur_position+1], list[hauteur_position][largeur_position]
    elif direction == "left":
        list[hauteur_position][largeur_position], list[hauteur_position][largeur_position-1] = list[
            hauteur_position][largeur_position-1], list[hauteur_position][largeur_position]
    return list


# il peut retourner en arrière mais cela ne créera jamais de nouvelles lignes et on met des conditions sur les frontières du jeu et le déplacement
def move_char_without_obstacles(list, move):
    hauteur_position, largeur_position = get_position_char(list)
    largeur = len(list[0])
    hauteur = len(list)
    if move == "down":
        if hauteur_position != hauteur-1:
            interchange_position(list, hauteur_position,
                                 largeur_position, "down")
            return list
    if move == "up":
        if hauteur_position <= 2:
            list = new_largeur_line_up(list)
            hauteur_position += 1
        interchange_position(list, hauteur_position, largeur_position, "up")
        return list
    if move == "left":
        if largeur_position <= 2:
            list = new_hauteur_line_left(list)
            largeur_position += 1
        interchange_position(list, hauteur_position, largeur_position, "left")
        return list
    if move == "right":
        if largeur_position >= largeur-3:
            list = new_hauteur_line_right(list)
            largeur_position -= 1
        interchange_position(list, hauteur_position, largeur_position, "right")
        return list


def display_move_char_without_obstacles(list, move):
    list = move_char_without_obstacles(list, move)
    if list == None:
        return "Tu as perdu"
    else:
        return display_grid(list)

        # test pour voir si cela marche


list = adapted_list_with_char()
print(display_grid(list))
print(display_move_char_without_obstacles(list, "right"))
print(display_move_char_without_obstacles(list, "right"))
print(display_move_char_without_obstacles(list, "up"))
print(display_move_char_without_obstacles(list, "left"))
print(display_move_char_without_obstacles(list, "down"))
print(display_move_char_without_obstacles(list, "down"))
print(display_move_char_without_obstacles(list, "down"))
print(display_move_char_without_obstacles(list, "down"))


# implémentation d'un dictionnaire pour préciser l'environnement et la nature de l'obstacle


def largeur_generate_line(list):
    largeur = len(list[0])
