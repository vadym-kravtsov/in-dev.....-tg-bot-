
import asyncio
from utils.logger import AppLogging
from aiogram import Bot, Dispatcher


from setup import preload_card, setup_dispatcher

from config.settings import BOT_TOKEN

logger = AppLogging.get_logger()


async def main():
    try:
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()
        logger.info("✅ Bot and dispatcher create")
    except Exception as e:
        logger.exception(f"❌ Failed to create bot {e}")
        raise

    await preload_card()
    await setup_dispatcher(dp)

    logger.info("✅ The bot is starting")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("The Bot has been stopped ⛔")