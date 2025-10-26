from aiogram import Router, types, F
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest

from config.settings import ADMIN_ID
from database.operations import get_users_all
from bot.keyboards.inline import get_main_keyboard

router: Router = Router()


@router.message(F.from_user.id == ADMIN_ID)
async def admin_message(message: types.Message, lang: str):
    is_admin = message.from_user.id if message.from_user.id == ADMIN_ID else None
    text = message.text if is_admin else None
    users = await get_users_all()
    cnt = 0
    for user in users:
        try:
            if user != ADMIN_ID:
                await message.bot.send_message(
                    user,
                    text,
                    reply_markup=get_main_keyboard(lang)
                )
                cnt += 1

        except (TelegramBadRequest, TelegramForbiddenError):
            pass
    await message.answer(f"✅ Successfully shipped {cnt} users.")
