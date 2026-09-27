# Exerc-cio-Head-First-Python---Flask-search4letters

markdown
# Flask Search4Letters

Aplicação web simples em Flask, feita como exercício do livro *Head First Python*.

Recebe uma frase e um conjunto de letras através de um formulário, e retorna quais dessas letras aparecem na frase.

## Tecnologias
- Python 3
- Flask
- Jinja2 (templates com herança via `{% extends %}`)
- HTML + CSS

## Como rodar

```bash
git clone https://github.com/SEU_USUARIO/flask-search4letters.git
cd flask-search4letters
pip install flask
python3 vsearch4.py
```

Depois acesse `http://127.0.0.1:5000/entry` no navegador.

## Estrutura do projeto

├── vsearch4.py # rotas Flask (/, /entry, /search4)
├── search.py # lógica de busca (interseção de conjuntos)
├── templates/ # HTML com Jinja2
│ ├── base.html # template base (herança)
│ ├── entry.html # formulário de entrada
│ └── results.html # página de resultado
└── static/
└── hf.css # estilização


## O que pratiquei aqui
- Rotas Flask (GET e POST)
- Herança de templates com Jinja2
- Passagem de variáveis do backend pro HTML
- Formulários HTML e captura de dados via `request.form`
- Debug de erros comuns (caminhos de template, sintaxe Jinja, tags HTML mal fechadas)
