from telebot import types


def start_inline():
    markup = types.InlineKeyboardMarkup()

    variants = types.InlineKeyboardButton(
        text="🖼 Обработка", callback_data="menu:variants"
    )
    balance = types.InlineKeyboardButton(text="💳 Баланс", callback_data="user:balance")

    markup.row(variants, balance)

    return markup


def recv_photo_inline(photo_id):
    markup = types.InlineKeyboardMarkup()

    shakal = types.InlineKeyboardButton(
        text="🧨 Шакал", callback_data=f"process:photo:shakal:{photo_id}"
    )
    shakalplus = types.InlineKeyboardButton(
        text="💥 Шакал +", callback_data=f"process:photo:shakalplus:{photo_id}"
    )
    cancel = types.InlineKeyboardButton(text="❌ Отмена", callback_data="menu:start")

    markup.row(shakal, shakalplus)
    markup.add(cancel)

    return markup


def done_shakal_photo_inline(photo_id):
    markup = types.InlineKeyboardMarkup()

    more = types.InlineKeyboardButton(
        text="Больше", callback_data=f"process:photo:shakal:{photo_id}"
    )
    less = types.InlineKeyboardButton(
        text="Меньше", callback_data=f"process:photo:shakal:{photo_id}"
    )
    back = types.InlineKeyboardButton(text="◀️ Назад", callback_data="menu:start")

    markup.row(more, less)
    markup.add(back)

    return markup


def variants_inline():
    markup = types.InlineKeyboardMarkup()

    photo = types.InlineKeyboardButton(
        text="🖼 Фото", callback_data="menu:variants:photo"
    )
    video = types.InlineKeyboardButton(
        text="📼 Видео", callback_data="menu:variants:video"
    )
    gif = types.InlineKeyboardButton(text="🎞 GIF", callback_data="menu:variants:gif")
    back = types.InlineKeyboardButton(text="◀️ Назад", callback_data="menu:start")

    markup.row(photo, video, gif)
    markup.add(back)

    return markup


def balance_inline():
    markup = types.InlineKeyboardMarkup()

    balance_info = types.InlineKeyboardButton(
        text="ℹ️ Что такое кредиты", callback_data="menu:balance_info"
    )
    topup = types.InlineKeyboardButton(
        text="💰 Купить кредиты", callback_data="user:balance:topup"
    )
    unlimit = types.InlineKeyboardButton(
        text="♾️ Купить безлимит", callback_data="user:balance:unlimit"
    )
    back = types.InlineKeyboardButton(text="◀️ Назад", callback_data="menu:start")

    markup.add(balance_info)
    markup.row(topup, unlimit)
    markup.add(back)

    return markup
