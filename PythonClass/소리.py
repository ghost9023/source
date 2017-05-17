# Assuming your file is a WAV:

from tkinter import *
from winsound import *

root = Tk() # create tkinter window

play = lambda: PlaySound('Sound.wav', SND_FILENAME)
button = Button(root, text = 'Play', command = play)

button.pack()
root.mainloop()


# Assuming your file is a MP3:

# from tkinter import *
# import mp3play
#
# root = Tk() # create tkinter window
#
# f = mp3play.load('Sound.mp3'); play = lambda: f.play()
# button = Button(root, text = 'Play', command = play)
#
# button.pack()
# root.mainloop()
#
# import mp3play
#
# filename = r'd:/data/BOMB.mp3'
# clip = mp3play.load(filename)
#
# clip.play()
#
# import time
# time.sleep(min(30, clip.seconds()))
# clip.stop()