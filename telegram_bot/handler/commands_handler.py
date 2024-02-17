from aiogram import Router
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.filters import CommandStart,Command
from aiogram.utils.chat_action import ChatActionSender
import requests

from config import currencies, CBU_URL

command_router=Router()


@command_router.message(CommandStart())
async def hendler_start(message:Message):
    s="Bizni botga hush kelibsiz\n\n"
    s+="Meta tarmog`idan yuklab oluvchi\n"
    s+="eng tez eng qulay bot "
    await message.answer(text=s)
@command_router.message(Command('help'))
async def help_handler(message:Message):
    s="<b>Bot qanday ishlashi haqida </b>\n\n"
    s+="/start tugmasini bosing\n\n"
    s+="Valyuta kursini belgilang \n"
    s+="/usd kursini olish\n"
    s+="/eur kursini olish\n"
    s+="/rub kursini olish\n"
    s+="/all kursini olish\n\n"
    s+="konvertasiya summasini jo`nating \n"
    s+="100 \n\n"
    s+="@myonetel_bot"
    await message.reply(text=s)
    
@command_router.message(Command('all', prefix='!#&?/'))
async def courses_handler(message: Message):
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.from_user.id):
        response = requests.get(CBU_URL)

        s = "Today's currency rates:\n\n"

        for course in response.json():
            if course['Ccy'] in currencies.keys():
                currencies[course['Ccy']]['rate'] = course['Rate']
                s += f"\t - 1 {course['CcyNm_EN']} is {course['Rate']} sum\n"
        await message.answer(text=s)


@command_router.message(Command('usd', prefix='$!/#'))
async def usd_handler(message: Message):
    response = requests.get(f"{CBU_URL}USD/")
    res = response.json()[0]
    s = f"1 {res['CcyNm_EN']} = {res['Rate']} sums"
    await message.reply(text=s)


@command_router.message(Command('eur', prefix='$!/#'))
async def eur_handler(message: Message):
    response = requests.get(f"{CBU_URL}EUR/")
    res = response.json()[0]
    s = f"1 {res['CcyNm_EN']} = {res['Rate']} sums"
    await message.reply(s)


@command_router.message(Command('rub', prefix='$!/#'))
async def rub_handler(message: Message):
    response = requests.get(f"{CBU_URL}RUB/")
    res = response.json()[0]
    s = f"1 {res['CcyNm_EN']} = {res['Rate']} sums"
    await message.reply(s)

