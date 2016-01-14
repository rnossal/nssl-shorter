#!/usr/bin/env python
# encoding: utf-8

import pymongo, base62, urllib2, re, json

#Lê arquivo de configuração
with open('conf/conf.json') as json_data:
    conf = json.load(json_data)

#Pega a url da base de dados, inicia o cliente e depois pega o banco
MONGODB_URI = 'mongodb://%s:%s@%s:%s/%s' % (conf['mongoConnection']['user'],
											conf['mongoConnection']['password'],
											conf['mongoConnection']['host'],
											conf['mongoConnection']['port'],
											conf['mongoConnection']['database'])
#Estrutura: mongodb://[usuário]:[senha]@[host]:[porta]/[base de dados]

client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

urls = db['urls']

#Cria a chave e associa à URL
def create_short(url):
	url = re.sub('^http://|^https://', '', url)
	if url_exists(url) is False:
		try:
			req = urllib2.Request("http://" + url, headers={'User-Agent' : "Nossal's Browser"})
			response = urllib2.urlopen(req)
			response.close()

			cursor = urls.find().limit(1).sort('_id', -1)
			key = base62.encode(cursor.count())

			urls.insert({'_id': key, 'url': url})

			return key
		except Exception:
			return False
	else:
		return url_exists(url)

#Checa se a URL já foi encurtada
def url_exists(url):
	if urls.find({'url': url}).count() is 0:
		return False
	else:
		return urls.find({'url': url})[0]['_id']

#Pega e URL a partir da chave
def get_url(key):
	if urls.find({'_id': key}).count() is not 0:
		return 'http://' + urls.find({'_id': key})[0]['url']
	else:
		return False
