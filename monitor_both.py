#!/usr/bin/env python
# forked from https://gist.github.com/PRosenb/2ce5159a334af203fca7ef06501775f0
# routes audio from multiple blackhole channels to speakers
# This allows me to set blackhole as system output, so I can capture it
# in other programs and route DAW output where it needs to go.
import sounddevice as sd
import numpy as np
import sys

# Download the pkg file of BlackHole
# https://github.com/ExistentialAudio/BlackHole/releases
# Install BlackHole
#
# Install sounddevice
# pip install sounddevice --user
#
# Make file executable
# chmod +x ./monitor.py
#

# Check with the following command what name the Built-in Output device has
# python -m sounddevice
IN =  'BlackHole 16ch'
OUT = 'Built-in Output'

output = sd.OutputStream(channels=2, blocksize=0, latency="low", device=OUT)
output.start()

def input_callback(indata, frames, time, status):
    output.write(np.ascontiguousarray(
        indata[:, [0,1]] + # PA
        indata[:, [2,3]] + # cue
        indata[:, [8,9]])) # system output, configure as blackhole with stereo settings
                           # i.e. set blackhole as output in system preferences, then
                           # open audio midi setup, choose blackhole->configure speakers
                           # set left as channel 7 and right as channel 8 (1-indexed there and
                           # 0-indexed in numpy)

with sd.InputStream(channels=16, callback=input_callback, blocksize=0, latency="low", device=IN):
    print('#' * 80)
    print('press Return to quit')
    print('#' * 80)
    if sys.version_info[0] < 3:
        raw_input()
    else:
        input()
