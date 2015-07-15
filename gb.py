import winsound, sys, time
from datetime import datetime
def mknoise(sound):
    "Make some noise."
    winsound.PlaySound(sound,winsound.SND_FILENAME)

def chime(hour,twelvehour=True):
    "Chime for the hour specified. Set twelvehour to True to enable twelve-hour chiming."
    if twelvehour and hour == 0:
        hour=12
    if twelvehour and hour > 12:
        hour-=12
    mknoise("gb_intro.wav")
    for i in range(hour):
        mknoise("gb_chime.wav")

if __name__ == '__main__':
    #Hack to play intro.
    chime(0,twelvehour=False)
    print "Firing on all cylinders!"
    while True:
        time.sleep(0.1)
        if datetime.now().minute == 0 and datetime.now().second == 0:
            chime(datetime.now().hour)