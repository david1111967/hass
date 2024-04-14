#!/usr/bin/env python
import sys
import bringapi
import pymongo

class Database(object):
    URI = "mongodb://root:DV8kR2kQRWF4@nas.local:27017/"
    DATABASE = "openfoodfacts"

    @staticmethod
    def initialize():
        Database.DATABASE = "openfoodfacts"
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[Database.DATABASE]

    @staticmethod
    def insert (collection, data):
        Database.DATABASE[collection].insert(data)
        pymongo.MongoClient(Database.URI)

    @staticmethod
    def find(collection, query) :
        result = Database.DATABASE[collection].find(query)
        pymongo.MongoClient(Database.URI)
        return result

    @staticmethod
    def find_one(collection, query) :
        result = Database.DATABASE[collection].find_one(query)
        pymongo.MongoClient(Database.URI)
        return result
    
class BringExtract:
    def __init__(self, codigo, user, password):
        self.codigo = codigo
        self.user = user
        self.password = password

    def search(self):
        Database.initialize()
        query = {"Codigo": self.codigo}
        result = Database.find("openfoodfacts", query)
        if result != None:
            for rownum in result:
                if rownum['Codigo'] == self.codigo:
                    Nombre = rownum['Nombre']
                    bring = bringapi.BringApi(self.user, self.password)
                    bring.purchase_item(Nombre)
                    return Nombre
