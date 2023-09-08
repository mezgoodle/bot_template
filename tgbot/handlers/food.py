from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from loader import dp
from tgbot.keyboards.reply.food_keyboard import make_row_keyboard
from tgbot.states.states import OrderFood

router = Router()
dp.include_router(router)

FOOD_NAMES = ["Sushi", "Spaghetti", "French fries"]
FOOD_SIZES = ["Mini", "Small", "Large"]


@router.message(Command("food"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Choose food:",
        reply_markup=make_row_keyboard(FOOD_NAMES),
    )
    await state.set_state(OrderFood.choosing_food_name)


@router.message(OrderFood.choosing_food_name, F.text.in_(FOOD_NAMES))
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_food=message.text.lower())
    await message.answer(
        text="Thanks. Now, please, choose a size of portion:",
        reply_markup=make_row_keyboard(FOOD_SIZES),
    )
    await state.set_state(OrderFood.choosing_food_size)


@router.message(OrderFood.choosing_food_name)
async def food_chosen_incorrectly(message: Message):
    await message.answer(
        text="I don't know such a dish.\n\n"
        "Please, choose from a list above:",
        reply_markup=make_row_keyboard(FOOD_NAMES),
    )


@router.message(OrderFood.choosing_food_size, F.text.in_(FOOD_SIZES))
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"You have chose {message.text.lower()} portion {user_data['chosen_food']}.\n",  # noqa: E501
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()
