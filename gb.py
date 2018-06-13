"""Copyright 2015, Bill Dengler
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import winsound
from datetime import datetime


def mknoise(sound):
    "Play a sound using the Windows sound API. Can be extended for other platforms."
    winsound.PlaySound(sound, winsound.SND_FILENAME)


def chime(hour, twelvehour=True):
    "Chime for the hour specified. Set twelvehour to True to enable twelve-hour chiming."
    # Sanity check input.
    if hour < 0 or hour > 23:
        raise ValueError("Hour must be between 0 and 23.")
    # Chime 24 times at midnight (in 24-hour mode)
    if not twelvehour:
        if hour == 0:
            hour = 24
    elif twelvehour:
        hour %= 12
        if hour == 0:
            hour = 12
    mknoise("gb_intro.wav")
    for _ in range(hour):
        mknoise("gb_chime.wav")


if __name__ == '__main__':
    mknoise("gb_intro.wav")
    while True:
        if datetime.now().minute == 0 and datetime.now().second == 0:
            chime(datetime.now().hour)
