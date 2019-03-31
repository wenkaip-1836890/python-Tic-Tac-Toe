'''Tic-Tac-Toe_Array_VIS_FOR_TK.py
Version of Aug. 29, 2018. Works with the formulation of
Tic-Tac-Toe that uses a State class for
representing states.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

myFont = None

WIDTH = 500
HEIGHT = 500
TITLE = 'Single-player Tic-Tac-Toe'


def initialize_vis():
    initialize_tk(WIDTH, HEIGHT, TITLE)


def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    print("In render_state, state is " + str(s))
    # Create the default array of colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (100, 100, 255)

    row = [white] * 3
    the_color_array = [row, row[:], row[:]]
    # Now create the default array of string labels.
    row = ['' for i in range(3)]
    the_string_array = [row, row[:], row[:]]

    for i in range(len(s.map)):
        for j in range(len(s.map[i])):
            if (s.map[i][j] == 1):
                the_color_array[i][j] = red
                the_string_array[i][j] = 'X'
            elif (s.map[i][j] == 2):
                the_color_array[i][j] = blue
                the_string_array[i][j] = 'O'
            else:
                the_color_array[i][j] = white

    caption = "Current state of the game. Textual version: " + str(s)
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    # print("the_state_array is: "+str(the_state_array))
    the_state_array.show()




