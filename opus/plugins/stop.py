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
    filters.command(["end", "stop"])
    & filters.group
    & ~app.bl_users
)
@lang.language()
@can_manage_vc
async def _stop(
    _,
    m: types.Message
):

    if len(m.command) > 1:
        return

    call = await db.get_call(
        m.chat.id
    )

    await Opus.stop(
        m.chat.id
    )

    if not call:
        return await m.reply_text(
            m.lang["not_playing"]
        )

    await m.reply_text(
        m.lang["play_stopped"].format(
            m.from_user.mention
        )
    )
