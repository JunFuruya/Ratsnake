# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class IndexEntity(BaseWebEntity):
    def __init__(self):
        super().__init__()
        pass
    
    def to_array(self):
        login_entity_list = super().__init__();
        return login_entity_list