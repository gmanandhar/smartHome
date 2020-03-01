from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from  flask import  jsonify
import  os
basedir = os.path.abspath(os.path.dirname(__file__))
db_uri = 'sqlite:///' + os.path.join(basedir, 'smartHome.sqlite')
engine = create_engine(db_uri)

# Create a MetaData instance
metadata = MetaData()
print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
print(metadata.tables)