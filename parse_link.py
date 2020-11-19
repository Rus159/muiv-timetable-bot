from requests_html import HTMLSession


def parse():
    response = HTMLSession().get('https://www.muiv.ru/studentu/fakultety-i-kafedry/fakultet-it/raspisaniya/')
    links = response.html.find('a[href^="/upload"]')
    link = ''
    for i in links:
        if 'заоч.' not in i.text:
            link_buff, link = map(str, str(i).split('upload'))
            break
    link = link[:-2]
    link = 'https://www.muiv.ru/upload' + link
    return link
