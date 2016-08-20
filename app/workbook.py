import xlrd


def cleanRow(aRow):
	print(aRow)

srcFiles = [
		'/home/vagrant/downloads/webdiaeia2014d3_ARG.xls',
		'/home/vagrant/downloads/webdiaeia2014d3_ARM.xls',
		'/home/vagrant/downloads/webdiaeia2014d3_DZA.xls', ]

x = xlrd.open_workbook(srcFiles[0])
# x = xlrd.open_workbook(srcFiles[0], formatting_info=True)




for iRow in range( x.sheet_by_name( 'inflows' ).nrows ):
	

	cleanRow(x.sheet_by_name( 'inflows' ).row(iRow))



class WorkBook(object):
	"""docstring for WorkBook"""
	def __init__(self, arg):
		super(WorkBook, self).__init__()
		self.arg = arg
		