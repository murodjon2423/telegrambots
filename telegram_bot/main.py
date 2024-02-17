import asyncio

import logging

from aiogram import Bot,Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handler.commands_handler import command_router
from handler.mro import message_router

async def main():
    bot=Bot( token=BOT_TOKEN,
             parse_mode=ParseMode.HTML,
             disable_web_page_preview=True)
    await bot.set_my_commands(
        commands=[
            BotCommand(command='start',description='Start/restart bot'),
            BotCommand(command='help',description='yo`riqnoma'),
            BotCommand(command='usd',description='usd course take'),
            BotCommand(command='eur',description='eur course take'),
            BotCommand(command='rub',description='rub course take'),
            BotCommand(command='all',description='all course take')
        ]
    )
    dp=Dispatcher()
    dp.include_router(message_router,command_router)
    await dp.start_polling(bot)

if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot stoped")


