from bottle import get, post, run, template
import mysql.connector

host = 'localhost'
port = 8080
debug=True
reloader=True

db_host = ''
db_port = 3306
db_name = 'hideout'
db_user = ''
db_pass = ''

@get('/')
def index(name):
    return template('<html><body>oh no!{{name}}</body></html>', name=name)

@get('/admin/links')
def link_list():
    sql = 'SELECT * FROM links limit 10'

    connect = mysql.connector.connect(db=db_name, host=db_host, port=db_port, user=db_user, passwd=db_pass)
    cur.execute(sql)
    
    link_list = [
        [1, 'AAA', 'http://aaa.co.jp'],
        [2, 'BBB', 'http://bbb.co.jp'],
        [3, 'CCC', 'http://ccc.co.jp']
    ]
    tempalte_path = './template/admin/links/list.html'
    return template(tempalte_path, link_list=link_list)

@get('/admin/links/create')
def link_create():
    html = '<html><body>create</body></html>'
    return template(html)

@post('/admin/links/update')
def link_update():
    html = '<html><body>update</body></html>'
    return template(html)

@post('/admin/links/confirm')
def link_confirm():
    html = '<html><body>confirm</body></html>'
    return template(html)

@post('/admin/links/complete')
def link_complete():
    html = '<html><body>complete</body></html>'
    return template(html)

#@error(404)
#def error(404):
#    return '404error'

#@error(500)
#def error(500):
#    return '500error'

if __name__ == "__main__":
    run(host=host, port=port, debug=debug, reloader=reloader)