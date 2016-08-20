from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import UnTradeBase

class Db( object ):
	"""docstring for Db.  A total hack solution"""
	def __init__( self ):
		
		engine = create_engine('sqlite+pysqlite:////home/vagrant/downloads/un_investments.db')

		UnTradeBase.metadata.bind = engine
		UnTradeBase.metadata.drop_all( engine )
		UnTradeBase.metadata.create_all( engine )

		Session = sessionmaker( autoflush=False )
		Session.configure( bind=engine )

		self.session = Session()
		
