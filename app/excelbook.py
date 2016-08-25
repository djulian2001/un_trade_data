from models import UnFiles
from utilities import hashThisList, hashFile
import os.path
import requests
import xlrd
import datetime

class ExcelBook(object):
	"""
		ExcelBook, context and state manager for each file that requires data extraction from.
	"""
	def __init__( self, db, remoteContent ):
		# self.filePath = filePath
		self.db = db
		self.bookId = None
		self.xlsBook = None 
		self.dbUnFileRecord = None
		self.fileUrl = remoteContent[1]
		self.urlCountryName = self.encodeLabel( remoteContent[0] )
		self.fileName = remoteContent[1].split('/')[-1]
		self._dlPath = '/home/vagrant/downloads/'
		
		self.setState()

	@property
	def dlPath( self ):
		return self._dlPath

	def encodeLabel( self, label ):

		return label.encode('utf8')


	def setState( self ):
		"""
			The sqlaclchemy object that will hold state.  If the file already exists 
			within the database we will not 
		"""
		def getRecords():
			return self.db.session.query( UnFiles ).filter( UnFiles.file_name == self.fileName ).all()
		
		records = getRecords()

		
		if records:
			if len( records ) == 1:
				self.dbUnFileRecord = records[0]
				self.bookId = records[0].id
				self.downloadFile()
			else:
				raise "Data Error.  More than 1 record returned for file %".format( self.fileName )
		else:	
			try:		
				self.downloadFile()
				
				record = UnFiles()
				record.file_url = self.fileUrl
				record.file_name = self.fileUrl.split('/')[-1]
				record.source_hash = hashFile( self.dlPath + self.fileUrl.split('/')[-1] )
				record.created_at = datetime.datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )

				record.url_country_name = self.urlCountryName

			except UnicodeEncodeError as e:
				record.url_country_name = self.encodeLabel( self.urlCountryName )
			
			finally:
				self.db.session.add( record )
				self.db.session.commit()

				self.dbUnFileRecord = record
				self.bookId = record.id
		

	def downloadFile( self ):
		"""
			dlFlag will be set prior to indicate if the file requires to be downloaded or use a local
			copy on the file system.
		"""

		localFileName = self.dlPath + self.fileUrl.split('/')[-1]

		if not os.path.isfile( localFileName ) :
			filePage = requests.get( self.fileUrl )
			print(filePage)
			output = open( localFileName ,'wb')
			output.write( filePage.content )
			output.close()

			openedBook = xlrd.open_workbook( localFileName, encoding_override="utf8")
		else:
			openedBook = xlrd.open_workbook( localFileName, encoding_override="utf8" )

		self.xlsBook = openedBook

		print "processing: {}".format(self.fileName)

