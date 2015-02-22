from bottle import Bottle, run, template, static_file, request
from super5 import count_address_word
from db import log

app = application = Bottle()

@app.route('/super5')
@app.route('/')
def index():
    return default_template()

@app.route('/super5', method='POST')
def custom():
    in_address = request.forms.address
    in_word = request.forms.word
    result = apply_template(in_address, in_word)
    return result

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

def apply_template(in_address, in_word):
    try:
        print("apply")
        address_count = count_address_word(in_address, in_word)
        print("address")
        log(in_address, in_word, address_count)
        print("log")
        return template('templates/super5_template', address=in_address, word=in_word, number=address_count)
    except Exception as e:
        print("except", e)
        return template('templates/super5_template', address='none',
                word='none', number=0)

def default_template():
    return apply_template('http://www.aftonbladet.se', 'super')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port='8080', reloader = True, debug = True)
