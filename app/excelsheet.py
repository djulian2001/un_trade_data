from models import RowInvestments, UnFileSheets, CellInvestments
from utilities import hashThisList
import xlrd
import datetime
# import warnings
			
# warnings.filterwarnings("error")

class ExcelSheet( object ):
	"""docstring for ExcelSheet"""
	def __init__(self, db, bookObj, sheet ):
		self.db = db
		self.bookObj = bookObj
		self.xlsSheet = bookObj.xlsBook.sheet_by_name( sheet )
		self.sheetName = sheet
		
		self.cleanRows = None
		self.totalRows = self.xlsSheet.nrows
		self.totalColumns = self.xlsSheet.ncols
		
		self.sheetObj = self.makeSheet()

		self.extractData()

		self.sheetObj.sheet_data_rows = self.cleanRows

		self.db.session.add( self.sheetObj )
		self.db.session.commit()

	def makeSheet( self ):

		try:
			sheetObj = UnFileSheets()
			sheetObj.un_file_id = self.bookObj.bookId
			# sheetObj.source_hash = hash( self.xlsSheet )
			sheetObj.investment_type = self.sheetName, 
			sheetObj.investment_context = str( self.xlsSheet.cell_value(1,0) )
			sheetObj.investment_scale = str( self.xlsSheet.cell_value(2,0) )
			sheetObj.investment_sources = '; '.join( [ self.encodeLabel(x) for x in self.xlsSheet.col_values(0) if 'Source:' in x ]  )
			sheetObj.investment_notes = '; '.join( [ self.encodeLabel(y) for y in self.xlsSheet.col_values(0) if 'Note:' in y ]  )
			sheetObj.sheet_max_columns = self.xlsSheet.ncols
			sheetObj.sheet_max_rows = self.xlsSheet.nrows
			sheetObj.created_at = datetime.datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )

			sheetObj.sheet_country_name = self.xlsSheet.cell_value(0,0)
		
		except UnicodeEncodeError as e:
			sheetObj.sheet_country_name = self.encodeLabel( self.xlsSheet.cell_value(0,0) )

		finally:
			self.db.session.add( sheetObj )
			
			self.db.session.commit()
			
			self.sheetId = sheetObj.id

			return sheetObj

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
	
	def sheetPattern( self, subRow ):
		"""Each sheet has a header row, the following are the data value patterns for thos rows.  If they don't match it will print out the non-match"""
		patterns=[
			[u'Region / economy', u'', u'', u'', u'', u'', 2001.0, 2002.0, 2003.0, 2004.0, 2005.0, 2006.0, 2007.0, 2008.0, 2009.0, 2010.0, 2011.0, 2012.0],
			[u'Region / economy', u'', u'', u'', u'', u'', 2001.0, u'2002', u'2003', u'2004', u'2005', u'2006', u'2007', u'2008', u'2009', u'2010', u'2011', u'2012'],
			[u'Reporting economy', 2001.0, u'2002', u'2003', u'2004', u'2005', u'2006', u'2007', u'2008', u'2009', u'2010', u'2011', u'2012'],
			[u'Reporting economy', 2001.0, 2002.0, 2003.0, 2004.0, 2005.0, 2006.0, 2007.0, 2008.0, 2009.0, 2010.0, 2011.0, 2012.0], ]
		
		patternsB = [	
			[u'Region / economy', u'', u'', u'', u'', u'', 2001.0, u'2002', u'2003', u'2004', u'2005', u'2006', u'2007', u'2008', u'2009', u'2010', u'2011', u'2012', u'', u'', u''], ]
		
		if subRow in patterns:
			# print(subRow)
			return ( self.totalColumns-12, self.totalColumns, )
		elif subRow in patternsB:
			return ( self.totalColumns-12-3, self.totalColumns-3, )
		else:
			print('NO MATCH SHEET PATTERN')
			print subRow

		
	def rowPatternCheck( self, rowType ):
		"""
			There are less miss patterns to match against then hit patterns.  match the misses and return false.
			
			examples:
			array('B', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
			[empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'']
		
			array('B', [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
			[text:u'Source:  UNCTAD FDI/TNC database, based on data from the Coordinated Direct Investment Survey (CDIS) of IMF.', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'', empty:u'']
		"""
		patterns=[
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], ]
			
			# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		if rowType.tolist() in patterns:
			return False
		else:
			return True


	def cleanTheData( self, aRow ):
		
		if len(aRow) == 12 and type(aRow) is list:
			rules = {
				"..":0,
				"":0,
				"-":0,

				}
			return [ rules[x.value] if x.value in rules.keys() else x.value for x in aRow  ]

		else:
			print("RECORD Type: {} and length: {} ".format( len(aRow), type(aRow) ) )
			return None
		
	def findHeaderRow(self, colValues ):

		patterns = [
			'Reporting economy',
			'Region / economy' ]

		for x in colValues:
			
			if 'economy' in x:
				print x, colValues.index(x)



	def extractData( self ):
		headRowIndex = 4
		cleanedRows = 0

		columnNeedle = self.xlsSheet.col_values(0, 0, self.xlsSheet.nrows )		
		headerRow = self.xlsSheet.row_values( headRowIndex, 0, self.totalColumns )

		sheetP = self.sheetPattern( headerRow )

		for inRow in range( headRowIndex + 1, self.xlsSheet.nrows ):
			rowTypeObj = self.xlsSheet.row_types(inRow,0, sheetP[1] )
			if self.rowPatternCheck( rowTypeObj ):
				rowLabelObj = self.xlsSheet.row_slice( inRow, 0, sheetP[0] )
				rowDataObj = self.xlsSheet.row_slice( inRow, sheetP[0], sheetP[1] )

				# print rowLabelObj, rowTypeObj, rowDataObj
				rowLabel = [x.value for x in rowLabelObj if x.value ][0]
				# rowDataObj = self.xlsSheet.row_slice( inRow, sheetP[0], sheetP[1] )
				badLabels = ['Reporting economy','Region / economy']
				if rowLabel not in badLabels:				
					cleanedRow = self.cleanTheData( rowDataObj )
					if cleanedRow:
						self.addGoodData( cleanedRow, rowLabel )

						cleanedRows += 1
						# print "{}.{}".format( self.sheetId,	cleanedRows)
		self.cleanRows = cleanedRows

	
	def addGoodData( self, data, label ):
		
		dataRecord = RowInvestments()
		dataRecord.un_sheet_id 			= self.sheetId
		dataRecord.created_at			= datetime.datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )
		
		dataRecord.investment_economy 	= str( label.encode('utf8') )

		self.db.session.add( dataRecord )
		self.db.session.commit()
		
		nonZero = 0

		for cell in enumerate( data ):
			yearValue = cell[0] + 2001
			
			if cell[1] != 0:
				
				cellObj = CellInvestments()
				
				cellObj.un_row_id = dataRecord.id
				cellObj.year = yearValue
				cellObj.amount = cell[1]
				cellObj.created_at = datetime.datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )
				
				self.db.session.add( cellObj)
				nonZero += 1
			

		dataRecord.row_non_zeros = nonZero

		self.db.session.add( dataRecord )

		self.db.session.commit()


	def encodeLabel( self, label ):
		# print  label, label.encode('utf8')
		return label.encode('utf8')



