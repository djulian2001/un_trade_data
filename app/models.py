from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Numeric
class CommonBase(object):
    """
        Using a Decarative approach with sqlachemy, every table using the BioPublic
        base factory will leverage from these conventions
    """
    # __table_args__ = {'mysql_engine':'InnoDB'}
    # new key for keeping record versions. 
    id = Column( Integer, primary_key=True )
    """ID created on the construction of the model"""
    source_hash = Column( String(64), nullable=False )
    """The source_hash: A hash of the source record which will indicate if a record has changed"""
    created_at = Column( DateTime, nullable=False )

UnTradeBase = declarative_base( cls=CommonBase )

class UnFiles( CommonBase ):
    __tablename__ = "un_trade_files"
    file_url = Column( String(255), nullable=False )
    file_name = Column( String(127), nullable=False )
    country_name = Column( String(127), nullable=False )
    data_source = Column( String(255), nullable=False, default="http://unctad.org/en/Pages/DIAE/FDI%20Statistics/FDI-Statistics-Bilateral.aspx" )


class Investments( CommonBase ):
    __tablename__ = "un_investment_data"
    country_name = Column( String(127), nullable=False )
    economy_region = Column( String(127), nullable=False )
    investment_type = Column( String(15), nullable=False )
    src_file_id = Column( Integer, nullable=False )
    year_20 = Column( Numeric() )
    additional_notes = Column( String(255), nullable=True )