import json
from datetime import date
from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command

from bot.keyboards.inline import get_language_keyboard, get_main_keyboard
# ❗ ІМПОРТУЄМО ФУНКЦІЮ ЗБЕРЕЖЕННЯ ID
from database.operations import get_or_create_user, update_user_last_message_id
# ❗ ІМПОРТУЄМО ФУНКЦІЮ ВИДАЛЕННЯ
from utils.message_utils import try_delete_message
from utils.logger import AppLogging

with open("data/text_menu.json", "r", encoding="utf-8") as f:
    texts = json.load(f)

with open("data/media_ids/birthday_ids.json", "r", encoding="utf-8") as f:
    birthday_ids = json.load(f)

logger = AppLogging.get_logger()
router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message) -> None:
    user = await get_or_create_user(message.from_user.id)
    user_name = message.from_user.first_name
    today = date.today()

    if user.last_message_id:
        await try_delete_message(message.bot, message.from_user.id, user.last_message_id)



    if user.birth_date and isinstance(user.birth_date,
                                      date) and user.birth_date.month == today.month and user.birth_date.day == today.day:
        if "birthday" in birthday_ids:
            file_id = birthday_ids["birthday"]

    if user.language:
        sent_msg_with_keyboard = await message.answer(
            text=texts["menu"]["ua"]["main_menu_title"].replace("{name}", user_name),
            reply_markup=get_main_keyboard(user.language),
            parse_mode="HTML",
        )
    else:
        text = texts["menu"]["ua"]["choose_language"].replace("{name}", user_name)
        sent_msg_with_keyboard = await message.answer(
            text=text,
            reply_markup=get_language_keyboard(),
            parse_mode="HTML"
        )

    if sent_msg_with_keyboard:
        await update_user_last_message_id(message.from_user.id, sent_msg_with_keyboard.message_id)

    try:
        await message.delete()
        logger.debug(f"🗑️ Delete /start command from user {message.from_user}")
    except TelegramBadRequest as e:
        logger.warning(f"⚠️ Could not delete /start command: {e}")
        pass