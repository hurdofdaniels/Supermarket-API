import API, os, sys

if len(sys.argv) <= 1:
	query = input("What do you want to search for? ")
else:
	query = sys.argv[1]

API.getMultiData(query, API.Shops.PakNSave)
