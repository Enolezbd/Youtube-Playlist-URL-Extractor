# YouTube Playlist URL Extractor

This project extracts all video URLs from a YouTube playlist and saves them in a plain text file (`playlist_urls.txt`).

It uses **Python** and **yt-dlp**, a powerful YouTube downloader library that works reliably for playlists.

---

## 🚀 How to use

### 1️⃣ Clone or open this Codespace

Open the project in **GitHub Codespaces** or clone it locally.

---

### 2️⃣ Install dependencies

In the **Codespaces terminal**, run:
```bash
pip install yt-dlp

3️⃣ Update main.py
Open main.py and replace:

playlist_url = 'https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID'
with your actual playlist URL.

4️⃣ Run the script
In the terminal, run:

```bash
python main.py

5️⃣ Get your URLs
The script will print each video URL in the terminal.

All video URLs will be saved to a file called playlist_urls.txt in the project folder.

✅ Requirements
Python 3.7+

yt-dlp Python package

⚡ Why yt-dlp?
yt-dlp is an improved fork of youtube-dl — it’s more reliable than pytube for playlists.

Done!
Use this to easily copy all video links from any YouTube playlist.
