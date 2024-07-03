from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'хорошо' in message.text.lower():
        await message.reply('Я рад за тебя! Хорошего тебе дня, добрый человек!')
    elif 'нормально' in message.text.lower():
        await message.reply('Выше нос! Жизнь приносит сюрпризы! Хорошего тебе дня, добрый человек!')
    elif 'хорошего дня' in message.text.lower():
        await message.reply('Начни работу с указания /start или открой меню. Еще увидимся')
    elif 'и тебе' in message.text.lower():
        await message.reply('Начни работу с указания /start или открой меню. Еще увидимся!')
    else:
        await message.reply('М-да, к такому я не был готов...')
