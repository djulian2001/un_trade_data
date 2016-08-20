from lxml import html
import requests


class Scraper( object ):

	def __init__( self ):
		"""
			The source of this page is the UN reference the srcUrl for data use policy.
		"""
		self._srcUrl = 'http://unctad.org/en/Pages/DIAE/FDI%20Statistics/FDI-Statistics-Bilateral.aspx'
		self._xPath = '//*[@id="FDIcountriesxls"]/option'
		self._siteRoot = "http://unctad.org"
		self._dlPath = '/home/vagrant/downloads/'
		self._remoteFiles = None
		self.getRemoteFiles()
		
	@property
	def remoteFiles( self ):
		return self._remoteFiles

	@property
	def srcUrl( self ):
		return self._srcUrl
	
	@property
	def xPath( self ):
		return self._xPath
	
	@property
	def siteRoot( self ):
		return self._siteRoot
	
	@property
	def dlPath( self ):
		return self._dlPath

	def getRemoteFiles( self ):
		page = requests.get( self.srcUrl )
		tree = html.fromstring( page.content )
		options = tree.xpath( self.xPath )
		self._remoteFiles = [ ( option.text, self.siteRoot + option.get("value"), ) for option in options if option.get("value") ]
		
	def downloadFile( self, fileUrl ):
		"""Takes in a url to an xls file saves that file local and returns that local path"""
		localFileName = self.dlPath + fileUrl.split('/')[6]

		filePage = requests.get( fileUrl )
		output = open( localFileName ,'wb')
		output.write( filePage.content )
		output.close()

		return localFileName
