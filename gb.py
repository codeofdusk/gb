#Copyright 2015, Bill Dengler
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
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