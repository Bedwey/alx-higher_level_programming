#!/usr/bin/python3
for ch in range(-122, -96):
    print(chr(abs(ch)) if abs(ch) % 2 == 0 else chr(abs(ch) - 32), end="")
