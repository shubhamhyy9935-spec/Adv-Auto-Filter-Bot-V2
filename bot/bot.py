#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyrogram import Client, enums
from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 
from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "bot/plugins"
            },
            workers=200,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username} started!"
        )
        try:
            self.USER, self.USER_ID = await User().start()
        except Exception as e:
            self.LOGGER(__name__).warning(f"Userbot failed: {e}")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
