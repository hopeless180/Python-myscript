import requests
from bs4 import BeautifulSoup
import os
from lxml import etree
import re

bv = input("请输入bv号：")
url = f"https://www.bilibili.com/video/{bv}/"

header_ = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com",
    "cookie": "buvid3=4B1706D6-52BE-961A-E1BF-A872271FC3E533037infoc; b_nut=1674141633; _uuid=10316B66B-3486-8FAD-D83B-3C393399BA3148396infoc; i-wanna-go-back=-1; LIVE_BUVID=AUTO8716741416422883; buvid_fp_plain=undefined; DedeUserID=34124962; DedeUserID__ckMd5=18abf3e7112ae462; rpdid=|(u|u)u)mRuR0J'uY~RuRk)Y|; nostalgia_conf=-1; hit-dyn-v2=1; b_ut=5; buvid4=CAB16B10-778A-D564-F86A-C62A15DB52BF78017-022012016-WT67as8gZw9GqIP0f7DFVA%3D%3D; CURRENT_BLACKGAP=0; CURRENT_PID=6cf8fa10-bca7-11ed-8b1a-4522c38af9b3; hit-new-style-dyn=1; CURRENT_FNVAL=4048; theme_style=light; kfcSource=zzpl_ugc_blhx; msource=zzpl_ugc_blhx; deviceFingerprint=656b9550935adf2b16046d4af54073a2; fingerprint=486b1d84c7a7426db12ceb62afdf9942; home_feed_column=5; share_source_origin=QQ; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; SESSDATA=d9b2a8fc%2C1703680649%2C56823%2A62XAMAhGQwRgZmdgwMIZrRJ4jpey_lV8-B-qBqyZ6vNEl_7CHcoiFYV-j454RjicfSwuAdoQAAPgA; bili_jct=063d3b9111f121d633fe7630b970390a; sid=6cmii1a3; bsource=search_google; CURRENT_QUALITY=120; browser_resolution=1920-881; PVID=4; b_lsid=10D3FB2B5_189122EEB23; buvid_fp=486b1d84c7a7426db12ceb62afdf9942; bp_t_offset_34124962=813423143489110025",
}

response_ = requests.get(url, headers=header_)
data_ = response_.content

html_obj = etree.HTML(data_)
videoTitle = html_obj.xpath("//title/text()")[0]
videoTitle = re.findall(r"(.*?)_哔哩哔哩", videoTitle)[0]
print(videoTitle)

info_ = html_obj.xpath('//script[contains(text(), "window.__playinfo__")]/text()')[0]
videoUrl = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', info_)[0]
print(videoUrl)
audioUrl = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', info_)[0]
print(audioUrl)

header_getvideo = dict(header_)
header_getvideo["Referer"] = url
response_video = requests.get(videoUrl, headers=header_getvideo)
response_audio = requests.get(audioUrl, headers=header_getvideo)
data_video = response_video.content
data_audio = response_audio.content

with open(f"temp_v_{videoTitle}.mp4", "wb") as f:
    f.write(data_video)
with open(f"temp_a_{videoTitle}.mp4", "wb") as f:
    f.write(data_audio)

try:
    os.system(
        f'ffmpeg -i "temp_v_{videoTitle}.mp4" -i "temp_a_{videoTitle}.mp4" -c copy "{videoTitle}.mp4"'
    )
except Exception as e:
    print(e)
else:
    os.remove(f"temp_v_{videoTitle}.mp4")
    os.remove(f"temp_a_{videoTitle}.mp4")
