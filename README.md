Split Record
------------
Given a recording (such as from vinyl discs) in any ffmpeg-supported
audio format (ideally something lossless like WAV or flac), split-record
splits the single recording into multiple MP3 files.

Suggested usage: cat tracklist.txt | ./split-record.py

Tracklist is read from stdin and is begins with the name of a
side (which is used as the input filename) followed by one line for each
track, consisting of track number, name, and duration.
Sides are separated by a newline.

For example:
```
Artist Album - Side 1.mp3
1 Track Name One 1:23
2 Track Name Two 3:11

Artist Album - Side 2.mp3
3 Track Name Three 0:34
4 Track Name Four 4:23
```
