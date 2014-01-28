from bottle import route, run, template, request
from super5 import count_address_word

@route('/super5')
def index():
    in_address = 'http://www.aftonbladet.se'
    in_word = 'super'
    address_count = count_address_word(in_address, in_word)
    return template('super5_template', address=in_address, word=in_word, number=address_count)

@route('/super5', method='POST')
def custom():
    in_address = request.forms.get('address')
    in_word = request.forms.get('word')
    address_count = count_address_word(in_address, in_word)
    return template('super5_template', address=in_address, word=in_word, number=address_count)


run(host='192.168.110.162', port='8080')
