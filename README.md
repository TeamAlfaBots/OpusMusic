<div align="center">

<img src="https://files.catbox.moe/oc0vh3.svg" width="720" height="auto" alt="OpusMusic Banner"/>

<h2>OpusMusic</h2>

<b>Telegram Group Calls Streaming Bot</b><br>
Supports YouTube, Spotify, Resso, Apple Music, SoundCloud and M3U8 links.

<br>

<a href="https://github.com/TeamAlfaBots/OpusMusic/stargazers">
    <img src="https://img.shields.io/github/stars/TeamAlfaBots/OpusMusic?color=blueviolet&logo=github&logoColor=black&style=for-the-badge" alt="Stars"/>
</a>
<a href="https://github.com/TeamAlfaBots/OpusMusic/network/members">
    <img src="https://img.shields.io/github/forks/TeamAlfaBots/OpusMusic?color=blueviolet&logo=github&logoColor=black&style=for-the-badge" alt="Forks"/>
</a>
<a href="https://github.com/TeamAlfaBots/OpusMusic/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License"/>
</a>
<a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Written%20in-Python-blueviolet?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</a>

<br><br>

OpusMusic lets you stream high-quality and low-latency audio and video playback into Telegram group video chats.<br>
Built with <b>Python</b>, <b>Pyrogram</b>, and <b>Py-TgCalls</b> — optimized for reliability and easy deployment.

</div>

<hr>

## 🔥 Features

- 🎧 Stream low-latency **audio & video** in real time to Telegram group video chats
- 🌐 Supports **YouTube, Spotify, Apple Music, SoundCloud, Resso & M3U8**
- ⚡ Advanced queue management with auto-play
- 🎛️ Powerful admin controls for group management
- ⚙️ Easy deployment — works on **Local, VPS, or Heroku**
- ❤️ Built with Python + Pyrogram + Py-TgCalls

<hr>

## ☁️ Deployment

### ✔️ Prerequisites

- [Python 3.10+](https://www.python.org) installed
- [ffmpeg](https://ffmpeg.org/) installed on your system
- Required variables from [`sample.env`](https://github.com/TeamAlfaBots/OpusMusic/blob/master/sample.env)

| Variable | Required | Description |
|----------|----------|-------------|
| `API_ID` | ✅ | Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | ✅ | Telegram API Hash |
| `BOT_TOKEN` | ✅ | Bot token from [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | ✅ | Your Telegram user ID |
| `LOGGER_ID` | ✅ | Log channel/group ID |
| `MONGO_URL` | ✅ | MongoDB connection string |
| `SESSION` | ✅ | Pyrogram session string |

> 💡 Generate your session string using [@StringFatherBot](https://t.me/StringFatherBot)

<hr>

<details>
<summary><h3>🐧 Local / VPS Setup (Linux & macOS)</h3></summary>

```bash
git clone https://github.com/TeamAlfaBots/OpusMusic
cd OpusMusic

# Install uv
curl -Ls https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Install dependencies
uv sync --frozen

# Rename and configure environment variables
mv sample.env .env
# Edit .env with your credentials

# Start the bot
bash start
