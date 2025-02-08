from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine('sqlite:///mestrecuca.db')
Session = sessionmaker(bind=engine)
db_session = Session()

def init_db():
    Base.metadata.create_all(engine)