# ╔══════════════════════════════════════════════╗
# ║               OpusMusic Bot                 ║
# ║        Advanced Telegram Music System       ║
# ╚══════════════════════════════════════════════╝
#
#  Copyright © 2026 Opus
#  Licensed under the Opus Software License.
#
#  Developed for high performance music streaming,
#  voice chat management and Telegram automation.
#
#  Project: OpusMusic
#  Powered by AlfaBots
#


import shutil
from pathlib import Path

from opus import logger


def ensure_dirs():
    """
    Ensure that the necessary directories exist.
    """
    if not shutil.which("deno") or not shutil.which("ffmpeg"):
        raise RuntimeError("Deno and FFmpeg must be installed and accessible in the system PATH.")

    for dir in ["cache", "downloads"]:
        Path(dir).mkdir(parents=True, exist_ok=True)
    logger.info("Cache directories updated.")
