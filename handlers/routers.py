'''
Модуль для работы с командами и обработки с запрещённый слов

@author: Сазанаков Владимир, Стогов Константин
@version: 1.0
@dateOfBeginning: 27.02.2026
@dateOfRelease: 30.05.2026
'''
from os import wait

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboard import get_main_reply_keyboard
from aiogram.fsm.state import State, StatesGroup  # Для работы с состоянием
from aiogram.fsm.context import FSMContext        # Для работы с состоянием

### Класс состояний (для функции /set_list )
class RegisterStates(StatesGroup):
    waiting_for_words = State()

router = Router()

badWords = ["delete", "казик", "нарко", "мет", "тяжкие", "jessy", "obama", "pussy", "ikit", "dick", "хуй", "пизда", "шлюха"]


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я простой бот для тебя\n\nНапиши <b>/help</b> для помощи",
                         parse_mode="HTML")
@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Команды:\n<b>/start</b> - заупстить бот\n<b>/help</b> для помощи\n<b>/about</b> для информации",
                         parse_mode="HTML",
                         reply_markup=get_main_reply_keyboard())
@router.message(Command("about"))
async def about(message: Message):
    await message.answer(f"Это команда про бота.\nБот разрабатывется командой БИТТ."
                         "\nСрок реализации - 30.05.2026")
@router.message(Command("my_handler"))
async def my_handler(message: Message):
    name = message.from_user.first_name
    user_id = message.from_user.id
    username = message.from_user.username
    await message.answer(f"firstname: <i>{name}</i>"
                         f"\nuserid: <i>{user_id}</i>"
                         f"\nusername: <i>{username}</i>", parse_mode="HTML")
"""
@router.message(Command("set_list"))
async def set_list(message: Message):
    await message.answer("Введите список запрещенных слов через пробел: "
                         "\nФормат ввода: слово1 слово2 слово3 слово4")

    await state.set_state(RegisterStates.waiting_for_words)

@router.message(RegisterStates.waiting_for_words)
async def process(message: Message, state: FSMContext):
    badWords = message.text.split()
    await state.clear()
"""
@router.message()
async def check_bad_words(message: Message):
    # Пропускаем команды (они уже обработаны выше)
    if message.text and message.text.startswith('/'):
        return
    ### Прикол
    if message.sticker or message.animation or message.photo:
        await message.delete()

    # Проверяем наличие текста
    if not message.text:
        return

    # Приводим к нижнему регистру для сравнения
    text_lower = message.text.lower()
    words = text_lower.split()

    # Проверка 1: совпадает ли все сообщение с запрещенным словом
    if text_lower in badWords:
        await message.delete()
        return
        return

    # Проверка 2: есть ли запрещенное слово внутри сообщения
    for word in words:
        if word in badWords:
            await message.delete()
            return

