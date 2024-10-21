from aiogram import F, Router, types
from aiogram.filters import Command, CommandObject

from logging import getLogger


from candy_dl.bot import keyboards as kb
from candy_dl.download import download_mp3, download_mp4


download_router = Router()
logger = getLogger(__name__)

#start command
@download_router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(
        text=("Привет! Я бот для скачивания видео с YouTube.\n"
              "Для загрузки видео: /download url\n"
              "Для загрузки аудио: /download_mp3 url\n"
              "Или кнопки ниже."),
        reply_markup=kb.main_menu()
    )


@download_router.message(Command('download'))
async def download_video_message(message: types.Message, command: CommandObject):
    video_url = command.args
    data = download_mp4(video_url)

    video_id = data.get('id')
    video_title = data.get('title')

    video = types.FSInputFile(f'cache/video/{video_id}.mp4')
    await message.answer_video(video, caption=video_title)


@download_router.message(Command('download_mp3'))
async def download_audio_message(message: types.Message):
    ...


@download_router.callback_query(F.data == 'download')
async def download_video_callback(callback: types.CallbackQuery):
    ...


@download_router.callback_query(F.data == 'download_mp3')
async def download_audio_callback(callback: types.CallbackQuery):
    ...