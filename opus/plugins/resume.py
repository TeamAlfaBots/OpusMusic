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
    buttons,
    can_manage_vc
)


@app.on_message(
    filters.command(["resume"])
    & filters.group
    & ~app.bl_users
)
@lang.language()
@can_manage_vc
async def _resume(
    _,
    m: types.Message
):

    if not await db.get_call(m.chat.id):

        return await m.reply_text(
            m.lang["not_playing"]
        )

    if await db.playing(m.chat.id):

        return await m.reply_text(
            m.lang["play_not_paused"]
        )

    await Opus.resume(
        m.chat.id
    )

    await m.reply_text(
        text=m.lang["play_resumed"].format(
            m.from_user.mention
        ),
        reply_markup=buttons.controls(
            m.chat.id
        ),
    )
