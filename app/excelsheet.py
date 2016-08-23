from models import Investments
from utilities import hashThisList
import xlrd
import datetime


class ExcelSheet( object ):
	"""docstring for ExcelSheet"""
	def __init__(self, db, bookObj, sheet ):
		self.db = db
		self.bookObj = bookObj
		self.xlsSheet = bookObj.xlsBook.sheet_by_name( sheet )
		self.name = self.xlsSheet.name
		self.cleanRows = None
		self.totalRows = self.xlsSheet.nrows
		self.totalColumns = self.xlsSheet.ncols
		self.countryName = self.xlsSheet.cell_value(0,0)
		self.investmentType = sheet
		self.investmentContext = self.xlsSheet.cell_value(1,0)
		self.investmentScale = self.xlsSheet.cell_value(2,0)
		self.investmentSources = '; '.join( [ x for x in self.xlsSheet.col_values(0) if 'Source:' in x ] )
		self.investmentNotes = ': '.join([ y for y in self.xlsSheet.col_values(0) if 'Note:' in y ] )
		
		if sheet =='inflows' or sheet == 'instock':
			self.inExtractData()
		else:
			self.outExtractData()

		db.session.commit()



	def checkThisRow( self, noneTest, holdValue ):
		ignoredValues = [
			'Region / economy',
			'Reporting economy',
			'Source:',
			'Note'
			]
		
		if noneTest == 3 and holdValue not in ignoredValues:
			print(holdValue)
			return True
		else:
			return False
	


	def inExtractData( self ):

		cleanRows = 0
		for inRow in range(3,self.xlsSheet.nrows):
			noneTest = 0
			holdValue = None
			for inCol in range(0,5):

				subRow = self.xlsSheet.row_values(inRow, 0, 5)
				print subRow
				testValue = self.xlsSheet.cell_value( inRow, inCol )
				
				if testValue is not None:
					holdValue = testValue
					# print(holdValue)
				else:
					++noneTest


				# print('{} noneTest:   {}').format(noneTest, testValue)

			# if self.checkThisRow( noneTest, holdValue ):
			# 	# print(holdValue)
			# 	dataRecord = Investments()
			# 	dataRecord.un_file_id 			= self.xlsBook.bookId
			# 	dataRecord.country_name 		= self.countryName
			# 	dataRecord.investment_context 	= self.investmentContext
			# 	dataRecord.investment_type		= self.investmentType
			# 	dataRecord.investment_economy 	= holdValue
			# 	dataRecord.year_2001 			= self.xlsSheet.cell_value( inRow, 6)
			# 	dataRecord.year_2002			= self.xlsSheet.cell_value( inRow, 7)
			# 	dataRecord.year_2003			= self.xlsSheet.cell_value( inRow, 8)
			# 	dataRecord.year_2004			= self.xlsSheet.cell_value( inRow, 9)
			# 	dataRecord.year_2005			= self.xlsSheet.cell_value( inRow, 10)
			# 	dataRecord.year_2006			= self.xlsSheet.cell_value( inRow, 11)
			# 	dataRecord.year_2007			= self.xlsSheet.cell_value( inRow, 12)
			# 	dataRecord.year_2008			= self.xlsSheet.cell_value( inRow, 13)
			# 	dataRecord.year_2009			= self.xlsSheet.cell_value( inRow, 14)
			# 	dataRecord.year_2010			= self.xlsSheet.cell_value( inRow, 15)
			# 	dataRecord.year_2011			= self.xlsSheet.cell_value( inRow, 16)
			# 	dataRecord.year_2012			= self.xlsSheet.cell_value( inRow, 17)
			# 	dataRecord.investment_sources 	= self.investmentSources
			# 	dataRecord.investment_notes		= self.investmentNotes
			# 	dataRecord.created_at			= datetime.datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )

			# 	++cleanRows

				# self.db.session.add( dataRecord )

			# first get the investment_economy value for a row

			# for columns between 0-5 get the value, but only if the rest are none. from 6 - 17
			


			# print(iRow)




	def outExtractData(self):
		pass


	def setSheetContext(self):
		# self.
		pass

	def cleanRow(self):
		pass
