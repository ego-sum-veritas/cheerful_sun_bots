import asyncio
import random
from telegram import Bot

# Замініть 'YOUR_BOT_TOKEN' на твій отриманий токен від @BotFather
bot_token = '6310897669:AAH5dnBgBHuxXMRa_b9FE397n2TrLQI9iP8'
bot = Bot(token=bot_token)

# Замініть 'YOUR_GROUP_ID' на ідентифікатор твоєї групи в Telegram (можна отримати у @userinfobot)
group_id = '-1001816722760'

# Функція для отримання цитати з файлу
def get_random_quote():
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
        quotes = [quote.strip() for quote in quotes if quote.strip()]  # Видаляємо порожні рядки
        if not quotes:
            return 'Файл з цитатами порожній або містить лише порожні рядки.'
        return random.choice(quotes)


# Функція для надсилання цитати у групу
async def send_daily_quote():
    quote = get_random_quote()
    await bot.send_message(chat_id=group_id, text=quote)

# Головна функція
async def main():
    while True:
        await send_daily_quote()
        # Почекати 24 години перед наступною відправкою
        await asyncio.sleep(24 * 60 * 60)

if __name__ == "__main__":
    asyncio.run(main())

