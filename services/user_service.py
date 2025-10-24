from database.operations import update_user
from utils.logger import AppLogging

logger = AppLogging.get_logger()


class UserService:
    @staticmethod
    async def update_user_field(user_id: int, **kwargs):
        await update_user(user_id, **kwargs)
        for field,value in kwargs.items():
            logger.info(f"✅ User {user_id} update {field}: {value}")