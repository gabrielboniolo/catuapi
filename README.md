# Catuapi

**Catuapi** é um projeto desenvolvido como parte da minha pós-graduação em Engenharia de Software.  
Seu objetivo é servir como um MVP simples para cadastro e visualização de cafés especiais brasileiros.

---

## Sobre o projeto

Este sistema foi feito utilizando **Python**, **Flask** e **SQLAlchemy**, com renderização de páginas HTML usando `render_template`.

A ideia é permitir o cadastro de cafés com informações básicas como:

- Nome
- Produtor
- Variedade
- Descrição sensorial
- Tipo
- Região
- Altitude

O usuário pode:

- Cadastrar um novo café
- Listar todos os cafés já registrados
- Visualizar os detalhes de um café específico
- Deletar um café (via formulário com botão de exclusão)

---

## Objetivo

A proposta principal do projeto é exercitar conceitos de desenvolvimento backend com Flask, como:

- Organização do projeto em arquivos separados (`main.py`, `routes.py`, `models.py`, `db.py`)
- Manipulação de banco de dados com SQLAlchemy
- Uso de templates para renderização dinâmica
- Implementação de rotas com métodos GET, POST e DELETE

Este projeto é apenas um protótipo educacional, mas pode ser expandido futuramente com autenticação, filtros, paginação, API REST completa, entre outros recursos.

---

## Status

Projeto funcional com as rotas principais implementadas.
