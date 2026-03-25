# Painel de Vendas - StyleSync (API e Web App)

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

Este repositório contém o código-fonte de uma API RESTful e uma aplicação web simples desenvolvida em Flask para gerenciamento de produtos e vendas. O projeto foi construído de forma incremental, seguindo as melhores práticas de desenvolvimento, como a separação de responsabilidades, validação de dados e autenticação segura.

## 📜 Sobre o Projeto

O "Painel de Vendas StyleSync" simula o back-end e uma interface de administração para uma startup de e-commerce fictícia. O objetivo é fornecer uma base sólida e escalável para gerenciar as principais entidades do negócio: produtos, usuários e vendas.

A aplicação foi desenvolvida com uma arquitetura que utiliza o padrão *Application Factory* e *Blueprints* para garantir a modularidade e facilitar a manutenção e os testes.

## ✨ Funcionalidades Principais

* **API RESTful Completa:** Endpoints para todas as operações CRUD (Criar, Ler, Atualizar, Deletar) de produtos.
* **Autenticação via JWT:** Sistema de login que gera um JSON Web Token para proteger rotas administrativas.
* **Upload de Dados em Massa:** Funcionalidade para importar registros de vendas através do upload de arquivos `.csv`.
* **Validação de Dados:** Uso da biblioteca Pydantic para validar a estrutura e os tipos de dados em todas as requisições de entrada.
* **Interface Web Simples:** Páginas HTML renderizadas pelo Flask (usando Jinja2) e estilizadas com Bootstrap para interagir com as funcionalidades do back-end.
* **Introdução a Testes:** Inclui um exemplo de teste unitário utilizando Pytest.

## 🛠️ Tecnologias Utilizadas

* **Back-end:**
    * **Python 3**
    * **Flask:** Microframework web para a construção da API e da aplicação.
    * **MongoDB:** Banco de dados NoSQL para persistência dos dados.
    * **PyMongo:** Driver oficial para conectar a aplicação Python ao MongoDB.
    * **Pydantic:** Para validação e modelagem de dados.
    * **PyJWT:** Para geração e validação de JSON Web Tokens.
* **Front-end:**
    * **HTML5** com **Jinja2 Templates**
    * **Bootstrap 5:** Para estilização e responsividade das páginas.
* **Testes:**
    * **Pytest:** Framework para testes unitários.

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente de desenvolvimento.

### Pré-requisitos

* **Python 3.8+**
* **Git**
* Uma instância do **MongoDB** (local ou na nuvem, como o MongoDB Atlas).

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/stylesync_project.git](https://github.com/seu-usuario/stylesync_project.git)
    cd stylesync_project
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Unix/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Crie o arquivo `requirements.txt`** com o seguinte conteúdo:
    ```txt
    Flask
    pymongo
    python-dotenv
    pydantic
    PyJWT
    pytest
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Copie o conteúdo do exemplo abaixo para o seu `.env` e substitua pelos seus valores.

    ```ini
    # .env.example
    # Chave secreta para o Flask e JWT. Use um valor longo e aleatório.
    SECRET_KEY="uma-chave-secreta-muito-forte-e-aleatoria"

    # String de conexão do seu banco de dados MongoDB.
    MONGO_URI="mongodb+srv://<seu_usuario>:<sua_senha>@<seu_cluster>.mongodb.net/<nome_do_banco>?retryWrites=true&w=majority"
    ```

6.  **Execute a aplicação:**
    ```bash
    python run.py
    ```
    A aplicação estará rodando em `http://127.0.0.1:5000`.

##  документи API Endpoints

A API segue os princípios REST. Para acessar os endpoints protegidos, inclua o token JWT no cabeçalho da requisição: `Authorization: Bearer <seu_token>`.

| Método | Endpoint                    | Protegido? | Descrição                                        |
| :----- | :-------------------------- | :--------: | :------------------------------------------------- |
| `POST` | `/login`                    |     Não    | Autentica um usuário e retorna um `access_token`.  |
| `GET`  | `/produtos`                 |     Não    | Lista todos os produtos cadastrados.               |
| `GET`  | `/produto/<id>`             |     Não    | Retorna os detalhes de um produto específico.      |
| `POST` | `/produtos`                 |     Sim    | Cria um novo produto.                              |
| `PUT`  | `/produto/<id>`             |     Sim    | Atualiza um produto existente.                     |
| `DELETE`| `/produto/<id>`             |     Sim    | Deleta um produto existente.                       |
| `POST` | `/vendas/upload`            |     Sim    | Faz o upload de um arquivo `.csv` de vendas.       |

### Exemplo: Criar um Novo Produto

* **Endpoint:** `POST /produtos`
* **Corpo da Requisição (JSON):**
    ```json
    {
        "name": "Caneca Oficial do Curso",
        "price": 49.90,
        "description": "Uma caneca para tomar seu café enquanto coda.",
        "stock": 150
    }
    ```
* **Resposta de Sucesso (201 Created):**
    ```json
    {
        "message": "Produto criado com sucesso!",
        "id": "62e3f8c6b7d4a5e1f6e2c3d4"
    }
    ```

## 🌐 Interface Web

O projeto também serve uma interface web simples, construída com Flask Templates e Bootstrap, que permite interagir com a API. As páginas incluem:
* Página de Login (`/login`)
* Dashboard principal (`/dashboard`)
* Lista de Produtos (`/produtos`)
* Formulário para adicionar produtos (`/produtos/novo`)
* Formulário para upload de vendas (`/vendas/upload`)

## ✅ Testes

O projeto contém uma introdução a testes unitários com Pytest para garantir a qualidade do código. Para executar os testes, rode o seguinte comando na raiz do projeto:

```bash
