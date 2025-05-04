from game.game_manager import GameManager
import pygame
import sys

def main():
    pygame.init()
    gm=GameManager()
    gm.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()







