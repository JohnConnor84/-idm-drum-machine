# IDM Drum Machine v0.1

IDM percussion instrument for Raspberry Pi 3B+ and Pure Data.

## Hardware

- Raspberry Pi 3B+
- PCM5102 I2S DAC
- HDMI display
- USB numeric keypad
- USB MIDI interface
- Korg nanoKONTROL (optional)
- Cirklon Sequentix MIDI clock source

## Features

- 16 percussion voices
- Up to 32 samples per voice
- Bank-based sample loading
- Random sample selection
- Probability
- Density
- Mutation
- Chaos
- Pitch variation
- Microtiming
- Per-voice LPF
- Per-voice reverb send
- MIDI Clock slave
- MIDI Start / Stop / Continue
- German / English interface
- CRT-style monochrome green interface
- Adjustable contrast and green tone
- Automatic startup

## Sample naming

Samples use the format:

VOICE.SAMPLE.wav

Example:

13.4.wav

Voice 13, sample 4.

## Bank structure

banks/ └── IDM_DARK/ ├── 1.1.wav ├── 1.2.wav ├── 2.1.wav ├── 13.1.wav ├── 13.2.wav ├── 13.3.wav ├── 13.4.wav └── 16.1.wav


## MIDI

Cirklon | v MIDI DIN | v USB MIDI Interface | v Raspberry Pi 3B+ | v Pure Data


The IDM Drum Machine follows external MIDI Clock when available.

## Keypad

- Num Lock = Start / Stop
- / = Bank Select
- 7 = Back
- 1 = LPF
- 3 = Reverb Send
- Enter = Confirm
- Arrow keys = Navigation
- +/- = Change value

## License

MIT
