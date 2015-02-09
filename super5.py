from urllib.request import urlopen
import html2text

def get_site(address):
    with urlopen(address) as stream :
        html = stream.read().decode('utf8')
        return str(html)

def count_word(str_input, word):
    print(word)
    str_input = str_input.lower()
    return str_input.count(word)

def parse_to_txt(html_input):
    print('create renderer')
    h_renderer = html2text.HTML2Text()
    h_renderer.ignore_links = True
    print('handle')
    return h_renderer.handle(html_input)


def count_address_word(address, word):
    print('get_site')
    html = get_site(address)
    print('parse')
    txt = parse_to_txt(html)
    print('count')
    return count_word(txt, word)
