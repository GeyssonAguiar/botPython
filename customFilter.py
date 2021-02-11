from telegram.ext import MessageFilter

class FilterAwesome(MessageFilter):
    def filter(self, message):
        return '#bot' in message.text

class FilterDolar(MessageFilter):
    def filter(self, message):
        return message.text

class FilterBovespa(MessageFilter):
    def filter(self, message):
        return message.text


