from __future__ import unicode_literals
import logging
import yt_dlp as youtube_dl

logger = logging.getLogger(__name__)

class DlLogger(object):
    def debug(self, msg):
        logger.debug(msg)

    def warning(self, msg):
        logger.warning(msg)

    def error(self, msg):
        logger.error(msg)

    
def dl_hook(d):
    if d['status'] == 'finished':
        logger.info('Done downloading, now converting ...')




ydl_opts_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': DlLogger(),
    'progress_hooks': [dl_hook],
    'outtmpl': 'cache/audio/%(id)s.%(ext)s'
}

ydl_opts_mp4 = {
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'logger': DlLogger(),
    'progress_hooks': [dl_hook],
    'outtmpl': 'cache/video/%(id)s.%(ext)s'
}


def download_mp3(url):
    with youtube_dl.YoutubeDL(ydl_opts_mp3) as ydl:
        ydl.download([url])
        return ydl.extract_info(url, download=False)
        


def download_mp4(url):
    with youtube_dl.YoutubeDL(ydl_opts_mp4) as ydl:
        ydl.download([url])
        return ydl.extract_info(url, download=False)