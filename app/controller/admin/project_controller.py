# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.project_entity_list import ProjectListEntity
from app.entity.project_entity import ProjectEntity

class ProjectController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('プロジェクト一覧', 'プロジェクトの一覧表示を行います。', '')
        self.__user_id = self.get_login_user()
        #self.__service = AccountTitleService()
        #self.__validator = AccountTitleValidator()

    def index(self):
        #self.set_session('account_title_id', '')
        #self.set_session('account_title_name', '')
        #self.set_session('account_title_classification_type', '')

        #return self.view('./template/admin/estimate/list.html', self.__service.getList(self.__user_id, limit, offset))
        return self.view('./template/admin/projects/list.html', ProjectListEntity())

    def insert(self):
        return self.view('./template/admin/projects/create.html', ProjectEntity())