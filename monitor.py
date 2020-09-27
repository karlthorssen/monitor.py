#!/usr/bin/env python
import sounddevice as sd
import sys

# Download the pkg file of BlackHole
# https://github.com/ExistentialAudio/BlackHole/releases
# Install BlackHole
#
# Install sounddevice
# pip install sounddevice --user
#
# Make file executable
# chmod +x ./forwardSound.py
#
# Click on Mac volume control (on top) and choose 'Output Device': 'BlackHole 16ch'
#
# Check with the following command what name the Built-in Output device has
# python -m sounddevice
sd.default.device = 'BlackHole 16ch', 'Built-in Output'

frames = 10

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    # if frames > 0:
    #     print(indata)
    #     frames = frames - 1
    # if outdata[0][0] != 0:
    #     import ipdb;ipdb.set_trace()
    outdata[:] = indata[:, [2,3]]

with sd.Stream(channels=(6, 2), callback=callback, blocksize=0, latency="low"):
    print('#' * 80)
    print('press Return to quit')
    print('#' * 80)
    if sys.version_info[0] < 3:
        raw_input()
    else:
        input()
