#!/usr/bin/env python3
"""
YouTube Downloader using yt-dlp
Supports video and audio downloads with various quality options
"""

import os
import sys
import yt_dlp
from pathlib import Path

class YouTubeDownloader:
    def __init__(self, download_path="downloads"):
        self.download_path = Path(download_path)
        self.download_path.mkdir(exist_ok=True)
        
    def get_video_info(self, url):
        """Get video information without downloading"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown'),
                    'view_count': info.get('view_count', 0),
                    'upload_date': info.get('upload_date', 'Unknown'),
                    'description': info.get('description', '')[:200] + '...' if info.get('description') else ''
                }
        except Exception as e:
            print(f"Error getting video info: {e}")
            return None
    
    def download_video(self, url, quality='best', format_type='mp4'):
        """Download video with specified quality"""
        
        # Define output template
        output_template = str(self.download_path / '%(title)s.%(ext)s')
        
        # Configure download options
        ydl_opts = {
            'outtmpl': output_template,
            'format': f'best[height<={quality}][ext={format_type}]/best[ext={format_type}]/best',
        }
        
        # If quality is specified as 'best' or 'worst', use it directly
        if quality in ['best', 'worst']:
            ydl_opts['format'] = f'{quality}[ext={format_type}]/{quality}'
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading video: {url}")
                ydl.download([url])
                print("Download completed successfully!")
                return True
        except Exception as e:
            print(f"Error downloading video: {e}")
            return False
    
    def download_audio(self, url, format_type='mp3'):
        """Download audio only"""
        
        output_template = str(self.download_path / '%(title)s.%(ext)s')
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format_type,
                'preferredquality': '192',
            }],
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading audio: {url}")
                ydl.download([url])
                print("Audio download completed successfully!")
                return True
        except Exception as e:
            print(f"Error downloading audio: {e}")
            return False
    
    def download_playlist(self, url, quality='best', format_type='mp4'):
        """Download entire playlist"""
        
        output_template = str(self.download_path / '%(playlist_title)s/%(title)s.%(ext)s')
        
        ydl_opts = {
            'outtmpl': output_template,
            'format': f'best[height<={quality}][ext={format_type}]/best[ext={format_type}]/best',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading playlist: {url}")
                ydl.download([url])
                print("Playlist download completed successfully!")
                return True
        except Exception as e:
            print(f"Error downloading playlist: {e}")
            return False

def main():
    """Main function with interactive menu"""
    downloader = YouTubeDownloader()
    
    print("=== YouTube Downloader ===")
    print("1. Download Video")
    print("2. Download Audio Only")
    print("3. Download Playlist")
    print("4. Get Video Info")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            url = input("Enter YouTube URL: ").strip()
            if not url:
                print("Please enter a valid URL")
                continue
                
            # Get video info first
            info = downloader.get_video_info(url)
            if info:
                print(f"\nTitle: {info['title']}")
                print(f"Duration: {info['duration']} seconds")
                print(f"Uploader: {info['uploader']}")
                
                quality = input("Enter quality (720, 1080, best, worst) [default: best]: ").strip()
                if not quality:
                    quality = 'best'
                
                format_type = input("Enter format (mp4, webm, mkv) [default: mp4]: ").strip()
                if not format_type:
                    format_type = 'mp4'
                
                downloader.download_video(url, quality, format_type)
        
        elif choice == '2':
            url = input("Enter YouTube URL: ").strip()
            if not url:
                print("Please enter a valid URL")
                continue
                
            format_type = input("Enter audio format (mp3, wav, m4a) [default: mp3]: ").strip()
            if not format_type:
                format_type = 'mp3'
                
            downloader.download_audio(url, format_type)
        
        elif choice == '3':
            url = input("Enter YouTube Playlist URL: ").strip()
            if not url:
                print("Please enter a valid URL")
                continue
                
            quality = input("Enter quality (720, 1080, best, worst) [default: best]: ").strip()
            if not quality:
                quality = 'best'
                
            downloader.download_playlist(url, quality)
        
        elif choice == '4':
            url = input("Enter YouTube URL: ").strip()
            if not url:
                print("Please enter a valid URL")
                continue
                
            info = downloader.get_video_info(url)
            if info:
                print(f"\n=== Video Information ===")
                print(f"Title: {info['title']}")
                print(f"Duration: {info['duration']} seconds")
                print(f"Uploader: {info['uploader']}")
                print(f"Views: {info['view_count']:,}")
                print(f"Upload Date: {info['upload_date']}")
                print(f"Description: {info['description']}")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()