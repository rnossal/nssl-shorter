# Rnossal URL Shortener

###### Um simples encurtador de URL feito em Python.

---

Encurtador de URL simples feito em Python usando Flask, Sass e banco de dados MongoDB.
Pode ser acessado no link [Rnossal URL Shortener]

## Configuração do ambiente
**TODO**
- Instalar Python 2.7 (para seguir a execução no ambiente de desenvolvimento também ter pip)
- Dependências no Python: Flask, Jinja2, MarkupSafe, Werkzeug, argparse, gunicorn, itsdangerous, wsgiref, pymongo
- Criar o arquivo de configuração conf.json na pasta conf (arquivo de exemplo em conf/conf_sample.json)

No Heroku:
```
Fazer deploy dos arquivos no Heroku
heroku ps:scale web=1 --app [nome do app no heroku]
```
No ambiente de desenvolvimento para testes:
```
pip install Flask Jinja2 MarkupSafe Werkzeug argparse gunicorn itsdangerous wsgiref pymongo
python app.py
```

Projeto feito com carinho por: [Rafael Nossal]

[Rafael Nossal]:http://about.me/rnossal
[Rnossal URL Shortener]:http://nssl.ml
