import csv
import os
fileDir = "WATCHLISTS\\"
watchlists = []

class Watchlist:
	def __init__(self, titleList):
		self.watchlist = titleList

def createObject(file):
	titles = []

	with open(file, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for i, row in enumerate(reader):
			if i!=0:
				titles.append(row[5])

	watchlists.append(Watchlist(titles))

	return None

def createLists(fileDir):

	for file in os.listdir(fileDir):
		createObject(fileDir+file)

	return None

def commonMovies(watchlists):

	commonList=watchlists[0].watchlist
	for i in range (len(watchlists)-1):
		commonList=set(commonList).intersection(watchlists[i+1].watchlist)

	return commonList

createLists(fileDir)

print(commonMovies(watchlists))