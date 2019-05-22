#coding: UTF-8

from vendor.slackbot.bot import respond_to

@respond_to('db')
def dump_database(message):
    #if == 'start':
    message.send('dump')
