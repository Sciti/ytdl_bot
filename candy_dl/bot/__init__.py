from aiogram import Bot, Dispatcher, types, enums
from aiogram.client.default import DefaultBotProperties
from aiogram.client.telegram import TelegramAPIServer
from aiogram.client.session.aiohttp import AiohttpSession

from candy_dl.conf import settings
from candy_dl.bot.handlers import download_router


class CandyDLBot:
    def __init__(self):
        local_server = AiohttpSession(
           api=TelegramAPIServer.from_base('http://localhost:8081')
        )
        self.bot = Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=enums.ParseMode.HTML,
                link_preview_is_disabled=True
            ),
            session=local_server
        )
        self.dp = Dispatcher()


    async def run(self):
        await self._register_routers()
        await self.dp.start_polling(self.bot)


    async def _register_routers(self):
        self.dp.include_router(download_router)

    async def set_commands(self, commands: list[tuple]):
        commands = [
            types.BotCommand(command=command, description=desc)
            for command, desc in commands
        ]

        await self.bot.set_my_commands(commands)


    async def logout(self):
        await self.bot.log_out()