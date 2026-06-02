🎵 OpusMusic

<p align="center">
  <img src="https://img.shields.io/badge/Telegram-Music%20Bot-blue?style=for-the-badge&logo=telegram">
  <img src="https://img.shields.io/github/license/yourusername/OpusMusic?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.11-yellow?style=for-the-badge&logo=python">
</p><p align="center">
 Powerful Telegram Music Bot Based On Pyrogram & PyTgCalls
</p>---

✨ Features

- 🎧 Voice Chat Music Streaming
- 🔎 YouTube Search & Play
- ⏯ Pause / Resume / Skip / Stop
- 📜 Queue System
- 🔁 Loop Mode
- 🌍 Multi Language Support
- 👮 Admin & Auth System
- 📢 Broadcast Feature
- ⚡ Fast & Optimized
- 🐳 Docker Support
- ☁️ VPS / Railway / Heroku Deploy
- 🔥 Clean Modular Structure

---

📂 Project Structure

OpusMusic-main/
│
├── opus/
│   ├── core/
│   ├── helpers/
│   ├── plugins/
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

🚀 Deploy Guide

🔹 Requirements

- Python 3.11+
- FFmpeg
- MongoDB
- Telegram Bot Token
- Telegram API ID & HASH
- Assistant String Session

---

🔑 Get Required Variables

Telegram API

Go To:

https://my.telegram.org

Create App And Copy:

- API_ID
- API_HASH

---

Create Bot

Open Telegram And Search:

@BotFather

Create Bot And Copy:

- BOT_TOKEN

---

MongoDB URL

Create Free MongoDB Database:

https://www.mongodb.com/cloud/atlas

Copy Mongo URI.

---

⚙️ VPS / Ubuntu Deployment

1️⃣ Install Dependencies

sudo apt update && sudo apt install ffmpeg python3 python3-pip git -y

---

2️⃣ Upload Project

unzip OpusMusic-main.zip
cd OpusMusic-main

---

3️⃣ Install Python Packages

Since project uses "pyproject.toml":

pip3 install -U pip setuptools wheel
pip install .

---

4️⃣ Setup Environment Variables

cp sample.env .env
nano .env

Fill Variables:

API_ID=
API_HASH=
BOT_TOKEN=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=

---

5️⃣ Start Bot

bash start

OR

python -m opus

---

🐳 Docker Deployment

Build Docker Image

docker build -t opusmusic .

Run Container

docker run -d --name opusmusic --env-file .env opusmusic

---

☁️ Railway Deployment

1. Upload Project To GitHub
2. Open Railway
3. Create New Project
4. Connect GitHub Repo
5. Add Environment Variables
6. Deploy

---

☁️ Heroku Deployment

1. Fork Repository
2. Create Heroku App
3. Connect GitHub
4. Add Variables
5. Deploy

---

🔥 Important Notes

FFmpeg Required

Install FFmpeg:

sudo apt install ffmpeg

---

Assistant String Session

Generate Pyrogram String Session.

You Can Use Any Trusted String Generator.

---

📜 Commands

Command| Description
/play| Play Music
/skip| Skip Current Song
/pause| Pause Stream
/resume| Resume Stream
/stop| Stop Streaming
/queue| Show Queue
/ping| Check Ping
/broadcast| Broadcast Message

---

🛠 Built With

- Python
- Pyrogram
- PyTgCalls
- MongoDB
- FFmpeg
- Docker

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
