# -*- coding: utf-8 -*-

from app.service.slack_service import SlackBotStartService
from app.repository.api_idcf_cloud_repository import ApiIdcfCloudRepository

if __name__ == "__main__":
    slack_bot_service = SlackBotStartService()
    #slack_bot_service.run()

#    api_idcf_cloud_repository = ApiIdcfCloudRepository()
#    api_idcf_cloud_repository.start()
#    api_idcf_cloud_repository.get_virtual_machine_list()
#    api_idcf_cloud_repository.stop()
    