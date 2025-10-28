from aiogram import Router, types, F
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest

from config.settings import ADMIN_ID
from database.operations import get_users_all, update_user_last_message_id
from bot.keyboards.inline import get_main_keyboard
# ❗ ЗМІНЕНО: Припускаємо, що ви змінили цю функцію на try_delete_message
from utils.message_utils import try_delete_message

router: Router = Router()


@router.message(F.from_user.id == ADMIN_ID)
async def admin_message(message: types.Message):
    users_data = await get_users_all()
    cnt = 0
    for user_data in users_data:
        recipient_id = user_data.telegram_id
        if recipient_id == ADMIN_ID:
            continue
        try:
            recipient_lang = user_data.language or "ua"
            keyboard = get_main_keyboard(recipient_lang)

            if user_data.last_message_id:
                await try_delete_message(message.bot, recipient_id, user_data.last_message_id)
            sent_msg = await message.copy_to(
                chat_id=recipient_id,
                reply_markup=keyboard
            )
            await update_user_last_message_id(recipient_id, sent_msg.message_id)
            cnt += 1
        except (TelegramBadRequest, TelegramForbiddenError):
            pass
    await message.answer(f"✅ Successfully shipped {cnt} users.")
