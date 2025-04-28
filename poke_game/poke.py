# Poke the Dots V4
# This is a graphical game where two dots move around
# the screen, bouncing off the edges. The usser tries 

from uagame import Window
from random import randint
from pygame import QUIT, Color, MOUSEBUTTONUP, KEYDOWN, K_p
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():
    # create the window
    game = Game()
    # play game
    game.play()

# class game
class Game:
    # An object in this class represents a complete game
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_dot
    def __init__(self):
        self._window = Window('Poke the Dots', 500, 400)
        self._adjust_window()
        self._frame_rate = 90
        self._close_selected = False
        self._clock = Clock()
        self._small_dot = Dot('red', [50,75], 30, [1,2], self._window)
        self._big_dot = Dot('blue', [200,100], 40, [2,1], self._window)
        self._small_dot.randomize()
        self._big_dot.randomize()
        self._score = 0


    def _adjust_window(self):
        self._window.set_font_name('ariel')
        self._window.set_font_size(64)
        self._window.set_font_color('white')
        self._window.set_bg_color('black')

    
    def play(self):
        # while not player has selected close
        while not self._close_selected:
            # play frame
            #   handle events
            self.handle_events()
            #   draw game
            self.draw()
            #   update game
            self.update()
        self._window.close()


    def handle_events(self):
        event_list = get_events()
        # for event in event_list
        for event in event_list:
            self.handle_one_event(event)


    def handle_one_event(self, event):
        #   handle one event
        #       if event category equals close
        if event.type == QUIT:
            # remember play has selected close
            self._close_selected = True
        
        elif event.type == MOUSEBUTTONUP:
            self.handle_mouse_up(event)


    def handle_mouse_up(self, event):
        self._small_dot.randomize()
        self._big_dot.randomize()


    def draw(self):
        self._window.clear()
        self.draw_score()
        # draw small dot
        # draw big dot
        self._small_dot.draw()
        self._big_dot.draw()
        # update display
        self._window.update()


    def update(self):

        # move small dot
        self._small_dot.move()
        # move big dot
        self._big_dot.move()
        # control frame rate
        self._clock.tick(self._frame_rate)
        self._score = get_ticks() // 1000
        

    def draw_score(self):
        string = 'Score: ' +str(self._score)
        self._window.draw_string(string, 0, 0)

    
# class dot
class Dot:
    # An object in this class represents a colored circle that can move
    # - color
    # - center
    # - radius
    # - velocity
    # - window
    def __init__(self, color, center, radius, velocity, window):
        self._color = color
        self._center = center
        self._radius = radius
        self._velocity = velocity
        self._window = window


    def move(self):
        size = (self._window.get_width(), self._window.get_height())
        # for index in sequence 0 to 1
        for index in range(0,2):
            # update center at index
            #   add velocity at index to center at index
            self._center[index] = self._center[index] + self._velocity[index]
            #   if dot edge outside window
            if (self._center[index] < self._radius) or (self._center[index] + self._radius > size[index]):
            #if ((center[index] == radius) or (center[index] == size[index])):
                # neagte velocity at index
                self._velocity[index] = -self._velocity[index]


    def draw(self):
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius, 3)


    def randomize(self):
        size = (self._window.get_width(), self._window.get_height())
        for index in range (0, 2):
            self._center[index] = randint(self._radius, size[index] - self._radius)
main()