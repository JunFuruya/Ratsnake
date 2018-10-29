#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.link_service import LinkService
from app.entity.link_entity import LinkEntity

from app.helper.helper import HashHelper

'''
Link Controller Module
'''
class LinkController(BaseController):

    def __init__(self):
        self.__service = LinkService()
        self.__title = 'リンク集'
        self.__description = 'リンク集を登録・編集・削除します。'
        pass

    def index(self, request, link_id=0):
        session = request.environ.get('beaker.session')
        # TODO セッションからとる
        user_id = 1
        # TODO もっと良い方法を考える
        if link_id == 0:
            link_id = request.query.get('link_id')
        if link_id == '':
            link_id = HashHelper.hexdigest('link_id') in session
 
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0
        
        session[HashHelper.hexdigest('link_id')] = ''
        session[HashHelper.hexdigest('link_name')] = ''
        session.save()

        # TODO もっと良い方法を考える
        entity = self.__service.getList(user_id, link_id, limit, offset)
        entity.set_link_id(link_id)
        # TODO もっと良い方法を考える
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        
        return self.view('./template/admin/links/list.html', entity=entity)
    
    def create(self, request, link_id):
        # TODO セッションからとる
        user_id = 1

        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('link_id')] = link_id
        session.save()

        entity = linkEntity()
        entity.set_link_id(link_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/create.html', entity=entity)

    def detail(self, request, link_id, link_id):
        
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('link_id')] = link_id
        session.save()
        
        entity = self.__service.get(user_id, link_id, link_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/detail.html', entity=entity)

    def edit(self, request, link_id, link_id):
        session = request.environ.get('beaker.session')
        #link_id = HashHelper.hexdigest('link_id') in session
        # TODO user_id 取得する
        user_id = 1
        
        entity = self.__service.get(user_id, link_id, link_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/edit.html', entity=entity)
    
    def confirm(self, request, link_id):
        session = request.environ.get('beaker.session')
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
        session.save()
        
        # TODO もっと良い設計があるはず
        entity = linkEntity()
        entity.set_link_id(link_id)
        entity.set_title(self.__title)
        entity.set_link_id(link_id)
        entity.set_link_spell(link_spell)
        entity.set_link_explanation(link_explanation)
        entity.set_link_pronounciation(link_pronounciation)
        entity.set_link_is_learned(link_is_learned)
        entity.set_link_note(link_note)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/confirm.html', entity=entity)

    def insert(self, request, link_id):
        session = request.environ.get('beaker.session')
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        link_spell = session.get(HashHelper.hexdigest('link_spell'), False)
        link_explanation = session.get(HashHelper.hexdigest('link_explanation'), False)
        link_pronounciation = session.get(HashHelper.hexdigest('link_pronounciation'), False)
        link_is_learned = session.get(HashHelper.hexdigest('link_is_learned'), False)
        link_note = session.get(HashHelper.hexdigest('link_note'), False)
        
        #TODO ログイン時に取得するようにする
        user_id = 1
        
        # TODO validation
        
        session = request.environ.get('beaker.session')
        
        session[HashHelper.hexdigest('link_id')] = ''
        session[HashHelper.hexdigest('link_name')] = ''
        session.save()

        entity = self.__service.create(user_id, link_id, link_spell, link_explanation, link_pronounciation, link_is_learned, link_note)
        entity.set_link_id(link_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/complete.html', entity=entity)

    def update(self, request, link_id, link_id):
        session = request.environ.get('beaker.session')
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        link_id = session.get(HashHelper.hexdigest('link_id'), False)
        link_spell = session.get(HashHelper.hexdigest('link_spell'), False)
        link_explanation = session.get(HashHelper.hexdigest('link_explanation'), False)
        link_pronounciation = session.get(HashHelper.hexdigest('link_pronounciation'), False)
        link_is_learned = session.get(HashHelper.hexdigest('link_is_learned'), False)
        link_note = session.get(HashHelper.hexdigest('link_note'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('link_id')] = ''
        session[HashHelper.hexdigest('link_spell')] = ''
        session[HashHelper.hexdigest('link_explanation')] = ''
        session[HashHelper.hexdigest('link_pronounciation')] = ''
        session[HashHelper.hexdigest('link_is_learned')] = ''
        session[HashHelper.hexdigest('link_note')] = ''
        session.save()

        entity = linkEntity()
        entity.set_link_id(link_id)
        entity.set_link_id(self.__service.update(user_id, link_id, link_id, link_spell, link_explanation, link_pronounciation, link_is_learned, link_note))

        entity.set_title(self.__title)
        entity.set_title(self.__title)
        entity.set_title(self.__title)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/complete.html', entity=entity)
    
    def delete(self, request, link_id, link_id):
        link_id = request.forms.get('link_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('link_id')] = ''
        session.save()

        entity = linkEntity()
        entity.set_link_id(link_id)
        entity.set_link_id(self.__service.delete(user_id, link_id, link_id))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/links/complete.html', entity=entity)
    
