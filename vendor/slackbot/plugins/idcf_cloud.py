#coding: UTF-8
import re

# 20180515 change include path from "slackbot" to "vendor.slackbot"
from vendor.slackbot.bot import respond_to
from vendor.slackbot.bot import listen_to

from app.service.idcf_cloud_service import BaseService

#commands = ('jushoku help - ')
# jushoku idcf start
# jushoku idcf stop

@respond_to('help')
def show_help(message):
    message.reply('test')
    pass

@respond_to('idcf start$', re.IGNORECASE)
def start_idcf_cloud(message):
    message.reply_webapi('hi!', as_user=None)

@respond_to('idcf start$', re.IGNORECASE)
def start_idcf_cloud(message):
    message.reply_webapi('hi!', as_user=None)

# サンプル。これを雛形に処理を追加する
#@respond_to('idcf start$', re.IGNORECASE)
#def start_idcf_cloud(message):
#    message.reply_webapi('hi!', as_user=None)