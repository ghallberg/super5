import sqlite3
from bottle import route, run, template, request, static_file
from super5 import count_address_word

def apply_template(in_address, in_word):
    try:
        address_count = count_address_word(in_address, in_word)
        log(in_address, in_word, address_count)
        return template('templates/super5_template', address=in_address, word=in_word, number=address_count)
    except:
        return default_template()

def log(address, word, count):
    conn = sqlite3.connect('super5.db')
    conn.cursor().execute(
            ''' INSERT INTO results (address,word,count) VALUES (?,?,?) ''',
            (address, word, count)
    )
    conn.commit()
    conn.close()

def default_template():
    return apply_template('http://www.aftonbladet.se', 'super')

@route('/super5')
@route('/')
def index():
    return default_template()

@route('/super5', method='POST')
def custom():
    in_address = request.forms.address
    in_word = request.forms.word
    result = apply_template(in_address, in_word)
    return result

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    bottle.debug(True)
    run(host='0.0.0.0', port='8080', reloader = True)
