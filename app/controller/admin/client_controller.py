# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.client_validator import ClientValidator
#from app.service.client_service import ClientService
#from app.entity.client_entity import ClientEntity

# TODO 動くようにする

'''
Client Controller Module
'''
class ClientController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('取引先マスタ', 'とりひきさきの情報を登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        #self.__service = ClientService()
        self.__validator = ClientValidator()
        pass

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        # session をクリアする
        self.set_session('client_id', '')
        self.set_session('client_name', '')
        
        return self.view('./template/admin/clients/list.html', self.__service.getList(self.__user_id, limit, offset))
    
    def create(self):
        return self.view('./template/admin/clients/create.html', ClientEntity())

    def detail(self, client_id):
        # TODO validation
        
        self.set_session('client_id', client_id)
        
        return self.view('./template/admin/clients/detail.html', self.__service.get(self.__user_id, client_id))

    def edit(self, client_id):
        language_id = self.get_session('client_id')
        # TODO validation        
        return self.view('./template/admin/clients/edit.html', self.__service.get(self.__user_id, client_id))
    
    def confirm(self):
        client_id = self.get_session('client_id')
        client_name = self.get_param('client_name')

        error_messages = self.__validator.get_error_messages(client_name)
        if(len(error_messages) == 0):
            self.set_session('client_name', client_name)
            template = './template/admin/clients/confirm.html'
        else:
            template = './template/admin/clients/create.html'
        
        # TODO Factory Class
        entity = ClientEntity()
        entity.set_client_id(client_id)
        entity.set_client_name(client_name)
        entity.set_error_message(error_messages)
        return self.view(template, entity)

    def insert(self):
        client_name = self.get_session('client_name')
        
        # TODO validation
        
        # session をクリアする
        self.set_session('client_id', '')
        self.set_session('client_name', '')

        return self.view('./template/admin/clients/complete.html', self.__service.create(self.__user_id, client_name))

    def update(self):
        client_id = self.get_session('client_id')
        client_name = self.get_session('client_name')
        
        # session をクリアする
        self.set_session('client_id', '')
        self.set_session('client_name', '')

        entity = ClientEntity()
        entity.set_client_id(self.__service.update(client_id, self.__user_id, client_name))
        return self.view('./template/admin/clients/complete.html', entity)
    
    def delete(self):
        client_id = self.get_param('client_id')

        # session をクリアする
        self.set_session('client_id', '')
        self.set_session('client_name', '')

        entity = ClientEntity()
        entity.set__id(self.__service.delete(_id, self.__user_id))
        return self.view('./template/admin/languages/complete.html', entity)    