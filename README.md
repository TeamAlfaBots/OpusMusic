<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=300&text=🎵+OpusMusic&fontAlign=50&fontAlignY=42&fontSize=68&desc=Advanced+Telegram+Voice+Chat+Music+Bot&descAlignY=65&descSize=22&animation=fadeIn&fontColor=ffffff&color=0:0f0c29,50:302b63,100:24243e" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=800&size=22&pause=1000&color=8B5CF6&center=true&vCenter=true&width=900&lines=⚡+Ultra+Fast+Telegram+VC+Music+Bot;🎵+High+Quality+Audio+Streaming;🧠+Smart+Queue+%26+Voice+Controls;🌐+Powered+By+AlfaBots+Network" alt="Typing SVG"/>

<br/><br/>

[![Stars](https://img.shields.io/github/stars/TeamAlfaBots/OpusMusicV2?style=for-the-badge&logo=github&color=8B5CF6&labelColor=111827&label=⭐+Stars)](https://github.com/TeamAlfaBots/OpusMusicV2/stargazers)
[![Forks](https://img.shields.io/github/forks/TeamAlfaBots/OpusMusicV2?style=for-the-badge&logo=github&color=06B6D4&labelColor=111827&label=🍴+Forks)](https://github.com/TeamAlfaBots/OpusMusicV2/network/members)
[![Issues](https://img.shields.io/github/issues/TeamAlfaBots/OpusMusicV2?style=for-the-badge&logo=github&color=F59E0B&labelColor=111827&label=🐛+Issues)](https://github.com/TeamAlfaBots/OpusMusicV2/issues)
[![License](https://img.shields.io/github/license/TeamAlfaBots/OpusMusicV2?style=for-the-badge&color=22C55E&labelColor=111827&label=📜+License)](https://github.com/TeamAlfaBots/OpusMusicV2/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=111827)](https://python.org)
[![Repo Size](https://img.shields.io/github/repo-size/TeamAlfaBots/OpusMusicV2?style=for-the-badge&color=EC4899&labelColor=111827&label=📦+Size)](https://github.com/TeamAlfaBots/OpusMusicV2)

<br/>

[**🎯 Features**](#-features) &nbsp;•&nbsp; [**🚀 Quick Start**](#-quick-start) &nbsp;•&nbsp; [**⚙️ Configuration**](#%EF%B8%8F-configuration) &nbsp;•&nbsp; [**☁️ Deploy**](#-deployment) &nbsp;•&nbsp; [**🤝 Contributing**](#-contributing)

</div>

---

## 🌌 Overview

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🎵  OpusMusicV2  —  The Ultimate Telegram Music Bot 🎵    ║
║                                                              ║
║   Stream music in Telegram Voice Chats with zero lag,       ║
║   crystal-clear audio, and a smart assistant that just      ║
║   works — every single time.                                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

</div>

**OpusMusicV2** is a production-grade, feature-rich Telegram Voice Chat music bot built for serious group streaming. Engineered for speed, stability, and an exceptional user experience — from ultra-fast YouTube playback to seamless queue management and multi-language support.

### Why OpusMusicV2?

- 🚀 **Zero-buffer streaming** — Optimized audio pipeline delivers music without interruption
- 🔒 **Battle-tested** — Built on Pyrogram + PyTgCalls, the most stable MTProto stack
- 🧩 **Modular architecture** — Easy to extend with new plugins and custom commands
- 🌍 **Global ready** — Multi-language support out of the box

---

## ✨ Features

<div align="center">

| &nbsp; | Feature | Description | Status |
|:------:|:--------|:------------|:------:|
| 🎵 | **Voice Chat Streaming** | Real-time, low-latency audio in Telegram VCs | ✅ |
| 🔎 | **YouTube Search & Play** | Find and play any song instantly via inline search | ✅ |
| 📜 | **Smart Queue System** | Add, reorder, remove, and shuffle tracks effortlessly | ✅ |
| ⏯ | **Playback Controls** | Pause, Resume, Skip, Seek with a single command | ✅ |
| 🔁 | **Loop Mode** | Repeat a single track or the entire queue | ✅ |
| 🎚 | **Volume Controller** | Fine-tune audio levels (0–200%) in real time | ✅ |
| 🤖 | **Auto Assistant Join** | Hands-free VC joining via Userbot assistant | ✅ |
| ⚡ | **Ultra Fast Streaming** | Optimized pipeline for zero-buffer playback | ✅ |
| 🌍 | **Multi-Language Support** | Localized for global communities | ✅ |
| 📻 | **Radio Streaming** | 24/7 live radio station support | ✅ |
| 🛡️ | **Admin Controls** | Auth users, ban/unban, and manage permissions | ✅ |
| ☁️ | **Easy Deployment** | Heroku, VPS, Docker — deploy in minutes | ✅ |

</div>

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,linux,mongodb,git,github,docker&theme=dark" alt="Tech Stack"/>

| Technology | Purpose | Version |
|:----------:|:--------|:-------:|
| **Python** | Core bot language | `3.10+` |
| **Pyrogram** | Telegram MTProto client | `2.x` |
| **PyTgCalls** | Voice Chat streaming engine | `Latest` |
| **yt-dlp** | YouTube audio extraction | `Latest` |
| **MongoDB + Motor** | Async database for settings & queue | `6.x+` |
| **Docker** | Containerized deployment | `20.x+` |

</div>

---

## 🚀 Quick Start

> **Prerequisites:** Python 3.10+, a Telegram API ID/Hash, a Bot Token, and a MongoDB instance.

```bash
# 1. Clone the repo
git clone https://github.com/TeamAlfaBots/OpusMusicV2.git
cd OpusMusicV2

# 2. Install dependencies
pip install -U -r requirements.txt

# 3. Configure environment
cp .env.example .env
nano .env   # Fill in your values (see Configuration below)

# 4. Launch the bot
python -m opus
```

🎉 **That's it!** Your bot should now be online. Add it to a group, start a voice chat, and play your first song.

---

## ⚙️ Configuration

### Required Environment Variables

Create a `.env` file in the root directory:

```env
# ─── Telegram API ───────────────────────────────────────────
API_ID         =              # From https://my.telegram.org
API_HASH       =              # From https://my.telegram.org
BOT_TOKEN      =              # From @BotFather
STRING_SESSION =              # Pyrogram string session (see below)

# ─── Database ───────────────────────────────────────────────
MONGO_DB_URI   =              # MongoDB connection URI (e.g., mongodb+srv://...)

# ─── Owner Config ───────────────────────────────────────────
OWNER_ID       =              # Your Telegram User ID (numeric)
LOGGER_ID      =              # Log channel/group ID (numeric, with -100 prefix)
```

<details>
<summary><strong>🔑 How to generate STRING_SESSION</strong></summary>

<br/>

**Option A — Use a Telegram Bot:**

> Generate your session string via [@StringFatherBot](https://t.me/StringFatherBot) on Telegram.

**Option B — Generate locally:**

```bash
pip install pyrogram tgcrypto
python -c "from pyrogram import Client; Client(':memory:', api_id=YOUR_API_ID, api_hash='YOUR_API_HASH').run(Client.export_session_string)"
```

> ⚠️ **Security:** Never share your session string with anyone. Treat it like a password.

</details>

<details>
<summary><strong>🆔 How to find your OWNER_ID</strong></summary>

<br/>

Send `/start` to [@userinfobot](https://t.me/userinfobot) on Telegram — it will reply with your numeric user ID.

</details>

<details>
<summary><strong>🗄️ How to get MONGO_DB_URI</strong></summary>

<br/>

1. Create a free cluster at [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a database user with a password
3. Whitelist `0.0.0.0/0` in Network Access
4. Copy the connection string — it looks like:
   ```
   mongodb+srv://username:password@cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```

</details>

---

## ☁️ Deployment

### 🟣 One-Click Heroku Deploy

<div align="center">

[![Deploy to Heroku](https://img.shields.io/badge/🚀%20Deploy%20to-Heroku-8B5CF6?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/deploy?template=https://github.com/TeamAlfaBots/OpusMusicV2)

</div>

> Click the button above, fill in the environment variables, and your bot will be live in ~2 minutes.

---

### 🖥️ VPS Deployment (Ubuntu/Debian)

```bash
# Update system & install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip ffmpeg git

# Clone and setup
git clone https://github.com/TeamAlfaBots/OpusMusicV2.git
cd OpusMusicV2
pip3 install -U -r requirements.txt

# Configure
cp .env.example .env
nano .env

# Run with screen (persists after SSH disconnect)
screen -S opus
python3 -m opus
# Press Ctrl+A then D to detach
```

> **💡 Pro Tip:** Use `systemd` for production deployments to ensure the bot auto-restarts on crashes and system reboots.

<details>
<summary><strong>📋 systemd Service File</strong></summary>

```ini
# /etc/systemd/system/opusmusic.service
[Unit]
Description=OpusMusicV2 Telegram Bot
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/home/your-username/OpusMusicV2
ExecStart=/usr/bin/python3 -m opus
Restart=on-failure
RestartSec=10
EnvironmentFile=/home/your-username/OpusMusicV2/.env

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable opusmusic
sudo systemctl start opusmusic
sudo systemctl status opusmusic  # Check status
```

</details>

---

### 🐳 Docker Deployment

```bash
# Build the image
docker build -t opusmusicv2 .

# Run the container
docker run -d \
  --name opus \
  --env-file .env \
  --restart unless-stopped \
  opusmusicv2
```

**Docker Compose** (recommended for production):

```yaml
# docker-compose.yml
version: "3.9"
services:
  opus:
    build: .
    container_name: opusmusicv2
    env_file: .env
    restart: unless-stopped
    volumes:
      - ./downloads:/app/downloads
```

```bash
docker compose up -d
```

---

## 🎮 Commands

| Command | Description | Access |
|:--------|:------------|:------:|
| `/play <song>` | Play a song by name or YouTube URL | All |
| `/pause` | Pause current playback | Admin |
| `/resume` | Resume paused playback | Admin |
| `/skip` | Skip to the next song in queue | Admin |
| `/stop` | Stop playback and clear queue | Admin |
| `/queue` | View the current song queue | All |
| `/loop` | Toggle loop mode (track / queue / off) | Admin |
| `/volume <0-200>` | Adjust playback volume | Admin |
| `/shuffle` | Shuffle the current queue | Admin |
| `/song <name>` | Download a song as audio file | All |
| `/radio <url>` | Stream a live radio station | Admin |
| `/ping` | Check bot latency | All |

> **Note:** Admin = Group admin or authorized user. Use `/auth @username` to grant access.

---

## 📁 Project Structure

```
OpusMusicV2/
├── opus/
│   ├── __main__.py          # Entry point — initializes bot & userbot
│   ├── __init__.py          # Package initialization
│   ├── config.py            # Configuration loader (reads .env)
│   ├── core/                # Core bot logic
│   │   ├── bot.py           # Pyrogram bot client
│   │   ├── userbot.py       # Assistant/userbot client
│   │   └── calls.py         # PyTgCalls streaming handler
│   ├── plugins/             # Command handlers (modular)
│   │   ├── play.py          # /play command
│   │   ├── controls.py      # /pause, /resume, /skip, /stop
│   │   ├── queue.py         # /queue, /shuffle
│   │   ├── admin.py         # /auth, /ban, /unban
│   │   └── misc.py          # /ping, /help, /start
│   ├── utils/               # Helper utilities
│   │   ├── database.py      # MongoDB async operations
│   │   ├── youtube.py       # yt-dlp wrapper
│   │   ├── stream.py        # Audio stream utilities
│   │   └── decorators.py    # Permission decorators
│   └── assets/              # Static assets (thumbnails, etc.)
├── .env.example             # Environment variable template
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose setup
├── Procfile                 # Heroku process config
├── app.json                 # Heroku app manifest
├── LICENSE                  # MIT License
└── README.md                # You are here!
```

---

## 🔧 Troubleshooting

<details>
<summary><strong>❌ Bot doesn't join voice chat</strong></summary>

- Ensure `STRING_SESSION` is valid and the userbot account is in the group
- Make the userbot an admin with "Manage Voice Chats" permission
- Check that a voice chat is actively running in the group

</details>

<details>
<summary><strong>❌ "No results found" when playing a song</strong></summary>

- Ensure `yt-dlp` is up to date: `pip install -U yt-dlp`
- Check your internet connection on the server
- Some videos may be region-restricted — try a VPN or different query

</details>

<details>
<summary><strong>❌ MongoDB connection error</strong></summary>

- Verify your `MONGO_DB_URI` is correct (no extra spaces)
- Ensure `0.0.0.0/0` is whitelisted in MongoDB Atlas Network Access
- Check that the database user password doesn't contain special characters that need URL encoding

</details>

<details>
<summary><strong>❌ Audio stuttering or lag</strong></summary>

- Ensure your server has at least 1 vCPU and 512 MB RAM
- Install `ffmpeg` — it's required for audio processing
- Check server bandwidth (streaming requires ~128 kbps per active chat)

</details>

---

## 🤝 Contributing

We welcome contributions from the community! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feat/your-awesome-feature
   ```
3. **Make** your changes and test thoroughly
4. **Commit** with a descriptive message:
   ```bash
   git commit -m "feat: add your awesome feature"
   ```
5. **Push** to your fork:
   ```bash
   git push origin feat/your-awesome-feature
   ```
6. **Open** a Pull Request with a clear description of your changes

### Guidelines

- Follow the existing code style (PEP 8)
- Keep commits atomic and well-described
- Add comments for complex logic
- Test your changes in a real Telegram group before submitting

---

## 🐛 Issues & Support

| Channel | Link |
|:--------|:-----|
| 🐛 Bug Reports | [GitHub Issues](https://github.com/TeamAlfaBots/OpusMusicV2/issues/new?template=bug_report.md) |
| 💡 Feature Requests | [GitHub Issues](https://github.com/TeamAlfaBots/OpusMusicV2/issues/new?template=feature_request.md) |
| 💬 Community Support | [AlfaBots Support Group](https://t.me/AlfaBotsSupport) |

---

## 📜 License

```
MIT License — © 2024–2026 Team AlfaBots

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to use, copy, modify, merge, and distribute it freely,
subject to the conditions of the MIT License.
```

See [`LICENSE`](https://github.com/TeamAlfaBots/OpusMusicV2/blob/main/LICENSE) for full details.

---

## ⭐ Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=TeamAlfaBots/OpusMusicV2&type=Date)](https://star-history.com/#TeamAlfaBots/OpusMusicV2&Date)

</div>

> **If OpusMusicV2 helps your community, give it a ⭐ — it means a lot!**

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=20&pause=1000&color=EC4899&center=true&vCenter=true&width=800&lines=🚀+AlfaBots+Network;AI+•+Music+•+Automation;Building+Powerful+Telegram+Projects" alt="AlfaBots"/>

<br/>

**⚡ Fast &nbsp;•&nbsp; Stable &nbsp;•&nbsp; Modern ⚡**

<br/>

Made with ❤️ by **[Team AlfaBots](https://github.com/TeamAlfaBots)**

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:24243e,50:302b63,100:0f0c29" width="100%"/>

</div>
