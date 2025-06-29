from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext

from bot.keyboards import main_keyboard
from database.db_services import save_user_if_not_exists

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command('start'))
async def cmd_start(message: Message, session: AsyncSession, state: FSMContext):
    """
    Обработчик команды /start — приветствует пользователя и предоставляет основную информацию о возможностях бота.

    Отправляет приветственное сообщение с кратким описанием функционала:
    - Загрузка документов для создания базы знаний
    - Сброс текущего контекста с помощью /reset
    - Получение помощи через /help
    - Поиск информации в Википедии через /search_wiki
    - Подключение к облачному хранилищу (пока Яндекс.Диск)

    Также предлагает начать с загрузки файла или задать вопрос с помощью кнопки.

    Args:
        message (Message): Объект сообщения от пользователя, вызвавшего команду /start.
    """
    user_id = message.from_user.id
    await save_user_if_not_exists(user_id, session)
    await state.clear()

    text = (
        "👋 Привет! Я — ваш AI-ассистент.\n\n"
        "Я помогу вам создавать личную базу знаний и отвечать на ваши вопросы с помощью искусственного интеллекта.\n\n"
        "📁 Вы можете загрузить файл с вашего устройства (PDF, DOCX, TXT и др.) с помощью команды /upload, "
        "или выбрать файл со своего Яндекс.Диска через команду /download_from_Yandex.disk.\n\n"
        "🤖 После загрузки вы сможете задавать вопросы по содержимому ваших файлов — я найду ответ с помощью AI!\n\n"
        "🔍 Также вы можете искать информацию в Википедии с помощью команды /search_wiki.\n\n"
        "🔄 Чтобы сбросить текущий контекст и начать новую сессию, используйте /reset.\n"
        "❓ Для получения справки напишите /help.\n\n"
        "Начните с загрузки файла или воспользуйтесь кнопками ниже для быстрого доступа к функциям."
    )

    await message.answer(text, reply_markup=main_keyboard)
