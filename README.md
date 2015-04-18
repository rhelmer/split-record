Split Record
------------
Given a recording (such as from vinyl discs) and a tracklist in any
ffmpeg-supported audio format, split-record splits the single
recording into multiple MP3 files.

Suggested usage: cat tracklist.txt | ./split.py > run.sh
Then inspect and execute run.sh

Tracklist is read from stdin and is begins with the name of a
side (which is used as the input filename) followed by one line for each
track, consisting of track number, name, and duration.
Sides are separated by a newline.
For example:

```
SIDE1
1 Track Name One 1:23
2 Track Name Two 3:11

SIDE1
3 Track Name Three 0:34
4 Track Name Four 4:23
```