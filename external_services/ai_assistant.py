from config import AUTHORIZATION_KEY, SERTIFICAT_PATH
import httpx
import requests
import uuid
import logging

logger = logging.getLogger(__name__)


async def get_access_token():
    """
    Асинхронно получает OAuth access_token для GigaChat API Сбербанка.

    Отправляет POST-запрос на эндпоинт авторизации Sberbank NGW с использованием
    базовой авторизации и уникального идентификатора запроса. Использует кастомный
    сертификат для проверки SSL-соединения.

    Returns:
        str | None: Строка access_token, если запрос выполнен успешно, иначе None.

    Исключения:
        Логирует ошибку и возвращает None при возникновении исключения.
    """
    try:
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Authorization": f"Basic {AUTHORIZATION_KEY}",
            "RqUID": str(uuid.uuid4())
        }
        data = {
            "scope": "GIGACHAT_API_PERS"
        }
        async with httpx.AsyncClient(verify=SERTIFICAT_PATH, timeout=20) as client:
            response = await client.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()["access_token"]
    except Exception as ex:
        logger.error("Error during getting token AI: %s", str(ex))
        return None


async def generate_answer(access_token, question, context):
    """
    Асинхронно отправляет вопрос и контекст в GigaChat API и возвращает сгенерированный ответ.

    Формирует payload с моделью GigaChat, системным сообщением и пользовательским вопросом,
    отправляет POST-запрос на эндпоинт GigaChat и возвращает текст ответа.

    Args:
        access_token (str): OAuth access_token для авторизации в GigaChat API.
        question (str): Вопрос пользователя.
        context (str): Контекст для генерации ответа (может быть пустым).

    Returns:
        str | None: Сгенерированный ответ от GigaChat, либо None при ошибке.

    Исключения:
        Логирует ошибку и возвращает None при возникновении исключения.
    """
    try:
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "model": "GigaChat",
            "messages": [
                {"role": "system", "content": "Ты — помощник, который отвечает на вопросы."},
                {"role": "user", "content": f"Контекст: {context}\nВопрос: {question}"}
            ],
            "stream": False
        }
        async with httpx.AsyncClient(verify=SERTIFICAT_PATH, timeout=20) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
    except Exception as ex:
        logger.error("Error during generating answer AI: %s", str(ex))
        return None
