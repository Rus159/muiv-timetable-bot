from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Keyboard:
    def __init__(self, arr):
        self.buttons = []
        self.greet = ReplyKeyboardMarkup(resize_keyboard=True)
        for text in arr:
            self.buttons.append(KeyboardButton(text))
        for button in self.buttons:
            self.greet.add(button)
        if 'Д' in arr[0]:
            self.greet.add(KeyboardButton('Вернуться к выбору курса'))

    def get_buttons(self):
        return self.greet
