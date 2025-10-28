from services.card_service import CardService

from database.database import init_db, reset_db_once  # ❗❗❗
from utils.logger import AppLogging
from bot.middlewares.user_middleware import UserMiddleware

from bot.handlers.start import router as start_router
from bot.handlers.callbacks import router as callback_router
from bot.handlers.cards_family_advice import router as card_family_advice
from bot.handlers.birth_date_calendar import router as birth_date_calendar
from bot.handlers.cards_obusha import router as cards_obusha
from bot.handlers.cards_vadaram import router as cards_vadaram
from bot.handlers.admin import router as admin_message

from aiogram import Dispatcher

app = AppLogging()
logger = app.get_logger()


async def preload_card():
    languages = ["ru", "ua", "en"]

    for lang in languages:
        try:
            # ❗ 1. ЗАВАНТАЖЕННЯ КОЛОДИ 'obusha' (як у вас було)
            await CardService.get_card_descriptions("1", "obusha", lang)

            # ❗ 2. ДОДАНО: ЗАВАНТАЖЕННЯ КОЛОДИ 'family_advice'
            # Припускаємо, що cards_family_advice використовує карти з 1 по 80
            await CardService.get_card_descriptions("1", "family_advice", lang)

            logger.info(f"✅ Language {lang} loader")
        except Exception as e:
            logger.exception(f"❌ error {lang}: {e}")


async def setup_dispatcher(dp: Dispatcher):
    try:
        dp.message.middleware(UserMiddleware())
        logger.info("✅ The Middleware for message is registered ")
        dp.callback_query.middleware(UserMiddleware())
        logger.info("✅ The Middleware for callback is registered ")
    except Exception:
        logger.exception("❌ The Middleware for callback not is registered ")
        raise
    try:
        await reset_db_once()
        logger.info("✅ The database has been initialized")
    except Exception:
        logger.exception("❌ Failed to initialize database")
        raise
    logger.info("✅ AI Service ready")
    try:
        dp.include_router(start_router)
        dp.include_router(callback_router)
        dp.include_router(card_family_advice)
        dp.include_router(birth_date_calendar)
        dp.include_router(cards_obusha)
        dp.include_router(cards_vadaram)
        dp.include_router(admin_message)
        logger.info("✅ All handlers registered")
    except Exception as e:
        logger.exception(f"❌ Failed to register handlers: {e}")
        return
