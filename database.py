import databases
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database('sqlite:///db.db')
engine = sqlalchemy.create_engine('sqlite:///db.db')