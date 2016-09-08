from scrape import Scraper
from db import Db
from excelbook import ExcelBook
from excelsheet import ExcelSheet
import sys

def main():

	db = Db()

	scrape = Scraper()
	"""The Scraper() class works, but don't want to kill site with my dev hits"""

	for remoteFile in scrape.remoteFiles:

		anXlsBook = ExcelBook( db, remoteFile )

		sheetNames = anXlsBook.xlsBook.sheet_names()

		for sheetName in sheetNames:
			sheetObj = ExcelSheet( db, anXlsBook, sheetName )

		# sys.exit()

if __name__=="__main__":
	main()