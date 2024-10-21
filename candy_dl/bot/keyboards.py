from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Скачать видео', callback_data='download'),
        InlineKeyboardButton(text='Скачать аудио', callback_data='download_mp3')
    )

    return builder.as_markup()