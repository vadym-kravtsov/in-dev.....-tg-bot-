from aiogram.exceptions import TelegramBadRequest, TelegramAPIError
from aiogram import Bot
from utils.logger import AppLogging

logger = AppLogging.get_logger()

async def try_delete_message(bot: Bot, chat_id: int, message_id: int) -> bool:
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        return True
    except TelegramBadRequest as e:
        logger.warning(f"Failed to delete message {message_id}: {e}")
        return False
    except TelegramAPIError as e:
        logger.error(f"Telegram API error while deleting message {message_id}: {e}")
        return False
    except Exception as e:
        logger.exception(f"Unexpected error while deleting message {message_id}: {e}")
        return False