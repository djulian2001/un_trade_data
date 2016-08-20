from scrape import Scraper
from db import Db
from exceldata import ExcelData

def main():

	db = Db()

	# scrape = Scraper()
	"""The Scraper() class works, but don't want to kill site with my dev hits"""
	remoteFiles = [
		('Afghanistan', '/home/vagrant/downloads/webdiaeia2014d3_AFG.xls'),
		('Albania', '/home/vagrant/downloads/webdiaeia2014d3_ALB.xls'),
		('Algeria', '/home/vagrant/downloads/webdiaeia2014d3_DZA.xls'),
		('American Samoa', '/home/vagrant/downloads/webdiaeia2014d3_ASM.xls'),
		('Angola', '/home/vagrant/downloads/webdiaeia2014d3_AGO.xls'),
		('Anguilla', '/home/vagrant/downloads/webdiaeia2014d3_AIA.xls'),
		('Antigua and Barbuda', '/home/vagrant/downloads/webdiaeia2014d3_ATG.xls'),
		('Argentina', '/home/vagrant/downloads/webdiaeia2014d3_ARG.xls'),
		('Armenia', '/home/vagrant/downloads/webdiaeia2014d3_ARM.xls'),
		('Aruba', '/home/vagrant/downloads/webdiaeia2014d3_ABW.xls'), ]

	# for remoteFile in scrape.remoteFiles:
	for remoteFile in remoteFiles:


		# downloads the an xls file
		# workBookPath = scrape.downloadFile( remoteFile[1] )
		
		workBookPath = remoteFile[1]

		xlsData = ExcelData( workBookPath, db, remoteFile )

		print(xlsData)

	# afg = scrape.remoteFiles[0]
	# scrape.downloadFile( afg[1] )

if __name__=="__main__":
	main()