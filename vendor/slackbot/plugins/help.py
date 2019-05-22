#coding: UTF-8

from vendor.slackbot.bot import respond_to
import g

@respond_to('help')
def show_help(message):
    g.log.info('test')
    help_text = 'help'
    g.log.info('auau')
    message.send(help_text)
