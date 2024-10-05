import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

TOKEN = 'BOT_TOKEN'
dp = Dispatcher(storage=MemoryStorage())

kb_list = [[KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]]
kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

ikb_list = [[InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='Рассчитать'),
             InlineKeyboardButton(text='Формулы расчёта', callback_data='Формула')]]
ikb = InlineKeyboardMarkup(inline_keyboard=ikb_list)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=ikb)


@dp.callback_query(F.data == 'Рассчитать')
async def set_age(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.callback_query(F.data == 'Формула')
async def set_age(callback: CallbackQuery):
    await callback.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Ввведите свой рост: ')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Ввведите свой вес: ')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = round(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161, 1)
    await message.answer(f'Ваша норма калорий {str(calories)}')
    await state.clear()


@dp.message()
async def all_massages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
