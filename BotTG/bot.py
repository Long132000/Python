import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from db import get_user_balance, update_user_balance
import datetime

# Установите уровень ведения журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция старта
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    balance = get_user_balance(user_id)
    if balance is None:
        await update.message.reply_text("Привет! У вас пока нет счета. Начнем с 100 монет.")
        update_user_balance(user_id, 100.0)
    else:
        await update.message.reply_text(f"Привет! Ваш текущий счет: {balance} монет.")

# Функция для ежедневного получения 10 монет 
async def day(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    user_id = update.message.from_user.id 
    data = get_user_balance(user_id) 

    if data is None: 
        await update.message.reply_text("Вы не зарегистрированы. Используйте команду /start.") 
        return 

    # Handle the case where the data is not a tuple with two elements
    if isinstance(data, tuple) and len(data) == 2:
        balance, last_claim_date = data
    else:
        await update.message.reply_text("Ошибка получения данных о балансе. Пожалуйста, попробуйте снова.")
        return  # Exit function if there's an error

    today = datetime.date.today().isoformat()  # Получаем дату в формате YYYY-MM-DD 

    if last_claim_date == today: 
        await update.message.reply_text("Вы уже получили свои 10 монет сегодня!") 
    else: 
        balance += 10 
        update_user_balance(user_id, balance, today) 
        await update.message.reply_text(f"Вы получили 10 монет! Ваш текущий баланс: {balance} монет.") 



# Функция для игры
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    balance = get_user_balance(user_id)

    if balance is None:
        await update.message.reply_text("Вы не зарегистрированы. Используйте команду /start.")
        return

    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("Пожалуйста, укажите сумму для ставки, например: /play 10")
        return

    bet = int(context.args[0])

    if bet <= 0 or bet > balance:
        await update.message.reply_text("Ставка должна быть положительной и не превышать ваш текущий счет.")
        return

    # Рандом между 1 и 2
    result = random.randint(1, 2)

    if result == 2:
        balance += bet
        await update.message.reply_text(f"Вы выиграли! Ваш новый баланс: {balance} монет.")
    else:
        balance -= bet
        await update.message.reply_text(f"Вы проиграли! Ваш новый баланс: {balance} монет.")

    update_user_balance(user_id, balance)

# Функция для обработки ошибок
def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main():
    """Запуск бота."""
    application = ApplicationBuilder().token("6811851117:AAFE3H8-_rmdJLcJoTW3kjf-yzam1NzCRBQ").build()  

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("day", day))  # Добавляем обработчик для команды /day
    application.add_error_handler(error)

    application.run_polling()

if __name__ == '__main__':
    main()
