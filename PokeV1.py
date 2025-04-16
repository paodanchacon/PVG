# Poke the Dots V1
# This is a graphical game where two dots mov around
# the screen, bouncing off the edges
from uagame import Window
import pygame
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():
    # create the window
    window =create_window()
    # create the game
    #   create clock
    clock = Clock()
    #   create small dot
    small_color = 'blue'
    small_radius = 30
    small_center = [50,75]
    small_velocity = [1,2]
    #   create big dot
    big_color = 'green'
    big_radius = 40
    big_center = [200,100]
    big_velocity = [2,1]
    # play game
    play_game(window, big_color, big_center, big_radius, big_velocity, clock, small_color, small_center, small_radius, small_velocity)
    # close window
    window.close()


def create_window():
    # Create a window for the game, open it, and return it
    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    return window


def play_game(window, big_color, big_center, big_radius, big_velocity, clock, small_color, small_center, small_radius, small_velocity):
    close_selected = False
    # while not player has selected close
    while not close_selected:
        # play frame
        #   handle events
        close_selected = handle_events()
        #   draw game
        draw_game(window, big_color, big_center, big_radius, small_color, small_center, small_radius)
        #   update game
        update_game(window, big_center, big_radius, big_velocity, clock, small_color, small_center, small_radius, small_velocity)
    


def handle_events():
    closed = False
    event_list = get_events()
    # for event in event_list
    for event in event_list:
        #   handle one event
        #       if event category equals close
        if event.type == QUIT:
            # remember play has selected close
            closed = True
    return closed


def draw_game(window, big_color, big_center, big_radius, small_color, small_center, small_radius):
    window.clear()
    # draw small dot
    # draw big dot
    draw_dot(window, big_color, big_center, big_radius)
    draw_dot(window, small_color, small_center, small_radius)
    # update display
    window.update()



def update_game(window, big_center, big_radius, big_velocity, clock, small_color, small_center, small_radius, small_velocity):
    frame_rate = 90
    # move small dot
    move_dot(window, small_center, small_radius, small_velocity)
    # move big dot
    move_dot(window, big_center, big_radius, big_velocity)
    # control frame rate
    clock.tick(frame_rate)

def draw_dot(window, color_string, center, radius):
    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)

def move_dot(window, center, radius, velocity):
    size = (window.get_width(), window.get_height())
    # for index in sequence 0 to 1
    for index in range(0,2):
        # update center at index
        #   add velocity at index to center at index
        center[index] = center[index] + velocity[index]
        #   if dot edge outside window
        if (center[index] <= radius) or (center[index] + radius >= size[index]):
            # neagte velocity at index
            velocity[index] = -velocity[index]

main()