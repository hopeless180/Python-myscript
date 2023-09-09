import os, ffmpeg, re, shutil

MEGABYTE = 1 << 20
KILOBYTE = 1 << 10

def doffmpeg(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        if root == output_path:
            continue
        for file in files:
            ext = os.path.splitext(file)[1]
            basename = os.path.splitext(file)[0]
            if os.path.splitext(file)[1] in ['.mp4', '.m4v']:
                probe = ffmpeg.probe(os.path.join(root, file))
                video_info = next(s for s in probe['streams'] if s['codec_type'] == "video")
                # audio_info = next(s for s in probe['streams'] if s['codec_type'] == "audio")
                fps = int(video_info['r_frame_rate'].split('/')[0])
                bitrate = int(video_info['bit_rate'])
                if fps <= 30:
                    output_bitrate = 4*MEGABYTE
                elif fps <= 60:
                    output_bitrate = bitrate if bitrate < 4*MEGABYTE else '4M' if bitrate < 6*MEGABYTE else '6M' if bitrate < 8*MEGABYTE else '8M'
                elif fps == 120:
                    output_bitrate = bitrate if bitrate < 4*MEGABYTE else '8M' if bitrate < 6*MEGABYTE else '12M' if bitrate < 8*MEGABYTE else '16M'
                else:
                    output_bitrate = bitrate
                in_file = os.path.join(root, file)
                out_file = os.path.join(output_path,os.path.basename(file))
                if output_bitrate != bitrate and bitrate > 9*1024*1024:
                    stream = ffmpeg.input(in_file)
                    stream = ffmpeg.output(stream, dupFile(out_file), video_bitrate=output_bitrate)
                    try:
                        ffmpeg.run(stream)
                    except Exception as e:
                        print(e)
                    else:
                        os.remove(in_file)
                else:
                    shutil.move(in_file, dupFile(out_file))

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

if __name__ == "__main__":
    videofolder = r"G:\video"
    dstfolder = r'e:\车\同人3D'
    for x in os.listdir(videofolder):
        src = os.path.join(videofolder, x)
        dst = os.path.join(dstfolder, x)
        os.mkdir(dst) if not os.path.exists(dst) else None
        doffmpeg(input_path=src, output_path=dst)