from models import Source

rootSite = "unctad.org"

for option in XPATHQUERY( //*[@id="FDIcountriesxls"] ) if !option.index(1):
	
	srcFile = Source()

	srcFile.url = option.attribute.value() + rootSite
	country = option.value()
	
	# //*[@id="FDIcountriesxls"]/option[2]
	#	<option value="/Sections/dite_fdistat/docs/webdiaeia2014d3_AFG.xls">Afghanistan</option>

