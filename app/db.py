from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import UnTradeBase
import os

class Db( object ):
	"""docstring for Db.  A total hack solution"""
	def __init__( self ):
		
		# engine = create_engine('sqlite+pysqlite:////home/vagrant/downloads/un_investments.db')
		engine = create_engine(
					"mysql+pymysql://{}:{}@{}/{}".format(
						os.environ['MYSQL_USER_NAME'],
						os.environ['MYSQL_USER_PW'],
						os.environ['MYSQL_HOST_NAME'],
						os.environ['MYSQL_DATABASE'] ) )
						# os.environ['MYSQL_DATABASE'] ), echo=True )
		
		UnTradeBase.metadata.bind = engine
		UnTradeBase.metadata.drop_all( engine )
		UnTradeBase.metadata.create_all( engine )

		Session = sessionmaker( autoflush=False )
		Session.configure( bind=engine )

		self.session = Session()
		
