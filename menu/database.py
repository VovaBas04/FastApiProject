from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import Column, String,UUID,ForeignKey
import uuid

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# from config import Base
SQLALCHEMY_DATABASE_URL = "postgresql://user2:password@localhost/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Menu(Base):
    __tablename__ = "menu"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    relationship("Submenu",back_populates='menu',cascade='all,delete')


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    menu_id = Column(UUID, ForeignKey('menu.id',ondelete='cascade'))
    relationship("Menu",back_populates='submenu')
    relationship("Dish",back_populates='submenu',cascade="all,delete")


class Dish(Base):
    __tablename__="dish"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    price = Column(String)
    submenu_id = Column(UUID,ForeignKey('submenu.id',ondelete='cascade'))
    relationship("Submenu",back_populates='dish')

Base.metadata.create_all(bind=engine)
