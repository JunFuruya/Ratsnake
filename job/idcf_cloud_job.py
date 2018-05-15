# -*- coding: utf-8 -*-

from app.service.slack_service import SlackBotStartService
from vendor.slackbot.bot import respond_to, listen_to, default_reply

slack_bot_service = SlackBotStartService()

@respond_to('start orange')
def start_orange_virtual_machine(message):
    message.reply('OK')

@respond_to('stop orange')
def stop_orange_virtual_machine(message):
    message.send('stop')