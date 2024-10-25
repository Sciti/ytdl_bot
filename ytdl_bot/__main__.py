import asyncio
import sys
import os

from ytdl_bot.log import configure_logging
from ytdl_bot.bot import CandyDLBot



async def main():

    configure_logging()
    bot = CandyDLBot()
    await bot.set_commands(
        [
            ('start', 'Начать работу'),
            ('help', 'Помощь'),
            ('download', 'Скачать видео'),
            ('download_mp3', 'Скачать аудио'),
        ]
    )
    await bot.run()


if __name__ == '__main__':
    asyncio.run(main())