# AI-чат-бот для Telegram

Интеллектуальный Telegram-бот, который выполняет функции AI-ассистента: консультирует, генерирует стратегии и работает с
файлами, загруженными с устройства или Яндекс.Диска.

---

## 🚀 Возможности

- Загрузка текстовых файлов с устройства или Яндекс.Диска
- Сохранение файлов на Яндекс.Диске приложения, разбиение их на фрагменты и сохранение в базе знаний с эмбендингами
- Поиск с помощью AI (Gigachat): выбор файлов, ввод запроса, получение ответа на основе релевантных фрагментов
- Поиск статей в Википедии по ключевым словам или фразам

---

## 📦 Установка и подготовка

1. **Клонируйте репозиторий:**  
   git clone <repo_url>  
   cd <repo_folder>

2. **Установите зависимости:**  
   pip install -r requirements.txt


3. **Установите сертификат Минцифры:**

- Скачайте сертификат с [Госуслуг](https://www.gosuslugi.ru/crt)
- Установите сертификат согласно инструкции на сайте

4. **Создайте базу данных PostgreSQL:**

- Создайте базу с именем `ai_assistant_db`

5. **Зарегистрируйте приложение на Яндекс.ID:**

- Укажите права доступа к Яндекс.Диску

6. **Создайте файл `.env` на основе `.env.template` и заполните переменные:**

| Переменная             | Описание                                                                        |
|------------------------|---------------------------------------------------------------------------------|
| `BOT_TOKEN`            | Токен Telegram-бота                                                             |
| `YANDEX_TOKEN`         | Токен приложения Яндекс.Диска                                                   |
| `YANDEX_CLIENT_ID`     | Client ID Яндекс.Диска                                                          |
| `YANDEX_CLIENT_SECRET` | Client Secret Яндекс.Диска                                                      |
| `AUTHORIZATION_KEY`    | Ключ авторизации для GigaChat                                                   |
| `REDIRECT_URI`         | URL для OAuth-редиректа (например, http://localhost:8000/yandex_oauth_callback) |
| `SERTIFICAT_PATH`      | Путь к сертификату Минцифры                                                     |
| `DOWNLOADS_DIR`        | Временная папка для загрузки файлов                                             |
| `DATABASE_URL`         | Строка подключения к базе данных                                                |

7. **При первом запуске раскомментируйте строки в `main.py` для загрузки nltk:**

import nltk
nltk.download('punkt')


---

## ⚡️ Запуск

- **Запустите API:**  
  uvicorn api:app --host 0.0.0.0 --port 8000 --reload


- **Запустите бота:**  
  python main.py

---

## 🧠 Альтернативный AI (локальный запуск)

Если лимит облачных токенов исчерпан, можно использовать локальную модель (например, YandexGPT-5-Lite-8B-instruct-GGUF
через Ollama).

### Минимальные требования для YandexGPT-5-Lite-8B-instruct-GGUF

| Компонент  | Минимум/Рекомендация               |
|------------|------------------------------------|
| RAM        | 16–32 ГБ                           |
| CPU        | Современный 4-ядерный, AVX2/AVX512 |
| Диск       | SSD, 12–20 ГБ свободно             |
| ОС         | Windows 10/11, Linux, macOS        |
| GPU (опц.) | NVIDIA CUDA (ускоряет инференс)    |

### Запуск через Ollama

1. **Скачайте модель** (например, с Hugging Face) и сохраните в папку:  
   C:\Users<ваш_пользователь>\models\YandexGPT-5-Lite-8B-instruct-GGUF\


2. **Установите Ollama:**  
   [https://ollama.com/download](https://ollama.com/download)

3. **Создайте Modelfile:**  
   FROM C:\Users<ваш_пользователь>\models\YandexGPT-5-Lite-8B-instruct-GGUF\YandexGPT-5-Lite-8B-instruct-Q4_K_M.gguf

4. **Зарегистрируйте модель в Ollama:**  
   cd C:\Users<ваш_пользователь>\ollama_custom_model  
   ollama create yandexgpt5lite -f Modelfile


5. **Запустите модель:**  
   ollama run yandexgpt5lite


6. **Используйте модель из Python:**  
   import requests

response = requests.post(  
"http://localhost:11434/api/generate",  
json={"model": "yandexgpt5lite",   
"prompt": "Привет! Объясни, как пользоваться Ollama с локальной моделью."}  
)  
print(response.json()["response"])

**Полезные ссылки:**

- [Документация Telegram Bot API](https://core.telegram.org/bots/api)
- [Документация Яндекс.Диска API](https://yandex.ru/dev/disk/api/reference/)
- [Документация GigaChat](https://developers.sber.ru/docs/ru/gigachat/api-rest)
- [Ollama](https://ollama.com/)