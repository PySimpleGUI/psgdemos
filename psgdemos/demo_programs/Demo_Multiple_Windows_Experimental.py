#!/usr/bin/env python
import PySimpleGUI as sg

'''
  Parallel windows executing.
  
  Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
  
  Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
  
  You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
'''

layout1 = [[ sg.Text('Window 1') ],
           [sg.Input('')],
          [ sg.Button('Read')]]

window1 = sg.Window('My new window', layout1, location=(800,500))


layout2 = [[ sg.Text('Window 2') ],
           [sg.Input('')],
          [ sg.Button('Read')]]

window2 = sg.Window('My new window', layout2, location=(800, 625), return_keyboard_events=True)


layout3 = [[ sg.Text('Window 3') ],
           [sg.Input(do_not_clear=False)],
          [ sg.Button('Read')]]

window3 = sg.Window('My new window', layout3, location=(800,750), return_keyboard_events=True)


while True:     # Event Loop
    event, values = window1.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    elif event != '__timeout__':
        print(event, values)

    event, values = window2.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    elif event != '__timeout__':
        print(event, values)

    event, values = window3.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    elif event != '__timeout__':
        print(event, values)

window1.close()
window2.close()
window3.close()