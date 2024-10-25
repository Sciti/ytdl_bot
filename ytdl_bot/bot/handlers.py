from aiogram import F, Router, types
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext

from logging import getLogger


from ytdl_bot.bot import filters
from ytdl_bot.bot import keyboards as kb
from ytdl_bot.download import download_mp3_async, download_mp4_async
from ytdl_bot.conf import settings


download_router = Router()
logger = getLogger(__name__)
link = "https://www.youtube.com/"

#MARK: Filters
@download_router.message(filters.LinkFilter(link))
async def process_link(message: types.Message, state: FSMContext):
    link: str = message.text
    await state.update_data(link=link)
    await message.answer(
        text=f"Выбери формат",
        reply_markup=kb.main_menu()
    )

#MARK: Commands
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
    data = await download_mp4_async(video_url)

    video_id = data.get('id')
    video_title = data.get('title')

    video = types.FSInputFile(f'cache/video/{video_id}.mp4')
    await message.answer_video(video, caption=video_title)


@download_router.message(Command('download_mp3'))
async def download_audio_message(message: types.Message, command: CommandObject):
    audio_url = command.args
    data = await download_mp3_async(audio_url)

    audio_id = data.get('id')
    audio_title = data.get('title')

    audio = types.FSInputFile(f'cache/audio/{audio_id}.mp3')
    await message.answer_audio(audio, caption=audio_title)

#MARK: Callback query
@download_router.callback_query(F.data == 'download')
async def download_video_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    state_data = await state.get_data()
    link = state_data.get('link')

    data = await download_mp4_async(link)

    video_id = data.get('id')
    video_title = data.get('title')

    video = types.FSInputFile(f'cache/video/{video_id}.mp4')
    await callback.message.answer_video(video, caption=video_title)


@download_router.callback_query(F.data == 'download_mp3')
async def download_audio_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    state_data = await state.get_data()
    link = state_data.get('link')

    data = await download_mp3_async(link)

    audio_id = data.get('id')
    audio_title = data.get('title')

    audio = types.FSInputFile(f'cache/audio/{audio_id}.mp3')
    await callback.message.answer_audio(audio, caption=audio_title)