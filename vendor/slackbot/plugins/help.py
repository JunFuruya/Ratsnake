# coding=utf8
import os

from vendor.slackbot.bot import respond_to


@respond_to('help')
def help(message):
    message.reply('help')
