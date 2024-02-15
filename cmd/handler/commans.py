from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command

command_router=Router()

@command_router.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(text="<b>keldizmi</b>")
@command_router.message(Command('help'))
async def start_handler(message:Message):
    await message.answer(text="<b>ketasizmi</b>")
@command_router.message(Command('restart'))
async def start_handler(message:Message):
    await message.delete()