import os, sys, requests
from bs4 import BeautifulSoup

PUBLIC_QUERY = ""

class Shops:
	All = "All"
	Countdown = "Countdown"
	PakNSave = "PakNSave"
	NewWorld = "NewWorld"
	FreshChoice = "FreshChoice"

def getMultiData(QUERY, SHOP):
	if SHOP == "All":
		getCountdownData(QUERY)
		getPakNSaveData(QUERY)
		getNewWorldData(QUERY)
		getFreshChoiceData(QUERY, None)
	if SHOP == "Countdown":
		getCountdownData(QUERY)
	elif SHOP == "PakNSave":
		getPakNSaveData(QUERY)
	elif SHOP == "NewWorld":
		getNewWorldData(QUERY)
	elif SHOP == "FreshChoice":
		getFreshChoiceData(QUERY, None)

def getCountdownData(QUERY):
	print(QUERY)
	RES = requests.get(url="https://shop.countdown.co.nz/shop/searchproducts?search={}&search_type=ShopOnline".format(QUERY))
	print(RES.text)
	soup = BeautifulSoup(RES.text, 'html.parser')
	print(soup.find_all("product-stamp", {'class', 'ng-tns-c167-2'}))

def getPakNSaveData(QUERY):
	print(QUERY)
	RES = requests.get(url="https://www.paknsaveonline.co.nz/Search?q={}".format(QUERY))
	soup = BeautifulSoup(RES.text, 'html.parser')
	print(soup.find_all("a", {'class', 'fs-product-card__details u-color-black u-no-text-decoration u-cursor'}))

def getNewWorldData(QUERY):
	print(QUERY)
	RES = requests.get(url="https://www.ishopnewworld.co.nz/Search?q={}".format(QUERY))
	soup = BeautifulSoup(RES.text, 'html.parser')

def getFreshChoiceData(QUERY, STORE_LOCATION):
	print(QUERY)
	RES = requests.get(url="https://{}.store.freshchoice.co.nz/search?q={}".format("barrington" if STORE_LOCATION == None else STORE_LOCATION, QUERY))
	soup = BeautifulSoup(RES.text, 'html.parser')
