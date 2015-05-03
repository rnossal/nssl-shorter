#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, redirect, render_template, request, jsonify
from lib import shortener

app = Flask(__name__)

#Habilita o debug do flask
app.debug = True

#Página inicial
@app.route('/')
def home():
	return render_template('index.html')

#Rotina quando fornecida a URL com uma possível chave
@app.route('/<key>/')
@app.route('/<key>')
def show_key(key):
	if shortener.get_url(key) is not False:
		return redirect(shortener.get_url(key))
	else:
		return page_not_found(None)

#Página de erro 404
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html')

#Cuida de pegar a URL pelo método POST e tentar encurtar
@app.route('/shortIt', methods=['POST'])
def shortIt():
	urlInput = request.form['urlInput']
	#Códigos de erro:
		#0 = Não foi recebida nenhuma string do input
		#1 = A string pega do input não parece ser uma URL válida
	if urlInput == '':
		return jsonify(errorCode = 0, url = None)
	else:
		shortened = shortener.create_short(urlInput)
		if shortened is False:
			return jsonify(errorCode = 1, url = None)
		else:
			return jsonify(errorCode = None, url = shortened)

if __name__ == '__main__':
	app.run()
