# this repo Work with librosa 0.9.0

package for doremi-sketch
```
https://github.com/jymh22/doremi-sketch
```

# and shoud use updated torchlibrosa
```
'pip install git+https://github.com/bellsky/torchlibrosa'
```
instead pip install librosa at requirements

# Piano transcription inference

This toolbox is a piano transcription inference package that can be easily installed. Users can transcribe their favorite piano recordings to MIDI files after installation. To see how the piano transcription system is trained, please visit: https://github.com/bytedance/piano_transcription.

## Demos
Here is a demo of our piano transcription system: https://www.youtube.com/watch?v=5U-WL0QvKCg

## Installation
The piano transcription system is developed with Python 3.7 and PyTorch 1.4.0 (Should work with other versions, but not fully tested).
Install PyTorch following https://pytorch.org/. Users should have **ffmpeg** installed to transcribe mp3 files.

```
pip install git+https://github.com/bellsky/piano_transcription_inference
```

Installation is finished! 

## Usage
Want to try it out but don't want to install anything? We have set up a [Google Colab](https://colab.research.google.com/github/qiuqiangkong/piano_transcription_inference/blob/master/resources/inference.ipynb).

```
python3 example.py --audio_path='resources/cut_liszt.mp3' --output_midi_path='cut_liszt.mid' --cuda
```

This will download the pretrained model from https://zenodo.org/record/4034264.
Base path_url is C:/Users/'username'/piano_transcription_inference_data/note_F1=0.9677_pedal_F1=0.9186

Users could also execute the inference code line by line:
```
from piano_transcription_bellsky import PianoTranscription, sample_rate, load_audio

# set audio_path
audio_path = ('Your_Path')

# Load audio
(audio, _) = load_audio(audio_path, sr=sample_rate, mono=True)

# Transcriptor
transcriptor = PianoTranscription(device='cpu', checkpoint_path=None)  # device: 'cuda' | 'cpu'

# Transcribe and write out to MIDI file   # second args is output file name. file will be saved at -
transcribed_dict = transcriptor.transcribe(audio, 'cut_liszt.mid')
```

## Visualization of piano transcription

**Demo.** Lang Lang: Franz Liszt - Love Dream (Liebestraum) [[audio]](resources/cut_liszt.mp3) [[transcribed_midi]](resources/cut_liszt.mid)

<img src="resources/cut_liszt.png">

## FAQs
This repo support Linux and Mac. Windows has not been tested.

If users met "audio.exceptions.NoBackendError", then check if ffmpeg is installed.

If users met the problem of "Killed". This is caused by there are not sufficient memory.

## Applications

We have built a large-scale classical piano MIDI dataset https://github.com/bytedance/GiantMIDI-Piano using our piano transcription system.

## Cite
[1] High-resolution Piano Transcription with Pedals by Regressing Onsets and Offsets Times, [To appear], 2020
