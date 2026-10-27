import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import log
from bot.handlers.start_handler import router as start_handler
from bot.handlers.kart_obusha import router as obusha_handler
from bot.handlers.kart_vadaram import router as vadaram_handler
token = os.environ["tg_token"]

dp = Dispatcher()


async def main():
    dp.include_router(start_handler)
    dp.include_router(obusha_handler)
    dp.include_router(vadaram_handler)
    try:
        bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML"))
        log.logger.info("bot started successfully.....")
        await dp.start_polling(bot)
    except Exception as e:
        log.logger.error(f"Error initializing bot: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        print("bot stopped")
    log.logger.info("bot stopped!")
