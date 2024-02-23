#!/usr/bin/env python
import PySimpleGUI as sg
from chatterbot import ChatBot
import chatterbot.utils
from gtts import gTTS
from pygame import mixer
import time
import os

'''
Demo_Chatterbot.py


Note - this code was written using version 0.8.7 of Chatterbot... to install:

python -m pip install chatterbot==0.8.7

It still runs fine with the old version. 

A GUI wrapped around the Chatterbot package.
The GUI is used to show progress bars during the training process and
to collect user input that is sent to the chatbot.  The reply is displayed in the GUI window

Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
'''

# Create the 'Trainer GUI'
# The Trainer GUI consists of a lot of progress bars stacked on top of each other
sg.theme('NeutralBlue')
# sg.DebugWin()
MAX_PROG_BARS = 20              # number of training sessions
bars = []
texts = []
training_layout = [[sg.Text('TRAINING PROGRESS', size=(20, 1), font=('Helvetica', 17))], ]
for i in range(MAX_PROG_BARS):
    bars.append(sg.ProgressBar(100, size=(30, 4)))
    texts.append(sg.Text(' ' * 20, size=(20, 1), justification='right'))
    training_layout += [[texts[i], bars[i]],]       # add a single row

training_window = sg.Window('Training', training_layout)
current_bar = 0

# callback function for training runs
def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    global current_bar
    global bars
    global texts
    global training_window
    # update the window and the bars
    button, values = training_window.read(timeout=0)
    if button is None:       # if user closed the window on us, exit
        return
    if bars[current_bar].update_bar(iteration_counter, max=total_items) is False:
        return
    texts[current_bar].update(description)      # show the training dataset name
    if iteration_counter == total_items:
        current_bar += 1

def speak(text):
    global i
    tts = gTTS(text=text, lang='en',slow=False)
    tts.save('speech{}.mp3'.format(i%2))
    # playback the speech
    mixer.music.load('speech{}.mp3'.format(i%2))
    mixer.music.play()
    # wait for playback to end
    while mixer.music.get_busy():
        time.sleep(.1)
    mixer.stop()
    i += 1

i = 0
mixer.init()

# redefine the chatbot text based progress bar with a graphical one
chatterbot.utils.print_progress_bar = print_progress_bar

chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

################# GUI #################

layout = [[sg.Multiline(size=(80, 20), reroute_stdout=True, echo_stdout_stderr=True)],
          [sg.MLine(size=(70, 5), key='-MLINE IN-', enter_submits=True, do_not_clear=False),
           sg.Button('SEND', bind_return_key=True), sg.Button('EXIT')]]

window = sg.Window('Chat Window', layout,
                   default_element_size=(30, 2))

# ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
while True:
    event, values = window.read()
    if event != 'SEND':
        break
    string = values['-MLINE IN-'].rstrip()
    print('  ' + string)
    # send the user input to chatbot to get a response
    response = chatbot.get_response(values['-MLINE IN-'].rstrip())
    print(response)

window.close()