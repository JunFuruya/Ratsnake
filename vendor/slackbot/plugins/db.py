#coding: UTF-8

from app.services.dbdump_service import DbDumpService

from vendor.slackbot.bot import respond_to

def __init__():
    self.__dbdump_service = DbDumpService()

@respond_to('db[\s]+list')
def list_dump_names(message):
    message.self.__dbdump_service.
    message.send('dump')

@respond_to('db[\s]+create')
def dump_database(message):
    message.send('dump')
