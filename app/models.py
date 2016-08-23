from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey

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

class UnFiles( UnTradeBase ):
    __tablename__ = "un_trade_files"
    file_url = Column( String(255), nullable=False )
    file_name = Column( String(127), nullable=False )
    country_name = Column( String(127), nullable=False )
    data_source = Column( String(255), nullable=False, default="http://unctad.org/en/Pages/DIAE/FDI%20Statistics/FDI-Statistics-Bilateral.aspx" )


    investment_data = relationship( "Investments", cascade="all, delete-orphan" )

class Investments( UnTradeBase ):
    __tablename__ = "un_investment_data"
    un_file_id = Column( Integer, ForeignKey('un_trade_files.id'), nullable=False )
    country_name = Column( String(127), nullable=False )
    investment_context = Column( String(255), nullable=False )
    investment_scale = Column( String(55), nullable =False, default="(Millions of US dollars)" )
    investment_type = Column( String(15), nullable=False )
    investment_economy = Column( String(127), nullable=False )
    year_2001 = Column( Numeric(8,8), nullable=False )
    year_2002 = Column( Numeric(8,8), nullable=False )
    year_2003 = Column( Numeric(8,8), nullable=False )
    year_2004 = Column( Numeric(8,8), nullable=False )
    year_2005 = Column( Numeric(8,8), nullable=False )
    year_2006 = Column( Numeric(8,8), nullable=False )
    year_2007 = Column( Numeric(8,8), nullable=False )
    year_2008 = Column( Numeric(8,8), nullable=False )
    year_2009 = Column( Numeric(8,8), nullable=False )
    year_2010 = Column( Numeric(8,8), nullable=False )
    year_2011 = Column( Numeric(8,8), nullable=False )
    year_2012 = Column( Numeric(8,8), nullable=False )
    investment_sources = Column( String(255), nullable=True )
    investment_notes = Column( String(255), nullable=True )


