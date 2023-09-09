import mutagen
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack
from mutagen.wave import WAVE
from mutagen.id3 import TextFrame
from mutagen.wavpack import WavPackHeaderError
from mutagen.id3 import TALB
from mutagen import MutagenError
from mutagen.mp3 import MP3
import os
from tqdm import tqdm

input_path = r'E:\同人音声合集'

folders = os.listdir(input_path)

index = 0
for folder in tqdm(folders):
    for (root, dirs, files) in os.walk(os.path.join(input_path, folder)):
        for file in files:
            if not file.endswith('.flac') and not file.endswith('.mp3') and not file.endswith('.wav'):
                continue
            if file.endswith('.flac'):
                try:
                    audio = FLAC(os.path.join(root, file))
                except Exception as e:
                    print(e)
            elif file.endswith('.mp3'):
                try:
                    audio = MP3(os.path.join(root, file))
                except Exception as e:
                    print(e)
            elif file.endswith('.wav'):
                try:
                    audio = WAVE(os.path.join(root, file))
                except Exception as e:
                    print(e)
                    magic_number = ''
                    with open(os.path.join(root, file), 'rb') as f:
                        magic_number = f.read(12)
                        print('magic number is:', magic_number)
            # print(type(audio))
            if not 'TALB' in audio:
                audio['TALB'] = TALB(  # 插入专辑名称
                    encoding=3,
                    text=folder
                )
            try:
                audio.save()
            except Exception as e:
                print(e)