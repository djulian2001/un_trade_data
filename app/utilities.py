import hashlib

def hashThisList( theList ):
	"""
		The following takes in a list of variable data types, casts them to a
		string, then concatenates them together, then hashs the string value
		and returns it.
	"""
	thisString = ""
	for i in theList:
		thisString += str( i )

	thisSha256Hash = hashlib.sha256(thisString).hexdigest()

	return thisSha256Hash


def hashFile( afileName ):

	BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

	sha256 = hashlib.sha256()

	with open(afileName, 'rb') as f:
	    while True:
	        data = f.read(BUF_SIZE)
	        if not data:
	            break
	        sha256.update( data )

	return sha256.hexdigest()
