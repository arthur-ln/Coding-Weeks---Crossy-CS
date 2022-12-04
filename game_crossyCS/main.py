from game import Game
import pygame
from pygame import mixer


# executer le main pour lancer le jeu

if __name__ == '__main__':
    game = Game()
    while game.running:
        game.curr_menu.display_menu()
        if game.playing == True:
            mixer.music.load('sounds/bgsound.wav')  # musique lorsque l'on joue
            mixer.music.play(-1)
            game.run()
            mixer.music.stop()  # on arrete la musique lorsque l'on re rentre dans le menu
