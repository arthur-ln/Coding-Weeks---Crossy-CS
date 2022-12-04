from pytest import *
from game_crossyCS import *
from game_crossyCS_grid.grid_crossyCS import adapted_list_with_char, create_list, get_position_char, new_hauteur_line_left, new_hauteur_line_right, new_largeur_line_down, new_largeur_line_up


def test_create_list():
    assert create_list(2, 3) == [[0, 0, 0], [0, 0, 0]]


def test_get_position_char():
    assert get_position_char(adapted_list_with_char()) == (7, 3)


def test_new_hauteur_line_right():
    list = adapted_list_with_char()
    largeur = len(list[0])
    list[0][largeur-1] = 3
    list = new_hauteur_line_right(list)
    assert list == [[0, 0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def test_new_hauteur_line_left():
    list = adapted_list_with_char()
    list[0][0] = 3
    list = new_hauteur_line_left(list)
    assert list == [[0, 3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def test_new_largeur_line_up():
    list = adapted_list_with_char()
    largeur = len(list[0])
    list[0][0] = 3
    list = new_largeur_line_up(list)
    assert list == [[0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def test_new_largeur_line_down():
    list = adapted_list_with_char()
    list[1][0] = 3
    list = new_largeur_line_down(list)
    assert list == [[3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
