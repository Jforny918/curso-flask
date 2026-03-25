from wsgiref.simple_server import make_server

def aplicacao(environ, start_response):
    produtos = [
        {'nome': 'Notebook', 'valor': 2500},
        {'nome': 'Smartphone', 'valor': 1500},
        {'nome': 'Tablet', 'valor': 1200},
        {'nome': 'Monitor', 'valor': 800},
        {'nome': 'Teclado', 'valor': 200},
    ]

    linhas_html = ''
    for produto in produtos:
        linhas_html += f'<li>{produto["nome"]} - R$ {produto["valor"]}</li>'

    with open('index.html', 'r', encoding='utf-8') as file:
        html = file.read()

    html_final = html.replace('__PRODUTOS__', linhas_html)

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [html_final.encode('utf-8')]

make_server('', 5000, aplicacao).serve_forever()
