from typing import Callable, Any
from aiogram import BaseMiddleware, types

from ytdl_bot.db.repository import Repository

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, db_path: str) -> None:
        self.repository = Repository(db_path)

    async def __call__(
        self,
        handler: Callable[[types.Update, dict[str, Any]], Any],
        event: types.Update,
        data: dict[str, Any],
    ) -> Any:
        data['repository'] = self.repository
        await handler(event, data)

class AccessMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.Message, dict[str, Any]], Any],
        event: types.Message,
        data: dict[str, Any],
    ) -> Any:
        repository = data.get('repository')
        db_user = repository.get_user(telegram_id=event.from_user.id)
        if not db_user:
            repository.add_user(
                telegram_id=event.from_user.id,
                username=event.from_user.username,
                role="unknown"
            )
            return
        
        await handler(event, data)
