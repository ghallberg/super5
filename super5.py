from urllib.request import urlopen
import html2text

def get_site(address):
    with urlopen(address) as stream :
        html = stream.read().decode('utf8')
        return str(html)

def count_word(str_input, word):
    str_input = str_input.lower()
    return str_input.count(word)

def parse_to_txt(html_input):
    h_renderer = html2text.HTML2Text()
    h_renderer.ignore_links = True
    return h_renderer.handle(html_input)


def count_address_word(address, word):
    html = get_site(address)
    txt = parse_to_txt(html)
    return count_word(txt, word)
