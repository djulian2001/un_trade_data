from models import UnFiles
import xlrd

class ExcelData(object):
	"""docstring for ExcelData"""
	def __init__( self, filePath, db, remoteContent ):
		# self.filePath = filePath
		self.db = db
		self.xlsBook = xlrd.open_workbook( filePath )
		self.fileUrl = remoteContent[1]
		self.urlCountryName = remoteContent[0]
		


	def makeRecord( self ):
		record = UnFiles()
		record.file_url = self.fileUrl
		record.country_name = self.urlCountryName
		record.file_name = self.fileUrl.split('/')[6]

		

