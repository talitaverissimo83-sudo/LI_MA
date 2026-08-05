# pip install yt-dlp
import yt_dlp

url = input("Cole a URL do video: ")

opcoes = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4"
    "outtmpl": "%(tittle)s.%(ext)s",
    }

with yt_dlp.YoutubeDL(opcoes) as ydl