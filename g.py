# -*- coding: UTF-8 -*-

from app.helper.log_helper import LogHelper
log = LogHelper().get_instance()

from app.service.web_service import ConfigGetService
config = ConfigGetService().get_web_server_config()

