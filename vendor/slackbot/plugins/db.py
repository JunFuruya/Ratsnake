#coding: UTF-8

from app.service.dbdump_service import DbDumpService

from vendor.slackbot.bot import respond_to


@respond_to('^db (.*)')
def dbdump(message, args):
    option = args
    print(option)
    folder_path = 'C:\\Users\\junfuruya\\Desktop\\src\\Hideout'
    message_no_files = 'バックアップファイルはないよ。'

    dbdump_service = DbDumpService()
    if option == 'list':
        file_names = dbdump_service.get_dump_names(folder_path)
        print(file_names)
        if file_names is None:
            message.send(message_no_files)
        else:
            message.send('\n'.join(file_names))

    elif option == 'create':
    #    dbdump_service.create_dump()
        message.send('B')
    elif option == 'delete':
    #    dbdump_service.delete_dump(file_name)
        message.send('C')
