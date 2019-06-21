#coding: UTF-8

import traceback

from app.service.dbdump_service import DbDumpService

from vendor.slackbot.bot import respond_to

@respond_to('^dbdump (.*)')
def dbdump(message, option):
    print(option)
    try:
        dbdump_service = DbDumpService()
        if option == 'list':
            file_names = dbdump_service.get_dump_names(message)

        elif option == 'create':
            dbdump_service.create_dump(message)

        else:
            option_list = option.split(' ')
            if len(option_list) > 1:
                # TODO ファイルの存在チェックをし、ファイルがあるときに削除するようにする
                dbdump_service.delete_dump(message, option_list[1])
    except:
        traceback.print_exc()