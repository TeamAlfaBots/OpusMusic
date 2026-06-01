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

from pathlib import Path


def _list_modules():
    """
    List all Python module filenames (without extension)
    in the current directory excluding __init__.py
    """

    mod_dir = Path(__file__).parent

    return [
        file.stem
        for file in mod_dir.glob("*.py")
        if file.is_file() and file.name != "__init__.py"
    ]


all_modules = frozenset(sorted(_list_modules()))
