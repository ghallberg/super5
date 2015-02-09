from bottle import route, run, template, request, static_file
from super5 import count_address_word

def apply_template(in_address, in_word):
    address_count = count_address_word(in_address, in_word)
    return template('templates/super5_template', address=in_address, word=in_word, number=address_count)

@route('/super5')
@route('/')
def index():
    return apply_template('http://www.aftonbladet.se', 'super')

@route('/super5', method='POST')
def custom():
    in_address = request.forms.address
    in_word = request.forms.word
    result = apply_template(in_address, in_word)
    return result

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='0.0.0.0', port='8080', reloader = True)
