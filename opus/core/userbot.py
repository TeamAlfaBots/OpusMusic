# ╔══════════════════════════════════════════════╗
# ║               OpusMusic Bot                 ║
# ║        Advanced Telegram Music System       ║
# ╚══════════════════════════════════════════════╝

from pyrogram import Client

from opus import config, logger


class Userbot(Client):
    def __init__(self):
        self.clients = []

        clients = {
            "one": "SESSION1",
            "two": "SESSION2",
            "three": "SESSION3",
        }

        for key, string_key in clients.items():
            name = f"OpusUB{key[-1]}"
            session = getattr(config, string_key)

            if not session:
                continue

            setattr(
                self,
                key,
                Client(
                    name=name,
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=session,
                ),
            )

    async def boot_client(self, num: int, ub: Client):
        clients = {
            1: getattr(self, "one", None),
            2: getattr(self, "two", None),
            3: getattr(self, "three", None),
        }

        client = clients[num]

        if not client:
            logger.error(f"Assistant {num} client not found.")
            return

        try:
            await client.start()

            me = await client.get_me()

            client.id = me.id
            client.name = me.first_name
            client.username = me.username
            client.mention = me.mention

            self.clients.append(client)

            try:
                await client.send_message(config.LOGGER_ID, "Assistant Started")
            except Exception as e:
                logger.error(f"Assistant {num} logger error: {e}")

            try:
                await ub.join_chat("fallenx")
            except Exception:
                pass

            logger.info(
                f"Assistant {num} started as @{client.username}"
            )

        except Exception as e:
            logger.error(f"Assistant {num} failed to start: {e}")

    async def boot(self):
        if config.SESSION1:
            await self.boot_client(1, self.one)

        if config.SESSION2:
            await self.boot_client(2, self.two)

        if config.SESSION3:
            await self.boot_client(3, self.three)

    async def exit(self):
        if config.SESSION1:
            await self.one.stop()

        if config.SESSION2:
            await self.two.stop()

        if config.SESSION3:
            await self.three.stop()

        logger.info("Assistants stopped.")