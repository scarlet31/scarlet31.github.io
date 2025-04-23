from midiutil import MIDIFile
import pygame
import time

# === Create MIDI ===
midi = MIDIFile(numTracks=4)

# General settings
tempo = 120
track_names = ["Piano", "SynthPad", "Bass", "Drums"]
channels = [0, 1, 2, 9]  # 9 is for drums

# Tempo and track names
for i, name in enumerate(track_names):
    midi.addTrackName(i, 0, name)
    midi.addTempo(i, 0, tempo)

# Track 0: Piano Melody
melody = [60, 62, 64, 67, 69, 67, 64, 62]
for i, note in enumerate(melody):
    midi.addNote(0, channels[0], note, i * 0.5, 0.5, 100)

# Track 1: Synth Pad (Chords)
chords = [[60, 64, 67], [62, 65, 69], [59, 62, 67], [57, 60, 64]]
for i, chord in enumerate(chords):
    for note in chord:
        midi.addNote(1, channels[1], note, i * 2, 2, 80)

# Track 2: Bass
bassline = [36, 36, 35, 33]
for i, note in enumerate(bassline):
    midi.addNote(2, channels[2], note, i * 2, 2, 90)

# Track 3: Drums (Kick, Snare, Hi-Hat)
drum_notes = [36, 38, 42, 38]
for i, note in enumerate(drum_notes):
    midi.addNote(3, channels[3], note, i * 0.5, 0.5, 110)

# Save file
filename = "neon_ghost.mid"
with open(filename, "wb") as output_file:
    midi.writeFile(output_file)

# === Play MIDI ===
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

# Wait until playback finishes
while pygame.mixer.music.get_busy():
    time.sleep(0.5)

pygame.quit()
