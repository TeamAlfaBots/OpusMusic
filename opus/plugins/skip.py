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

from pyrogram import (
    filters,
    types
)

from opus import (
    Opus,
    app,
    db,
    lang
)

from opus.helpers import (
    can_manage_vc
)


@app.on_message(
    filters.command(
        [
            "skip",
            "next"
        ]
    )
    & filters.group
    & ~app.bl_users
)
@lang.language()
@can_manage_vc
async def _skip(
    _,
    m: types.Message
):

    if not await db.get_call(
        m.chat.id
    ):

        return await m.reply_text(
            m.lang["not_playing"]
        )

    await Opus.play_next(
        m.chat.id
    )

    await m.reply_text(
        m.lang["play_skipped"].format(
            m.from_user.mention
        )
    )
