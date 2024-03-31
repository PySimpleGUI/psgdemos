#!/usr/bin/env python
import PySimpleGUI as sg

# Only need these imports if using JPGs
from PIL import Image
from io import BytesIO


"""
    Demo of Net API - Download JPG Image using net_download_file_binary and display in a window
    
    The download is the easiest part.  It's the displaying of a JPG that's tricky.

    
    Copyright 2018-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


sg.theme('black')

# Download the binary file (into a variable, not a local file)

jpg_data = sg.net_download_file_binary(r'https://pysimplegui.net/images/tests/powered-by-pysimplegui-5.jpg')

# Now display a JPG image. It requires converting the image to PNG before using with PySimpleGUI
jpg_image = Image.open(BytesIO(jpg_data))

with BytesIO() as bio:
    jpg_image.save(bio, format='PNG')
    data = bio.getvalue()

sg.Window('Download JPG', [[sg.Image(data=data)]],
          use_custom_titlebar=True, titlebar_background_color='black', titlebar_text_color='white').read(close=True)
