from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.keyboards.reply_k import obusha_r_k

router: Router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer(
        "Hello! Welcome to the bot. Please choose an option from the menu.",
        reply_markup=obusha_r_k(),
    )
