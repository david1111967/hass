#!/usr/bin/env python
import sys
# import BringApi
import pymongo
import requests

class Database(object):
    def __init__(self, uri, database):
        self.uri = uri
        self.database = database

    def initialize(self):
        self.database = "openfoodfacts"
        client = pymongo.MongoClient(self.uri)
        self.database = client[self.database]

    def insert (self, collection, data):
        self.database[collection].insert(data)
        pymongo.MongoClient(self.uri)

    def find(self, collection, query) :
        result = self.database[collection].find(query)
        pymongo.MongoClient(self.uri)
        return result

    def find_one(self, collection, query) :
        result = self.database[collection].find_one(query)
        pymongo.MongoClient(self.uri)
        return result
    
class BringExtract:
    def __init__(self, codigo, user, password, uri, database):
        self.codigo = codigo
        self.user = user
        self.password = password
        self.uri = uri
        self.database = database

    def search(self):
        database = Database(self.uri, self.database)
        database.initialize()
        query = {"Codigo": self.codigo}
        result = database.find("openfoodfacts", query)
        if result != None:
            for rownum in result:
                if rownum['Codigo'] == self.codigo:
                    Nombre = rownum['Nombre']
                    bring = BringApi(self.user, self.password, True)
                    bring.purchase_item(Nombre, "")
                    return Nombre

class BringApi:
	_bringRestURL = "https://api.getbring.com/rest/"

	class AuthentificationFailed(Exception):
		pass

	def __init__(self, uuid, bringuuid, use_login = False):
		if use_login:
			self.bringUUID, self.bringListUUID = self.login(uuid, bringuuid)
		else:
			self.bringUUID = uuid
			self.bringListUUID = bringuuid
		self.headers = {    'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp',
		                    'X-BRING-CLIENT': 'android',
		                    'X-BRING-USER-UUID': self.bringUUID,
		                    'X-BRING-VERSION': '303070050',
		                    'X-BRING-COUNTRY': 'de' }
		self.addheaders = { 'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp',
		                    'X-BRING-CLIENT': 'android',
		                    'X-BRING-USER-UUID': self.bringUUID,
		                    'X-BRING-VERSION': '303070050',
		                    'X-BRING-COUNTRY': 'de',
		                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

	@classmethod
	def login(cls, email, password):
		try:
			params = {'email': email, 'password': password}
			response = requests.get(cls._bringRestURL+"bringlists",params=params)
			response.raise_for_status()
			login = response.json()
			return login['uuid'], login['bringListUUID']
		except (requests.RequestException, KeyError):
			raise cls.AuthentificationFailed('email password combination not existing')

	def purchase_item(self, item, specification):
		files = {'file': f'&purchase={item}&recently=&specification={specification}&remove=&sender=null'}
		return requests.put(f'{self._bringRestURL}bringlists/{self.bringListUUID}', files=files, headers=self.addheaders)

