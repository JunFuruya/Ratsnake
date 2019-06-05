#coding: UTF-8

from app.service.dbdump_service import DbDumpService

from vendor.slackbot.bot import respond_to

@respond_to('^db (.*)')
def dbdump(message, args):
    option = args

    dbdump_service = DbDumpService()
    if option == 'list':
        file_names = dbdump_service.get_dump_names(message)

    elif option == 'create':
        dbdump_service.create_dump(message)

    elif option == 'delete':
        dbdump_service.delete_dump(message, file_name)
