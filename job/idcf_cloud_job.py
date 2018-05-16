# -*- coding: utf-8 -*-

#from app.service.slack_service import SlackBotStartService
from app.service.idcf_cloud_service import IdcfCloudService
from vendor.slackbot.bot import respond_to, listen_to, default_reply

#slack_bot_service = SlackBotStartService()
idcf_cloud_service = IdcfCloudService()

@respond_to('start orange')
def start_orange_virtual_machine(message):
    # TODO: if faild to start, the bot should tell it failed
    idcf_cloud_service.start()
    message.reply('start')

@respond_to('stop orange')
def stop_orange_virtual_machine(message):
    # TODO: if faild to start, the bot should tell it failed
    idcf_cloud_service.stop()
    message.send('stop')