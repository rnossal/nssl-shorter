# Rnossal URL Shortener

######Um simples encurtador de URL feito em Python.

---

Encurtador de URL simples feito em Python usando Flask, Sass e banco de dados MongoDB.
Pode ser acessado no link [Rnossal URL Shortener]

## Configuração do ambiente
**TODO**
- Instalar Python 2.7
- Dependências no Python: Flask, Jinja2, MarkupSafe, Werkzeug, argparse, gunicorn, itsdangerous, wsgiref, pymongo
- Configurar a "MONGODB_URI" em lib/shortener.py com a URL do banco desejada

No Heroku:
```
heroku ps:scale web=1 --app [nome do app no heroku]
```
No ambiente de desenvolvimento:
```
python app.py
```

Projeto feito com carinho por: [Rafael Nossal]

[Rafael Nossal]:http://about.me/rnossal
[Rnossal URL Shortener]:http://nssl.ml
