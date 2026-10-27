from aiogram import types, Router, F
from bot.keyboards.reply_k import obusha_r_k
from constants.media_ids.obusha_ids import IDS_ob
from data.desc_cards.ua import ob_ua
from random import randint

router: Router = Router()


@router.message(F.text == "Obusha")
async def obusha_handler(message: types.Message) -> None:
    key = randint(1, 78)
    kart = IDS_ob[key]
    await message.answer_photo(
        photo=kart,
        caption=ob_ua[key],
        reply_markup=obusha_r_k(),
    )