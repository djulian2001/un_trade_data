from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey

class CommonBase(object):
    """
        Using a Decarative approach with sqlachemy, every table using the BioPublic
        base factory will leverage from these conventions
    """
    __table_args__ = {'mysql_engine':'InnoDB'}
    # new key for keeping record versions. 
    id = Column( Integer, primary_key=True )
    """ID created on the construction of the model"""
    created_at = Column( DateTime, nullable=False )

UnTradeBase = declarative_base( cls=CommonBase )

class UnFiles( UnTradeBase ):
    __tablename__ = "un_trade_files"
    file_url = Column( String(255), nullable=False )
    file_name = Column( String(127), nullable=False )
    url_country_name = Column( String(127), nullable=False )
    data_source = Column( String(255), nullable=False, default="http://unctad.org/en/Pages/DIAE/FDI%20Statistics/FDI-Statistics-Bilateral.aspx" )
    source_hash = Column( String(64), nullable=False )
    """The source_hash: A hash of the source record which will indicate if a record has changed"""
    
    file_investment_data = relationship( "UnFileSheets", cascade="all, delete-orphan" )

class UnFileSheets( UnTradeBase ):
    __tablename__ = "un_investment_sheet"
    un_file_id = Column( Integer, ForeignKey('un_trade_files.id'), nullable=False )
    sheet_country_name = Column( String(127), nullable=False )
    investment_type = Column( String(15), nullable=False )
    investment_context = Column( String(255), nullable=False )
    investment_scale = Column( String(55), nullable =False, default="(Millions of US dollars)" )
    investment_sources = Column( String(255), nullable=True )
    investment_notes = Column( String(255), nullable=True )
    sheet_max_columns = Column( Integer, nullable=False )
    sheet_max_rows = Column( Integer, nullable=False )
    sheet_data_rows = Column( Integer, nullable=True )
    
    sheet_investment_data = relationship( "RowInvestments", cascade="all, delete-orphan" )

class RowInvestments( UnTradeBase ):
    __tablename__ = "un_investment_row"
    un_sheet_id = Column( Integer, ForeignKey('un_investment_sheet.id'), nullable=False )
    investment_economy = Column( String(127), nullable=False )
    row_non_zeros = Column( Integer, nullable=True )
    
    row_investment_data = relationship( "CellInvestments", cascade="all, delete-orphan" )

class CellInvestments( UnTradeBase ):
    __tablename__ = "un_investment_data"
    un_row_id = Column( Integer, ForeignKey( 'un_investment_row.id' ), nullable=False )
    year = Column( Integer, nullable=False )
    amount = Column( Numeric(35,20), nullable=False )



