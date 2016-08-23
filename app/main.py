from scrape import Scraper
from db import Db
from excelbook import ExcelBook
from excelsheet import ExcelSheet
import sys

def main():

	db = Db()

	# scrape = Scraper()
	"""The Scraper() class works, but don't want to kill site with my dev hits"""

	# print( scrape.remoteFiles )

	# sys.exit()
	
	remoteFiles = [
		('Afghanistan', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_AFG.xls'),
		('Albania', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_ALB.xls'),
		('Algeria', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_DZA.xls'),
		('American Samoa', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_ASM.xls'),
		('Angola', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_AGO.xls'),
		('Anguilla', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_AIA.xls'),
		('Antigua and Barbuda', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_ATG.xls'),
		('Argentina', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_ARG.xls'),
		('Armenia', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_ARM.xls'),
		('Aruba', 'http://unctad.org/Sections/dite_fdistat/docs/webdiaeia2014d3_ABW.xls'), ]

	# for remoteFile in scrape.remoteFiles:
	for remoteFile in remoteFiles:

		anXlsBook = ExcelBook( db, remoteFile )

		inflowsSheet = anXlsBook.xlsBook.sheet_by_name("inflows")

		sheetNames = ['inflows', 'outflows','instock', 'outstock']
		for sheetName in sheetNames:
			sheetObj = ExcelSheet( db, anXlsBook, sheetName )

			# print("book {}, sheet {} total rows {}: total columns {} ".format( anXlsBook.fileName, sheetObj.name, sheetObj.totalRows, sheetObj.totalColumns ) )
			# print(sheetObj.investmentType)
			# print(sheetObj.investmentContext)
			# print(sheetObj.investmentScale)
			# print(sheetObj.investmentSources)
			# print(sheetObj.investmentNotess)






if __name__=="__main__":
	main()