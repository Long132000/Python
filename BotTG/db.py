import sqlite3
import datetime
import logging

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('casino.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            balance REAL DEFAULT 100.0
        )
    ''')
    conn.commit()
    conn.close()

# Получение баланса пользователя
def get_user_balance(user_id):
    conn = sqlite3.connect('casino.db')
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        logging.error(f"Error retrieving balance for user {user_id}: {e}")
        return None
    finally:
        conn.close()

# Обновление баланса пользователя
def update_user_balance(user_id, balance):
    conn = sqlite3.connect('casino.db')
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO users (user_id, balance) VALUES (?, ?)', (user_id, balance))
        conn.commit()
    except Exception as e:
        logging.error(f"Error updating balance for user {user_id} to {balance}: {e}")
    finally:
        conn.close()

# Команда для регистрации пользователя
def register_user(user_id):
    if get_user_balance(user_id) is None:
        update_user_balance(user_id, 100.0)  # Начальный баланс 100.0

# Выполнение команды "день"
async def day(update, context):
    user_id = update.message.from_user.id

    # Регистрация пользователя, если он еще не зарегистрирован
    register_user(user_id)

    balance = get_user_balance(user_id)

    if balance is None:
        await update.message.reply_text("Ошибка получения данных о балансе. Пожалуйста, попробуйте снова.")
        return

    today = datetime.date.today().isoformat()

    # Если вы хотите добавить 10 монет
    new_balance = balance + 10
    update_user_balance(user_id, new_balance)

    await update.message.reply_text(f"Вы получили 10 монет! Ваш новый баланс: {new_balance:.2f} монет.")



# Инициализация базы данных при запуске
init_db()
