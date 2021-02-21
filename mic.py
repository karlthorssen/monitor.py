#!/usr/bin/env python
# forked from https://gist.github.com/PRosenb/2ce5159a334af203fca7ef06501775f0
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
OUT =  'BlackHole 16ch'
IN = 'Q9-1'


output = sd.OutputStream(channels=16, blocksize=0, latency="low", device=OUT)
output.start()

# array stuff is fine
def input_callback(indata, frames, time, status):
    output.write(np.ascontiguousarray(
        np.pad(
            np.concatenate((indata, indata), axis=1),
               ((0, 0), (6, 8)),
               'constant',
               constant_values=0)
    ))

with sd.InputStream(channels=1, callback=input_callback, blocksize=0, latency="low", device=IN):
    print('#' * 80)
    print('press Return to quit')
    print('#' * 80)
    if sys.version_info[0] < 3:
        raw_input()
    else:
        input()
