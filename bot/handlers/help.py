from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import logging

from bot.keyboards import main_keyboard

router = Router()
logger = logging.getLogger(__name__)


@router.message(Command('help'))
async def cmd_help(message: Message):
    """
    Отправляет пользователю справочную информацию о доступных командах и основных возможностях бота.

    Сообщение содержит:
    - Список основных команд с кратким описанием
    - Краткие инструкции по работе с ботом
    - Подсказки по загрузке файлов и поиску информации

    Args:
        message (Message): Объект сообщения от пользователя, инициировавшего команду /help.

    Returns:
        None
    """
    text = (
        "📚 *Команды и возможности бота:*\n\n"
        "/start — Запустить бота и получить приветствие\n"
        "/upload — Загрузить файл с устройства (PDF, DOCX, TXT и др.)\n"
        "/download_from_Yandex.disk — Загрузить файл со своего Яндекс.Диска\n"
        "/reset — Сбросить текущий контекст и начать заново\n"
        "/search_wiki — Искать информацию в Википедии\n"
        "/help — Показать это сообщение\n\n"
        "💡 *Как работать с ботом:*\n"
        "1. Загрузите документы через /upload или выберите файл со своего Яндекс.Диска через /download_from_Yandex.disk.\n"
        "2. Задавайте вопросы — я отвечу, используя загруженные материалы с помощью AI.\n"
        "3. Для поиска информации в Википедии используйте /search_wiki.\n"
        "4. Для сброса и начала новой сессии используйте /reset.\n\n"
        "Если хотите, просто отправьте файл или воспользуйтесь кнопками для быстрого доступа к функциям!"
    )

    await message.answer(text, parse_mode="Markdown", reply_markup=main_keyboard)

