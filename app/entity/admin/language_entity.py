# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LanguageEntity(BaseWebEntity):
    def __init__(self):
        super().__init__()
        pass
    
    def to_array(self):
        language_entity_list = super().__init__();
        return language_entity_list