from flask import Flask 
#Flask é um micro framework para desenvolvimento web em Python. 
#Ele é leve e fácil de usar, permitindo que os desenvolvedores criem aplicações web rapidamente. 
#O Flask fornece ferramentas e bibliotecas para lidar com rotas, requisições HTTP, templates, entre outras funcionalidades essenciais para o desenvolvimento web.
app = Flask (__name__)
#A linha app = Flask(__name__) cria uma instância da classe Flask, que é a aplicação web. O argumento __name__ é usado para determinar o caminho do arquivo atual, o que é útil para localizar recursos como templates e arquivos estáticos.

@app.route('/') #é a rota da aplicação, ou seja, o caminho que o usuário irá acessar para ver a mensagem "Hello World"
def main():
    return "Hello World"

app.run(debug=True) 
#inicia o servidor Flask em modo de depuração, o que permite que você veja mensagens de erro detalhadas e recarregue automaticamente a aplicação quando fizer alterações no código.