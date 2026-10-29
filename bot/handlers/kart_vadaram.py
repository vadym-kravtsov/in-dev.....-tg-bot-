from aiogram import types, Router, F
from bot.keyboards.reply_k import obusha_r_k
from constants.media_ids.vadaram_ids import IDS_vdr
from data.desc_cards.ua import vdr_ua
from random import randint

router: Router = Router()


@router.message(F.text == "Vadaram")
async def obusha_handler(message: types.Message) -> None:
    await message.delete()  # delete the user's message to keep the chat clean
    key = randint(1, 80)
    kart = IDS_vdr[key]
    await message.answer_photo(
        photo=kart,
        caption=vdr_ua[key],
        reply_markup=obusha_r_k(),
    )
