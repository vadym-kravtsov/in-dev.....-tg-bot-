from aiogram import Router, types
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest
from config.settings import ADMIN_ID
from database.operations import get_users_all, update_user_last_message_id
from bot.keyboards.inline import  get_main_keyboard
from utils.message_utils import try_delete_message
from utils.logger import AppLogging

logger = AppLogging.get_logger()
router = Router()

@router.message()
async def admin_message(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    users_data = await get_users_all()
    logger.info(f"Fetched {len(users_data)} users")

    cnt = 0
    for user_data in users_data:
        # if user_data.telegram_id == ADMIN_ID:
        #     continue

        try:
            keyboard = get_main_keyboard(user_data.language or "ua")


            sent_msg = await message.copy_to(
                chat_id=user_data.telegram_id,
                reply_markup=keyboard
            )
            if user_data.last_message_id:
                await try_delete_message(message.bot, user_data.telegram_id, user_data.last_message_id)

            await update_user_last_message_id(user_data.telegram_id, sent_msg.message_id)
            cnt += 1

        except (TelegramBadRequest, TelegramForbiddenError):
            pass

    await message.answer(f"✅ Message {cnt} users")
