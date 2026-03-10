from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text = "о боте")],
            [KeyboardButton(text = "старт")],
            [KeyboardButton(text = "помощь")]
        ],
        resize_keyboard=True
    )
    return keyboard