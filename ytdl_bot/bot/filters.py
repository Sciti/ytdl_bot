from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery

class LinkFilter(Filter):
    def __init__(self, link: str) -> None:
        self.link = link

    async def __call__(self, message: Message) -> bool:
        return message.text.startswith(self.link)