import os, ffmpeg, json

MEGABYTE = 1 << 20
KILOBYTE = 1 << 10
DESKTOP = "c://Users//neun//Desktop"

def main():
    dir = "e:\\车"
    videoList = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            filename = os.path.join(root, file)
            _, ext = os.path.splitext(filename)
            if 'mp4' not in ext:
                continue
            probe = ffmpeg.probe(filename)
            videoInfo = next(s for s in probe['streams'] if s['codec_type'] == "video")
            bitrate = int(videoInfo['bit_rate'])
            if bitrate <= 10*MEGABYTE:
                continue
            print(os.path.basename(filename))
            videoObj = {
                'name': os.path.basename(filename),
                'path': filename,
                'information': videoInfo,
                'bitrate': int(bitrate / MEGABYTE)
            }
            videoList.append(videoObj)
            with open(os.path.join(DESKTOP, 'videolist.json'), 'w+') as f:
                json.dump(videoList, f)

if __name__ == '__main__':
    main()