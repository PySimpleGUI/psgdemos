import PySimpleGUI as sg

"""
    Demo Element Justification In A Window Using Stretch Elements

    How to Justify elements on 1 row to be left, right or left, middle, right

    Additionally, locate these buttons at the bottom of the screen


    To get 2 buttons to be all the way to the left and to the far right, then
        you want to place a Stretch element between them that expands
    If you want a third button that is centered, then add TWO Stretch elements, one
        on each side of the middle one

    Copyright 2021-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


layout = [  [sg.Text('Window with elements on the left and the right')],
            [sg.T('Using a Stretch element that expands enables you to "push" other elements around')],
            [sg.HorizontalSeparator()],
            [sg.VStretch()],   # Stretch verticaly
            [sg.Button('Left'), sg.Stretch(), sg.Button('Right')],
            [sg.Stretch(), sg.B('Right')],
            [sg.Button('Left'), sg.Stretch(), sg.B('Middle'),  sg.Stretch(),  sg.Button('Right')]  ]

window = sg.Window('Left and Right Justification', layout, resizable=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
