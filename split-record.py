#!/usr/bin/env python

import datetime
import os
import time
import subprocess
import sys

if os.isatty(0):
    print 'tracklist on stdin required!'
    sys.exit(1)

sides = {}
tracks = []
firstline = True
for line in sys.stdin:
    if line == '\n':
        sides[sidename] = tracks
        tracks = []
        firstline = True
        continue
    if firstline:
        sidename = line.strip()
        firstline = False
    else:
        line = line.strip()
        num = line.split()[0]
        name = ' '.join(line.split()[:-1])
        time = line.split()[-1]
        tracks.append((num, name, time))
sides[sidename] = tracks

for side in sides:
    seek = datetime.timedelta()
    for track in sides[side]:
        (num, name, time) = track
        t = datetime.datetime.strptime(time, '%M:%S')
        subprocess.call(
            ['ffmpeg', '-i' ,'%s' % side, '-ss', '%s' % seek,
             '-t', '%s' %time, '%s.mp3' % name]
        )
        delta = datetime.timedelta(minutes=t.minute, seconds=t.second)
        seek += delta
