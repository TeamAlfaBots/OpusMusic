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

import os
import asyncio

from pyrogram import errors, filters, types

from opus import app, db, lang


broadcasting = asyncio.Lock()


@app.on_message(
    filters.command(["broadcast"])
    & app.sudoers
)
@lang.language()
async def _broadcast(_, message: types.Message):

    if not message.reply_to_message:
        return await message.reply_text(
            message.lang["gcast_usage"]
        )

    if broadcasting.locked():
        return await message.reply_text(
            message.lang["gcast_active"]
        )

    msg = message.reply_to_message

    copy = "-copy" in message.command

    count = 0
    ucount = 0

    groups = set()
    users = set()

    sent = await message.reply_text(
        message.lang["gcast_start"]
    )

    if "-nochat" not in message.command:
        groups = set(await db.get_chats())

    if "-user" in message.command:
        users = set(await db.get_users())

    chats = list(groups | users)

    failed = None

    async with broadcasting:

        for chat in chats:

            try:

                if copy:
                    await msg.copy(
                        chat,
                        reply_markup=msg.reply_markup
                    )

                else:
                    await msg.forward(chat)

                if chat in groups:
                    count += 1

                else:
                    ucount += 1

                await asyncio.sleep(0.2)

            except errors.FloodWait as fw:

                await asyncio.sleep(
                    fw.value + 10
                )

            except Exception as ex:

                if not failed:
                    failed = open(
                        "errors.txt",
                        "w"
                    )

                failed.write(
                    f"{chat} - {ex}\n"
                )

                continue

    text = message.lang["gcast_end"].format(
        count,
        ucount
    )

    if failed:

        failed.close()

        await message.reply_document(
            document="errors.txt",
            caption=text,
        )

        try:
            os.remove("errors.txt")

        except Exception:
            pass

    await sent.edit_text(text)
