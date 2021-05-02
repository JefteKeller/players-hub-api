# <h1 align="center">***Players Hub*** </h1>

*Players Hub* é uma API desenvolvida para Gerenciar o CRUD de Usuários, Times, Categorias de Jogos, Partidas, Localizações, Convites e Comentários.

A aplicação foi projetada utilizando o Modelo de DataBase Relacional com o PostgreSQL, sendo implementada através da ORM SQLAlchemy e Python.

>***
>A aplicação foi criada baseada na necessidade de um sistema para Conexão de Jogadores e Organização de Partidas entre eles.
>***
<br>

## *Principais Recursos*

***
<br>

> ***
>  - CRUD completo de Usuários e endpoints com Informações detalhadas sobre o Usuário.
> - Histórico detalhado de Partidas do Usuário como Jogador e como Gerente de Times.
> - CRUD de Equipes, Sistema de Convites e histórico de Partidas do Time.
> - CRUD de Partidas, Sistema de Comentários e Localidades.
>#

<br>

## *Deploy e Documentação da API*

***
Todas as rotas e retornos assim como exemplos de uso estão especificados aqui:

- [Site da Documentação](https://docs-players-hub-api.vercel.app/)

A aplicação está hospedada no ***Heroku***:

- [Link da API](https://players-hub.herokuapp.com/)

> *No primeiro acesso após um período sem requisições, a API levará alguns segundos para responder, pois os servidores estão inicializando.*
>
 <br>

## *Bibliotecas e Tecnologias*

***


### As seguintes ferramentas foram usadas na construção do projeto:

- [Flask](https://github.com/pallets/flask)
- [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy)
- [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate/)
- [Flask-Marshmallow](https://github.com/marshmallow-code/flask-marshmallow)
- [Flask-JWT-Extended](https://github.com/vimalloc/flask-jwt-extended)

### Configuracões de Ambiente e Deploy

- [Environs](https://github.com/sloria/environs)
- [Gunicorn](https://github.com/benoitc/gunicorn)

### Testes

- [IPDB](https://github.com/gotcha/ipdb)
- [Ipython](https://github.com/ipython/ipython)
- [Pytest](https://github.com/pytest-dev/pytest)
- [Faker](https://github.com/joke2k/faker)

### Linters e Formatadores

- [Pylint](https://github.com/PyCQA/pylint)
- [Black]((https://github.com/psf/black))
