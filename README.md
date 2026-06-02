<p align="center">
  <img src="https://files.catbox.moe/oc0vh3.svg" alt="OpusMusic Banner" width="100%">
</p>

<h1 align="center">🎵 OpusMusic</h1>

<p align="center">
 Powerful Telegram Music Bot Built Using Pyrogram & PyTgCalls
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Telegram-MusicBot-2ea44f?style=for-the-badge&logo=telegram">
  <img src="https://img.shields.io/badge/Platform-VPS%20|%20Docker%20|%20Railway-purple?style=for-the-badge">
  <img src="https://img.shields.io/github/license/TeamAlfaBots/OpusMusic?style=for-the-badge">
</p>

---

# ✨ Features

```diff
+ Voice Chat Music Streaming
+ High Quality Audio Playback
+ YouTube Search & Play
+ Queue System
+ Pause / Resume / Skip / Stop
+ Loop & Seek Support
+ Multi Language Support
+ Broadcast System
+ Fast & Optimized
+ Modular Plugin Structure
+ Docker Ready
+ Railway / VPS / Heroku Support

---

📂 Project Structure

OpusMusic-main/
│
├── opus/
│   ├── core/
│   ├── plugins/
│   ├── helpers/
│   ├── locales/
│   └── database/
│
├── Dockerfile
├── Procfile
├── pyproject.toml
├── sample.env
├── start
└── README.md

---

🚀 VPS Deployment

1️⃣ Install Dependencies

sudo apt update && sudo apt install ffmpeg git python3 python3-pip -y

---

2️⃣ Upload Project

unzip OpusMusic-main.zip
cd OpusMusic-main

---

3️⃣ Install Python Packages

Since this project uses "pyproject.toml":

pip3 install -U pip setuptools wheel
pip install .

---

4️⃣ Setup Environment Variables

cp sample.env .env
nano .env

Fill This:

API_ID=
API_HASH=
BOT_TOKEN=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=

---

🔑 Required Variables

Variable| Description
API_ID| Telegram API ID
API_HASH| Telegram API HASH
BOT_TOKEN| Telegram Bot Token
MONGO_DB_URI| MongoDB Database URL
OWNER_ID| Your Telegram User ID
STRING_SESSION| Assistant Account String Session

---

5️⃣ Start The Bot

bash start

OR

python -m opus

---

🐳 Docker Deployment

Build Docker Image

docker build -t opusmusic .

---

Run Container

docker run -d --name opusmusic --env-file .env opusmusic

---

☁️ Railway Deployment

Steps

1. Upload Project To GitHub
2. Open Railway
3. Create New Project
4. Connect GitHub Repository
5. Add Environment Variables
6. Deploy Project

---

☁️ Heroku Deployment

Steps

1. Fork Repository
2. Create Heroku App
3. Connect GitHub Repository
4. Add Config Vars
5. Deploy

---

📜 Commands

Command| Description
/play| Play Music
/skip| Skip Current Song
/pause| Pause Music
/resume| Resume Music
/stop| Stop Streaming
/queue| Show Queue
/ping| Check Bot Speed
/broadcast| Broadcast Message

---

⚡ Powered By

- Pyrogram
- PyTgCalls
- MongoDB
- FFmpeg
- Python 3.11

---

📌 Recommended VPS

Minimum

- 1 GB RAM
- 1 vCPU

Recommended

- 2 GB RAM
- Ubuntu 22.04

---

❤️ Credits

- Pyrogram
- PyTgCalls
- Telegram

---

📄 License

This Project Is Licensed Under MIT License.

---

⭐ Support

If You Like This Project:

- Star The Repository
- Fork The Project
- Share With Friends

---

👑 Developed By

Team AlfaBots

Powered By AlfaBots
