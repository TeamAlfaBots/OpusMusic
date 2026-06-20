import os
import re
import yt_dlp
import random
import asyncio
import aiohttp

from py_yt import Playlist, VideosSearch
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from typing import Union

from opus import logger
from opus.helpers import Track, utils

API_URL = "https://api.shrutibots.site"
API_KEY = "ShrutiBotshMSR3LvyVv3GiNl7Q0bi"

DOWNLOAD_DIR = "downloads"


class YouTube:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="

        self.regex = re.compile(
            r"(https?://)?(www\.|m\.|music\.)?"
            r"(youtube\.com/(watch\?v=|shorts/|playlist\?list=)|youtu\.be/)"
            r"([A-Za-z0-9_-]{11}|PL[A-Za-z0-9_-]+)"
        )

        self.cookies = []
        self.checked = False
        self.cookie_dir = "opus/cookies"
        self.warned = False

    def get_cookies(self):
        if not self.checked:
            if os.path.exists(self.cookie_dir):
                for file in os.listdir(self.cookie_dir):
                    if file.endswith(".txt"):
                        self.cookies.append(f"{self.cookie_dir}/{file}")
            self.checked = True

        if not self.cookies:
            return None

        return random.choice(self.cookies)

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link

        return bool(re.search(self.regex, link))

    async def search(self, query: str, m_id: int, video=False):
        try:
            search = VideosSearch(query, limit=1)
            results = await search.next()
        except Exception as e:
            logger.error(f"Search Error: {e}")
            return None

        if results and results.get("result"):
            data = results["result"][0]

            return Track(
                id=data.get("id"),
                channel_name=data.get("channel", {}).get("name"),
                duration=data.get("duration"),
                duration_sec=utils.to_seconds(data.get("duration")),
                message_id=m_id,
                title=data.get("title")[:25],
                thumbnail=data.get("thumbnails", [{}])[-1]["url"].split("?")[0],
                url=data.get("link"),
                view_count=data.get("viewCount", {}).get("short"),
                video=video,
            )

    async def playlist(self, limit, user, url, video):
        tracks = []

        try:
            plist = await Playlist.get(url)

            for data in plist["videos"][:limit]:
                tracks.append(
                    Track(
                        id=data.get("id"),
                        channel_name=data.get("channel", {}).get("name"),
                        duration=data.get("duration"),
                        duration_sec=utils.to_seconds(data.get("duration")),
                        title=data.get("title")[:25],
                        thumbnail=data.get("thumbnails")[-1]["url"].split("?")[0],
                        url=data.get("link").split("&list=")[0],
                        user=user,
                        view_count="",
                        video=video,
                    )
                )

        except Exception as e:
            logger.error(f"Playlist Error: {e}")

        return tracks

    async def url(self, message_1: Message):
        messages = [message_1]

        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)

        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[
                            entity.offset : entity.offset + entity.length
                        ]

        return None

    async def api_download(self, video_id, video=False):
        try:
            youtube_url = self.base + video_id

            async with aiohttp.ClientSession() as session:

                params = {
                    "url": youtube_url,
                    "type": "video" if video else "audio",
                    "api_key": API_KEY,
                }

                async with session.get(
                    f"{API_URL}/download",
                    params=params,
                    timeout=aiohttp.ClientTimeout(total=600),
                ) as resp:

                    if resp.status != 200:
                        logger.error(f"API Status: {resp.status}")
                        return None

                    filename = f"downloads/{video_id}.{'mp4' if video else 'mp3'}"

                    os.makedirs("downloads", exist_ok=True)

                    with open(filename, "wb") as f:
                        async for chunk in resp.content.iter_chunked(131072):
                            f.write(chunk)

                    if os.path.exists(filename):
                        return filename

        except Exception as e:
            logger.error(f"API Download Error: {e}")

        return None

    async def ytdlp_download(self, video_id, video=False):
        url = self.base + video_id

        filename = f"downloads/{video_id}.{'mp4' if video else 'webm'}"

        cookie = self.get_cookies()

        opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "quiet": True,
            "nocheckcertificate": True,
        }

        if cookie:
            opts["cookiefile"] = cookie

        if video:
            opts["format"] = "bestvideo+bestaudio"
        else:
            opts["format"] = "bestaudio"

        def run():
            with yt_dlp.YoutubeDL(opts) as ydl:
                try:
                    ydl.download([url])
                except Exception as e:
                    logger.error(f"yt-dlp Error: {e}")
                    return None

            return filename

        return await asyncio.to_thread(run)

    async def download(self, video_id, video=False):
        file = await self.api_download(video_id, video)

        if file:
            return file

        logger.warning("API failed, switching to yt-dlp")

        return await self.ytdlp_download(video_id, video)