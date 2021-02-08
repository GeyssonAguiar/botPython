from telegram.ext import MessageFilter

class FilterAwesome(MessageFilter):
    def filter(self, message):
        return '#bot' in message.text


