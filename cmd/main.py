import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from config import Bot_Token
from aiogram import types
from aiogram.enums import ParseMode
from handler.commans import command_router
from aiogram.types import BotCommand
from handler.massage_handler import massage_router



async def main():
    bot=Bot(token=Bot_Token,parse_mode=ParseMode.HTML,disable_web_page_preview=True)
    await bot.set_my_commands( 
        commands=[
        BotCommand(command='start',description='Start/restart bot'),
        BotCommand(command='help',description='can you help bot'),
        BotCommand(command='restart',description='tozalash')
        ]
    )
    dp=Dispatcher()
    dp.include_router(command_router,massage_router)
    await dp.start_polling(bot)
    
if __name__ =="__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot stoped")
    