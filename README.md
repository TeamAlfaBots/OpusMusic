<div align="center">

<img src="https://files.catbox.moe/oc0vh3.svg" width="100%" alt="OpusMusic Banner"/>

<br>

<h1>🎵 OpusMusic</h1>

<p>
High Performance Telegram Music Bot Built With Pyrogram & Py-TgCalls
</p>

<p>
Supports YouTube, Spotify, Apple Music, SoundCloud & Live Streams
</p>

<br>

<a href="https://github.com/TeamAlfaBots/OpusMusic/stargazers">
  <img src="https://img.shields.io/github/stars/TeamAlfaBots/OpusMusic?style=for-the-badge&color=8b5cf6&logo=github">
</a>

<a href="https://github.com/TeamAlfaBots/OpusMusic/network/members">
  <img src="https://img.shields.io/github/forks/TeamAlfaBots/OpusMusic?style=for-the-badge&color=06b6d4&logo=github">
</a>

<a href="https://www.python.org">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
</a>

<a href="#">
  <img src="https://img.shields.io/badge/Powered%20By-AlfaBots-purple?style=for-the-badge">
</a>

</div>

---

# ✨ Features

<table>
<tr>
<td>🎧 High Quality Audio Streaming</td>
<td>⚡ Fast & Optimized Playback</td>
</tr>

<tr>
<td>🔎 YouTube Search & Direct Play</td>
<td>📜 Smart Queue Management</td>
</tr>

<tr>
<td>⏯ Pause / Resume / Skip</td>
<td>🔁 Loop & Seek Support</td>
</tr>

<tr>
<td>🌍 Multi Language Support</td>
<td>📢 Broadcast System</td>
</tr>

<tr>
<td>🐳 Docker Ready</td>
<td>☁️ Railway / VPS / Heroku Deploy</td>
</tr>
</table>

---

# 📂 Project Structure

```bash
OpusMusic/
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

🚀 Deploy On VPS

1️⃣ Install Required Packages

sudo apt update
sudo apt install ffmpeg git python3 python3-pip -y

---

2️⃣ Clone Repository

git clone https://github.com/TeamAlfaBots/OpusMusic
cd OpusMusic

---

3️⃣ Install Python Dependencies

«This project uses "pyproject.toml"»

pip3 install -U pip setuptools wheel
pip install .

---

4️⃣ Configure Environment Variables

cp sample.env .env
nano .env

Fill Required Variables:

API_ID=
API_HASH=
BOT_TOKEN=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=
LOGGER_ID=

---

5️⃣ Start The Bot

bash start

OR

python -m opus

---

🐳 Docker Deployment

Build Docker Image

docker build -t opusmusic .

Run Docker Container

docker run -d \
--name opusmusic \
--env-file .env \
opusmusic

---

☁️ Railway Deployment

Easy Steps

1. Upload Project To GitHub
2. Open Railway
3. Create New Project
4. Connect GitHub Repository
5. Add Environment Variables
6. Deploy Project

---

☁️ Heroku Deployment

<div align="center"><a href="https://dashboard.heroku.com/new">
  <img src="https://img.shields.io/badge/Deploy%20To-Heroku-7952B3?style=for-the-badge&logo=heroku&logoColor=white">
</a></div>---

⚙️ Environment Variables

Variable| Description
API_ID| Telegram API ID
API_HASH| Telegram API HASH
BOT_TOKEN| Telegram Bot Token
MONGO_DB_URI| MongoDB Database URL
OWNER_ID| Telegram User ID
STRING_SESSION| Assistant Session String
LOGGER_ID| Log Group ID

---

📜 Commands

Command| Description
/play| Play Music
/vplay| Play Video
/pause| Pause Playback
/resume| Resume Playback
/skip| Skip Current Track
/stop| Stop Streaming
/queue| Show Queue
/seek| Seek Stream
/ping| Check Ping

---

💻 Tech Stack

- Python 3.11
- Pyrogram
- Py-TgCalls
- MongoDB
- FFmpeg
- Docker

---

📌 Recommended VPS

Type| Specs
Minimum| 1GB RAM • 1 vCPU
Recommended| 2GB RAM • Ubuntu 22.04

---

❤️ Credits

- Pyrogram
- Py-TgCalls
- FFmpeg
- Telegram

---

📄 License

This project is licensed under the MIT License.

---

🌟 Support The Project

If you like this project:

- ⭐ Star the Repository
- 🍴 Fork the Repository
- 📢 Share with Friends

---

<div align="center">👑 Developed By Team AlfaBots

Powered By AlfaBots

</div>
```
