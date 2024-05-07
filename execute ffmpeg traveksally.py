import os, ffmpeg, re, shutil
from tqdm import tqdm

MEGABYTE = 1 << 20
KILOBYTE = 1 << 10
VIDEO = 'video'
AUDIO = 'audio'

def dovideoffmpeg(input_path:str, output_path:str, file:str, generateNewFolder: bool = False, folderName: str = "temp") -> None:
    src = os.path.join(input_path, file)
    dst = os.path.splitext(os.path.join(output_path, file))
    dst = dst[0] + "_lowBitrate"+dst[1]
    ext = os.path.splitext(src)[1]
    basename = os.path.splitext(src)[0]
    if ext in ['.mp4', '.m4v', '.avi'] and "_lowBitrate" not in src:
        try:
            probe = ffmpeg.probe(src)
        except Exception as e:
            print(src, e)
            return
        video_info = next(s for s in probe['streams'] if s['codec_type'] == "video")
        # audio_info = next(s for s in probe['streams'] if s['codec_type'] == "audio")
        fps = int(video_info['r_frame_rate'].split('/')[0])
        bitrate = int(video_info['bit_rate'])
        output_bitrate = calcBitrateByFPS(fps, bitrate)
        if output_bitrate != bitrate and bitrate > 11*MEGABYTE:
            stream = ffmpeg.input(src)
            stream = ffmpeg.output(stream, dupFile(dst), video_bitrate=output_bitrate)
            try:
                ffmpeg.run(stream, quiet=True)
            except Exception as e:
                print(e)
            else:
                os.remove(src)
        elif input_path != output_path:
            shutil.move(src, dupFile(dst))

def calcBitrateByFPS(fps: int, bitrate: int)->any:
    if fps <= 30:
        output_bitrate = 4*MEGABYTE
    elif fps <= 60:
        output_bitrate = bitrate if bitrate < 4*MEGABYTE else '4M' if bitrate < 6*MEGABYTE else '6M' if bitrate < 8*MEGABYTE else '8M'
    elif fps >= 120:
        output_bitrate = bitrate if bitrate < 4*MEGABYTE else '8M' if bitrate < 6*MEGABYTE else '12M' if bitrate < 8*MEGABYTE else '16M'
    else:
        output_bitrate = bitrate
    return output_bitrate

def calc_bitrate_byFps(fps: int, bitrate: int, border: list)->any:
    l = [x for x in border]
    if bitrate <= l[0] * MEGABYTE:
        return bitrate
    if fps <= 30:
        output_bitrate = f"{l[0]}M"
    else:
        if fps >= 120:
            l = [x*2 for x in l]
        output_bitrate = bitrate if bitrate < l[0] * MEGABYTE else f"{l[0]}M" if bitrate < l[1] * MEGABYTE else f"{l[1]}M" if bitrate < l[2] * MEGABYTE else f"{l[2]}M"
    return output_bitrate

def dupFile(path: str) -> str:
    ## 是否重复，不重复就退出
    if not os.path.exists(path):
        return path
    ## 是否符合我的命名规范，即字符串+（数字）的格式
    old_name = os.path.basename(path)
    match = re.match(r"^(.+?) \((\d+)\)\.(.+)$", old_name)
    if match:
        tmp_num = int(match.group(2))
        tmp_ext = match.group(3)
        new_name = re.sub(r"\(\d+\)", f"({tmp_num+1})", old_name)
        new_path = path.replace(old_name, new_name)
    else:
        new_path = "{0[0]} (2){0[1]}".format(os.path.splitext(path))
    try:
        match = re.match(r"^[a-zA-Z]:[\\\/]{1,2}(.+[\\\/]{1,2})*.+? \(\d+\)\.[\w]+$", new_path)
        if not match:
            raise ValueError("字符串不符合格式要求")
    except ValueError as e:
        print(e)
        raise
    return dupFile(new_path)

def check_filePath_format(str: str) -> bool:
    match = re.match(r"^[a-zA-Z]:[\\\/]{1,2}(.+[\\\/]{1,2})*.+? \(\d+\)\.[\w]+$", str)
    if match:
        return True
    else:
        return False
        # raise ValueError("字符串不符合文件系统格式要求")


def doaudioffmpeg(input_path:str, output_path:str, file:str, generateNewFolder: bool = False, folderName: str = "temp") -> None:
    name, ext = os.path.splitext(file)
    src = os.path.join(input_path, file)
    dst = os.path.join(output_path, f"{name}_Idid.mp3")
    if ext in ['.wav'] and "_Idid" not in src:
        dst = dupFile(dst)
        stream = ffmpeg.input(src)
        stream = ffmpeg.output(stream, dst)
        try:
            ffmpeg.run(stream, quiet=True)
        except Exception as e:
            print(e)
        else:
            os.remove(src) if os.path.exists(dst) else 0

def doffmpeg(state, **kwargs) -> None:
    state_funciton = {
        VIDEO: dovideoffmpeg,
        AUDIO: doaudioffmpeg
        # 状态 = 函数
    }
    selected_function = state_funciton.get(state)
    if selected_function:
        return selected_function(**kwargs)
    else:
        raise ValueError("Invalid state")

if __name__ == "__main__":
    # srcfolder = r"g://MapleHutCat"
    # dstfolder = r"g://MapleHutCat"
    src = "E:\\YeYeBirdie(イェイェバルディ)"
    for folder in tqdm(os.listdir(src), desc='根目录'):
        srcfolder = os.path.join(src, folder)
        dstfolder = os.path.join(src, folder)
        if os.path.isfile(srcfolder):
            doffmpeg(VIDEO, input_path=src, output_path=src, file = folder)
            continue
        os.mkdir(dstfolder) if not os.path.exists(dstfolder) else None
        for root, dirs, files in os.walk(srcfolder):
            for file in tqdm(files, desc="子目录"):
                doffmpeg(VIDEO, input_path=root, output_path=dstfolder, file = file)
