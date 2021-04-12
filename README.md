# Acessar postgres pelo terminal

sudo -i -u postgres
psql

# Criar Banco de dados:

CREATE DATABASE dbplayershub;

# Criar Usuário:

CREATE USER root WITH ENCRYPTED PASSWORD 'root';

GRANT ALL PRIVILEGES ON DATABASE dbplayershub TO root;

# Listar Bancos de Dados

\l

# Conectar em um Banco de Dados

\c nome_DB

# Listar Tabelas

\d

# Ver todos os usuários

\du
