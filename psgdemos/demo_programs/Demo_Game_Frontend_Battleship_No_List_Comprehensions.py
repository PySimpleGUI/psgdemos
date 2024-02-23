#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

def Battleship():
    sg.theme('Dark Blue 3')
    MAX_ROWS = MAX_COL = 10

    # Start building layout with the top 2 rows that contain Text elements
    layout =   [[sg.Text('BATTLESHIP', font='Default 25')],
                [sg.Text(size=(15,1), key='-MESSAGE-', font='Default 20')]]

    # Build the "board", a grid of Buttons
    board = []
    for row in range(MAX_ROWS):
        layout_row = []
        for col in range(MAX_COL):
            layout_row.append(sg.Button(str('O'), size=(4, 2), pad=(0,0), border_width=0, key=(row,col)))
        board.append(layout_row)

    # Add the board to the layout
    layout += board
    # Add the exit button as the last row
    layout += [[sg.Button('Exit', button_color=('white', 'red'))]]

    window = sg.Window('Battleship', layout)

    while True:         # The Event Loop
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if randint(1,10) < 5:           # simulate a hit or a miss
            window[event].update('H', button_color=('white','red'))
            window['-MESSAGE-'].update('Hit')
        else:
            window[event].update('M', button_color=('white','black'))
            window['-MESSAGE-'].update('Miss')
    window.close()

Battleship()
