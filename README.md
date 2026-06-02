<p align="center">
  <img src="assets/md.svg" alt="OpusMusic Banner">
</p>

<h1 align="center">🎵 OpusMusic</h1>

<p align="center">
 Powerful Telegram Music Bot Built Using Pyrogram & PyTgCalls
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Telegram-MusicBot-2ea44f?style=for-the-badge&logo=telegram">
  <img src="https://img.shields.io/badge/Platform-VPS%20%7C%20Docker%20%7C%20Railway-purple?style=for-the-badge">
</p>

---

# ✨ Features

- 🎧 Voice Chat Music Streaming
- 🔎 YouTube Search & Play
- ⏯ Pause / Resume / Skip
- 📜 Queue System
- 🌍 Multi Language Support
- 📢 Broadcast Feature
- ⚡ Fast & Optimized
- 🐳 Docker Ready

---

# 📂 Project Structure

```bash
OpusMusic-main/
│
├── assets/
│   └── md.svg
│
├── opus/
├── pyproject.toml
├── Dockerfile
├── sample.env
├── start
└── README.md

---

🚀 VPS Deployment

Install Dependencies

sudo apt update && sudo apt install ffmpeg git python3 python3-pip -y

---

Upload Project

unzip OpusMusic-main.zip
cd OpusMusic-main

---

Install Packages

pip3 install -U pip setuptools wheel
pip install .

---

Setup Env

cp sample.env .env
nano .env

Fill:

API_ID=
API_HASH=
BOT_TOKEN=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=

---

Start Bot

bash start

OR

python -m opus

---

🐳 Docker Deploy

docker build -t opusmusic .
docker run -d --name opusmusic --env-file .env opusmusic

---

❤️ Team AlfaBots
