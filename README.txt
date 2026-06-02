<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=300&text=🎵+OpusMusicV2&fontAlign=50&fontAlignY=42&fontSize=68&desc=Advanced+Telegram+Voice+Chat+Music+Bot&descAlignY=65&descSize=22&animation=fadeIn&fontColor=ffffff&color=0:0f0c29,50:302b63,100:24243e" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=800&size=22&pause=1000&color=8B5CF6&center=true&vCenter=true&width=900&lines=⚡+Ultra+Fast+Telegram+VC+Music+Bot;🎵+High+Quality+Audio+Streaming;🧠+Smart+Queue+%26+Voice+Controls;🌐+Powered+By+AlfaBots+Network" alt="Typing SVG"/>

<br/><br/>

[![Stars](https://img.shields.io/github/stars/TeamAlfaBots/OpusMusicV2?style=for-the-badge&logo=github&color=8B5CF6&labelColor=111827&label=⭐+Stars)](https://github.com/TeamAlfaBots/OpusMusicV2/stargazers)
[![Forks](https://img.shields.io/github/forks/TeamAlfaBots/OpusMusicV2?style=for-the-badge&logo=github&color=06B6D4&labelColor=111827&label=🍴+Forks)](https://github.com/TeamAlfaBots/OpusMusicV2/network/members)
[![Repo Size](https://img.shields.io/github/repo-size/TeamAlfaBots/OpusMusicV2?style=for-the-badge&color=EC4899&labelColor=111827&label=📦+Size)](https://github.com/TeamAlfaBots/OpusMusicV2)
[![License](https://img.shields.io/github/license/TeamAlfaBots/OpusMusicV2?style=for-the-badge&color=22C55E&labelColor=111827&label=📜+License)](https://github.com/TeamAlfaBots/OpusMusicV2/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=111827)](https://python.org)

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

---

## ✨ Features

<div align="center">

| Feature | Description | Status |
|:-------:|:------------|:------:|
| 🎵 | **Voice Chat Streaming** — Real-time, low-latency audio in Telegram VCs | ✅ |
| 🔎 | **YouTube Search** — Find and play any song instantly | ✅ |
| 📜 | **Smart Queue System** — Add, reorder, and manage tracks effortlessly | ✅ |
| ⏯ | **Playback Controls** — Pause, Resume, Skip with a single command | ✅ |
| 🔁 | **Loop Mode** — Repeat single track or the entire queue | ✅ |
| 🎚 | **Volume Controller** — Fine-tune audio levels in real time | ✅ |
| 🤖 | **Auto Assistant Join** — Hands-free VC joining via Userbot | ✅ |
| ⚡ | **Ultra Fast Streaming** — Optimized pipeline for zero-buffer playback | ✅ |
| 🌍 | **Multi-Language Support** — Localized for global communities | ✅ |
| 📻 | **Radio Streaming** — 24/7 live radio support | ✅ |
| ☁️ | **Easy Deployment** — Heroku, VPS, or any cloud in minutes | ✅ |

</div>

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,linux,mongodb,git,github,docker&theme=dark" alt="Tech Stack"/>

| Technology | Purpose |
|:----------:|:--------|
| **Python 3.10+** | Core bot language |
| **Pyrogram** | Telegram MTProto client |
| **PyTgCalls** | Telegram Voice Chat streaming |
| **yt-dlp** | YouTube audio extraction |
| **MongoDB + Motor** | Async database for settings & queue |
| **Docker** | Containerized deployment |

</div>

---

## ⚙️ Configuration

### Required Environment Variables

Create a `.env` file in the root directory and fill in the following:

```env
# ─── Telegram API ───────────────────────────────────────────
API_ID        =              # From my.telegram.org
API_HASH      =              # From my.telegram.org
BOT_TOKEN     =              # From @BotFather
STRING_SESSION=              # Pyrogram/Telethon string session

# ─── Database ───────────────────────────────────────────────
MONGO_DB_URI  =              # MongoDB connection URI

# ─── Owner Config ───────────────────────────────────────────
OWNER_ID      =              # Your Telegram User ID
LOGGER_ID     =              # Log channel/group ID
```

> **Tip:** Generate your `STRING_SESSION` using [@StringFatherBot](https://t.me/StringFatherBot) or run the session generator locally.

---

## 🚀 Deployment

### ☁️ One-Click Heroku Deploy

<div align="center">

[![Deploy to Heroku](https://img.shields.io/badge/🚀%20Deploy%20to-Heroku-8B5CF6?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/deploy?template=https://github.com/TeamAlfaBots/OpusMusicV2)

</div>

---

### 🖥️ VPS / Local Deployment

**Step 1 — Clone the repository**
```bash
git clone https://github.com/TeamAlfaBots/OpusMusicV2
cd OpusMusicV2
```

**Step 2 — Install dependencies**
```bash
pip install -U pyrogram tgcrypto pytgcalls motor yt-dlp python-dotenv
```

**Step 3 — Configure environment**
```bash
cp .env.example .env
nano .env   # Fill in your values
```

**Step 4 — Run the bot**
```bash
python -m opus
```

---

### 🐳 Docker Deployment

```bash
# Build the image
docker build -t opusmusicv2 .

# Run the container
docker run -d --env-file .env --name opus opusmusicv2
```

---

## 📁 Project Structure

```
OpusMusicV2/
├── opus/
│   ├── __main__.py          # Entry point
│   ├── core/                # Core bot logic
│   ├── plugins/             # Command handlers
│   ├── utils/               # Helper utilities
│   └── config.py            # Configuration loader
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker config
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/your-feature`
3. **Commit** your changes: `git commit -m "feat: add your feature"`
4. **Push** to your branch: `git push origin feat/your-feature`
5. **Open** a Pull Request

Please follow the existing code style and include relevant tests where applicable.

---

## 🐛 Issues & Support

Found a bug or need help? Open an issue on [GitHub Issues](https://github.com/TeamAlfaBots/OpusMusicV2/issues) or reach out via the AlfaBots support group.

---

## 📜 License

```
MIT License — © 2024 Team AlfaBots

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to use, copy, modify, merge, and distribute it freely,
subject to the conditions of the MIT License.
```

See [LICENSE](https://github.com/TeamAlfaBots/OpusMusicV2/blob/main/LICENSE) for full details.

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
