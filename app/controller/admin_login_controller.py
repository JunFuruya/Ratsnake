#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.base_entity import BaseEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class AdminLoginController(BaseController):
    def __init__(self):
        self.__title = ''
        self.__description = ''
        pass

    def index(self, request):
        service = LoginService()

        # TODO: a factory class should return entity through a service class 
        from app.entity.login_entity import LoginEntity
        login_entity = LoginEntity()
        login_entity.set_title('Hideout Main Page')
        login_entity.set_description('Hideout Login Page')
        login_entity.set_notification('Please enter your id and password.')
        tempalte_path = './template/admin/login.html'
        return jinja2_template(tempalte_path, entity=login_entity)

        # TODO もっと良い方法を考える
        entity = BaseEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/index.html')
        #return self.view('./template/index.html', entity=entity)

    def login(self, request):
        username = request.forms.get('username')
        password = request.forms.get('password')

        service = LoginService()
        if(service.is_authenticated(username, password)):
            session = request.environ.get('beaker.session')
            session[HashHelper.hexdigest('login')] = HashHelper.hexdigest(username)
            session.save()

            # TODO: move max_age to config file
            max_age = 60 * 60 * 24 * 30 # 1Month
            response.set_cookie(HashHelper.hexdigest('login'), session[HashHelper.hexdigest('login')], max_age=max_age)
            # TODO cookie 使えてる?
            return redirect('/admin')
        
        else:
            return redirect('/admin/login')

    def logout():
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('login')] = ''
        session.save()
        return redirect('/admin/login')

    def check_login_status():
        # TODO 動的に取得する
        username = 'admin' 
        session = request.environ.get('beaker.session')
        session_value = session.get(HashHelper.hexdigest('login'), False)
        hashed_value = HashHelper.hexdigest(username)
    
        if(session_value != hashed_value):
            return redirect('/admin/login')
        pass

