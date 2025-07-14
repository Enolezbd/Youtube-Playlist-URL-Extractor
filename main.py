import yt_dlp

# Replace with your playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID'

ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'dump_single_json': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)

    with open('playlist_urls.txt', 'w') as f:
        for entry in info['entries']:
            url = f"https://www.youtube.com/watch?v={entry['id']}"
            print(url)
            f.write(url + '\n')

print("\nAll URLs saved to 'playlist_urls.txt'")
