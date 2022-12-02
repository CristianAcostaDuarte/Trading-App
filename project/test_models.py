
from app import app
import requests
import pytest
from flask import Flask
import json
from pymongo import MongoClient
import pymongo

#   Test to see if we can get data from the API
def test_insert_stock():
    response = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/DAVA?apikey=2c18aef9c283317435d76672c51df35d')
    assert response.status_code == 200

#   Test to check routes health
def test_base_route():
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    
def test_dava_route():
    client = app.test_client()
    url = '/dava'
    response = client.get(url)
    assert response.status_code == 200

def test_btc_route():
    client = app.test_client()
    url = '/btc'
    response = client.get(url)
    assert response.status_code == 200
    
def test_eth_route():
    client = app.test_client()
    url = '/eth'
    response = client.get(url)
    assert response.status_code == 200

def test_ada_route():
    client = app.test_client()
    url = '/ada'
    response = client.get(url)
    assert response.status_code == 200

def test_ibm_route():
    client = app.test_client()
    url = '/ibm'
    response = client.get(url)
    assert response.status_code == 200
    
def test_ibm_route():
    client = app.test_client()
    url = '/ec'
    response = client.get(url)
    assert response.status_code == 200
    

#Test to see if we are connected with mongodb
def test_mongo():
    try:
        client = MongoClient('localhost')
        client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError as exc:
        assert False, f"database raised an exception {exc}"


#Test to see emails.
