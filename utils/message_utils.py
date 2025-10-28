from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot
from utils.logger import AppLogging

logger = AppLogging.get_logger()


async def try_delete_message(bot: Bot, chat_id: int, message_id: int) -> bool:
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        logger.info(f"🗑️ Message {message_id} successfully deleted in chat {chat_id}.")
    except TelegramBadRequest as e:
        logger.info(f"!!!!!!!!!! Message no delete {e}")
    return False
