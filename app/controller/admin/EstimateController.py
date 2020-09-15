# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController

class EstimateController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('見積一覧', '見積の登録と編集を行います。', '')
        self.__user_id = self.get_login_user()
        #self.__service = AccountTitleService()
        #self.__validator = AccountTitleValidator()

    def index(self, request):
        self.set_session('account_title_id', '')
        self.set_session('account_title_name', '')
        self.set_session('account_title_classification_type', '')

        #return self.view('./template/admin/estimate/list.html', self.__service.getList(self.__user_id, limit, offset))
        return self.view('./template/admin/estimate/list.html', null)