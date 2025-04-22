# Poke the Dots V3
# This is a graphical game where two dots move around
# the screen, bouncing off the edges
from uagame import Window
from random import randint
import pygame
from pygame import QUIT, Color, MOUSEBUTTONUP, KEYDOWN, K_p
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():
    # create the window
    window =create_window()
    game = create_game(window)
    # play game
    play_game(game)
    # close window
    window.close()


def create_window():
    # Create a window for the game, open it, and return it
    window = Window('Poke the Dots', 500, 400)
    window.set_font_size(64)
    window.set_font_color('white')
    window.set_bg_color('black')
    return window

def create_game(window,):
    # Create a Game object for poke the dots
    game = Game()
    game.window = window
    game.frame_rate = 90
    game.close_selected = False
    game.clock = Clock()
    game.small_dot = create_dot('red', [50,75], 30, [1,2], window)
    game.big_dot = create_dot('blue', [200,100], 40, [2,1], window)
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)
    game.score = 0
    return game

def create_dot(color, center, radius, speed, window):
    dot = Dot()
    dot.color = color
    dot.center = center
    dot.radius = radius
    dot.velocity = speed
    dot.window = window
    return dot

def play_game(game):
    
    # while not player has selected close
    while not game.close_selected:
        # play frame
        #   handle events
        handle_events(game)
        #   draw game
        draw_game(game)
        #   update game
        update_game(game)
    


def handle_events(game):
    
    event_list = get_events()
    # for event in event_list
    for event in event_list:
        #   handle one event
        #       if event category equals close
        if event.type == QUIT:
            # remember play has selected close
            game.close_selected = True
        
        elif event.type == MOUSEBUTTONUP:
            handle_mouse_up(game)

        elif event.type == KEYDOWN:
            if event.key == K_p:
                handle_mouse_up(game)


def handle_mouse_up(game):
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)

def draw_game(game):
    game.window.clear()
    draw_score(game)
    # draw small dot
    # draw big dot
    draw_dot(game.small_dot)
    draw_dot(game.big_dot)
    # update display
    game.window.update()

def draw_score(game):
    string = 'Score: ' +str(game.score)
    game.window.draw_string(string, 0, 0)

def update_game(game):

    # move small dot
    move_dot(game.small_dot)
    # move big dot
    move_dot(game.big_dot)
    # control frame rate
    game.clock.tick(game.frame_rate)
    game.score =get_ticks() // 1000

def draw_dot(dot):
    surface = dot.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius, 3)

def move_dot(dot):
    size = (dot.window.get_width(), dot.window.get_height())
    # for index in sequence 0 to 1
    for index in range(0,2):
        # update center at index
        #   add velocity at index to center at index
        dot.center[index] = dot.center[index] + dot.velocity[index]
        #   if dot edge outside window
        if (dot.center[index] < dot.radius) or (dot.center[index] + dot.radius > size[index]):
        #if ((center[index] == radius) or (center[index] == size[index])):
            # neagte velocity at index
            dot.velocity[index] = -dot.velocity[index]


def randomize_dot(dot):
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range (0, 2):
        dot.center[index] = randint(dot.radius, size[index] - dot.radius)
# class game
class Game:
    # An object in this class represents a complete game
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_dot
    pass

# class dot
class Dot:
    # An object in this class represents a colored circle that can move
    # - color
    # - center
    # - radius
    # - velocity
    # - window
    pass

main()