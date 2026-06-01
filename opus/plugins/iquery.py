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

from py_yt import VideosSearch
from pyrogram import types

from opus import app
from opus.helpers import buttons


@app.on_inline_query(~app.bl_users)
async def inline_query_handler(_, query: types.InlineQuery):

    text = query.query.strip().lower()

    if not text:
        return

    try:

        search = VideosSearch(
            text,
            limit=15
        )

        results = (
            await search.next()
        ).get("result", [])

        answers = []

        for video in results:

            title = video.get(
                "title",
                "Unknown Title"
            ).title()

            duration = video.get(
                "duration",
                "N/A"
            )

            views = video.get(
                "viewCount",
                {}
            ).get(
                "short",
                "N/A"
            )

            thumbnail = video.get(
                "thumbnails",
                [{}]
            )[0].get(
                "url",
                ""
            ).split("?")[0]

            channel = video.get(
                "channel",
                {}
            ).get(
                "name",
                "Unknown Channel"
            )

            channellink = video.get(
                "channel",
                {}
            ).get(
                "link",
                "https://youtube.com"
            )

            link = video.get(
                "link",
                "https://youtube.com"
            )

            published = video.get(
                "publishedTime",
                "N/A"
            )

            description = (
                f"{views} | "
                f"{duration} | "
                f"{channel} | "
                f"{published}"
            )

            caption = (
                f"<b>Title:</b> "
                f"<a href='{link}'>{title[:250]}</a>\n\n"

                f"<b>Duration:</b> {duration}\n"

                f"<b>Views:</b> "
                f"<code>{views}</code>\n"

                f"<b>Channel:</b> "
                f"<a href='{channellink}'>{channel}</a>\n"

                f"<b>Published:</b> {published}\n\n"

                f"<u><i>Fetched by {app.name}</i></u>"
            )

            answers.append(
                types.InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    description=description,
                    caption=caption,
                    reply_markup=buttons.yt_key(link),
                )
            )

        if answers:

            await app.answer_inline_query(
                query.id,
                results=answers,
                cache_time=5
            )

    except Exception:
        pass
