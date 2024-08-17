from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests


MOYSKLAD_API_TOKEN = '<ВАШ_МОЙСКЛАД_ТОКЕН>'
SMART_LIFE_API_TOKEN = '<ВАШ_SMART_LIFE_ТОКЕН>'
SMART_LIFE_DEVICE_ID = '<ВАШ_SMART_LIFE_УСТРОЙСТВО_ID>'
TELEGRAM_BOT_TOKEN = '<ВАШ_TELEGRAM_BOT_TOKEN>'


def get_products_from_moysklad():
    url = "https://online.moysklad.ru/api/remap/1.2/entity/product"
    headers = {"Authorization": f"Basic {MOYSKLAD_API_TOKEN}"}
    response = requests.get(url, headers=headers)
    products = response.json().get('rows', [])
    return [(product['name'], product['salePrice'] / 100) for product in products]


def start(update: Update, context: CallbackContext):
    products = get_products_from_moysklad()
    keyboard = [[InlineKeyboardButton(f"{name} - {price}₽", callback_data=name)] for name, price in products]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать в наш магазин цветов, выберите букет который вам понравился:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    selected_product = query.data
    query.edit_message_text(text=f"Ого, хороший выбор: {selected_product}. Перейдите к оплате.")

    if process_payment():
        unlock_fridge()
        query.message.reply_text("Оплата прошла успешно! Дверь холодильника открыта, заберите свой букет.")
    else:
        query.message.reply_text("Ошибка при оплате, пожалуйста, попробуйте снова.")

# Функция для обработки оплаты
def process_payment():
    # Здесь должна быть интеграция с реальной платежной системой
    return True


def unlock_fridge():
    url = "https://api.smartlife.com/v1/device/control"
    data = {
        "device_id": SMART_LIFE_DEVICE_ID,
        "action": "turn_on"
    }
    headers = {"Authorization": f"Bearer {SMART_LIFE_API_TOKEN}"}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 200

def main():

    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



# Email: jumanyyazowayhan32@gmail.com
# Github: ayhandev
# My website: ayhan008.pythonanywhere.com