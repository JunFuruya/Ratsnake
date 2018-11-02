#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.link_service import LinkService
from app.entity.link_entity import LinkEntity

from app.helper.helper import HashHelper

'''
Link Controller Module
'''
class LinkController(BaseController):

    def __init__(self, request):
        super().__init__(request)
        self.__title = 'リンク集'
        self.__description = 'リンク集を登録・編集・削除します。'
        self.__notification = 'Please enter your id and password.'

        self.__service = LinkService()
        pass

    def index(self):
        # TODO セッションからとる
        user_id = 1
        link_id = HashHelper.hexdigest('link_id') in session
 
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)
        
        self.set_session('link_id', '')
        self.set_session('user_id', '')
        self.set_session('link_category_id', '')
        self.set_session('link_site_name', '')
        self.set_session('link_url', '')
        self.set_session('link_display_order', '')

        # TODO もっと良い方法を考える
        entity = self.__service.getList(user_id, link_id, limit, offset)
        entity.set_link_id(link_id)
        return self.view('./template/admin/links/list.html', entity=entity)
    
    def create(self):
        # TODO セッションからとる
        user_id = 1

        # TODO validation
        
        return self.view('./template/admin/links/create.html', entity=linkEntity())

    def detail(self, link_id):
        link_id = self.get_param('link_id')
        # TODO , user_id 取得する
        user_id = 1
        # TODO validation
        
        self.set_session('link_id', link_id)
        self.set_session('link_category_id', link_category_id)
        self.set_session('link_site_name', link_site_name)
        self.set_session('link_url', link_url)
        self.set_session('link_display_order', link_display_order)
        
        return self.view('./template/admin/links/detail.html', entity=self.__service.get(user_id, link_id))

    def edit(self, link_id):
        self.set_session('link_id', link_id)
        # TODO user_id 取得する
        user_id = 1
        
        return self.view('./template/admin/links/edit.html', entity=self.__service.get(user_id, link_id))
    
    def confirm(self, request, link_id):
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        link_spell = request.forms.get('link_spell')
        link_explanation = request.forms.get('link_explanation')
        link_pronounciation = request.forms.get('link_pronounciation')
        # TODO 取得した値に応じて表示する
        link_is_learned = 0
        link_note = request.forms.get('link_note')
        
        # TODO validation
        
        session[HashHelper.hexdigest('link_spell')] = link_spell
        session[HashHelper.hexdigest('link_explanation')] = link_explanation
        session[HashHelper.hexdigest('link_pronounciation')] = link_pronounciation
        session[HashHelper.hexdigest('link_is_learned')] = link_is_learned
        session[HashHelper.hexdigest('link_note')] = link_note
        
        # TODO もっと良い設計があるはず
        entity = linkEntity()
        entity.set_link_id(link_id)
        entity.set_link_id(link_id)
        entity.set_link_spell(link_spell)
        entity.set_link_explanation(link_explanation)
        entity.set_link_pronounciation(link_pronounciation)
        entity.set_link_is_learned(link_is_learned)
        entity.set_link_note(link_note)
        return self.view('./template/admin/links/confirm.html', entity=entity)

    def insert(self, link_id):
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        link_spell = session.get(HashHelper.hexdigest('link_spell'), False)
        link_explanation = session.get(HashHelper.hexdigest('link_explanation'), False)
        link_pronounciation = session.get(HashHelper.hexdigest('link_pronounciation'), False)
        link_is_learned = session.get(HashHelper.hexdigest('link_is_learned'), False)
        link_note = session.get(HashHelper.hexdigest('link_note'), False)
        
        #TODO ログイン時に取得するようにする
        user_id = 1
        
        # TODO validation
        
        session[HashHelper.hexdigest('link_id')] = ''
        session[HashHelper.hexdigest('link_name')] = ''

        entity = self.__service.create(user_id, link_id, link_spell, link_explanation, link_pronounciation, link_is_learned, link_note)
        entity.set_link_id(link_id)
        return self.view('./template/admin/links/complete.html', entity=entity)

    def update(self, link_id):
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        link_spell = session.get(HashHelper.hexdigest('link_spell'), False)
        link_explanation = session.get(HashHelper.hexdigest('link_explanation'), False)
        link_pronounciation = session.get(HashHelper.hexdigest('link_pronounciation'), False)
        link_is_learned = session.get(HashHelper.hexdigest('link_is_learned'), False)
        link_note = session.get(HashHelper.hexdigest('link_note'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        session[HashHelper.hexdigest('link_id')] = ''
        session[HashHelper.hexdigest('link_spell')] = ''
        session[HashHelper.hexdigest('link_explanation')] = ''
        session[HashHelper.hexdigest('link_pronounciation')] = ''
        session[HashHelper.hexdigest('link_is_learned')] = ''
        session[HashHelper.hexdigest('link_note')] = ''

        entity = linkEntity()
        entity.set_link_id(link_id)
        entity.set_link_id(self.__service.update(user_id, link_id, link_id, link_spell, link_explanation, link_pronounciation, link_is_learned, link_note))

        return self.view('./template/admin/links/complete.html', entity=entity)
    
    def delete(self, link_id):
        link_id = request.forms.get('link_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        session[HashHelper.hexdigest('link_id')] = ''

        entity = linkEntity()
        entity.set_link_id(self.__service.delete(user_id, link_id, link_id))
        return self.view('./template/admin/links/complete.html', entity=entity)