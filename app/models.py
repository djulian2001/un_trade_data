from sqlalchemy.ext.declarative import declarative_base

class CommonBase(object):
    """
        Using a Decarative approach with sqlachemy, every table using the BioPublic
        base factory will leverage from these conventions
    """
    __table_args__ = {'mysql_engine':'InnoDB'}
    # new key for keeping record versions. 
    id = Column( Integer, primary_key=True )
    """ID created on the construction of the model"""
    source_hash = Column( String(64), nullable=False )
    """The source_hash: A hash of the source record which will indicate if a record has changed"""
    created_at = Column( DateTime, nullable=False )

UnTradeBase = declarative_base( cls=CommonBase )

class SrcFiles( CommonBase ):
	__tablename__ = "source_files"
	file_url = Column( String(255), nullable=False )
	file_name = Column( String(127), nullable=False )
	country_name = Column( String(127), nullable=False )
	data_source = Column( String(255), nullable=False, default="http://unctad.org/en/Pages/DIAE/FDI%20Statistics/FDI-Statistics-Bilateral.aspx" )


class TblNew( CommonBase ):
	__tablename__ = "tab_one"
	col1 = Column( String(15), nullable=True, default='yeah data' )