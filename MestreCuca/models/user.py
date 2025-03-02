from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, ForeignKey
from database.db import Base, db_session
from flask_login import UserMixin, current_user

class User(Base,UserMixin):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(Text, nullable=False)

    @classmethod
    def exists(cls, email):
        return db_session.query(cls).filter_by(email=email).first() is not None
    
    @classmethod
    def exists_by_name(cls, nome):
        return db_session.query(cls).filter_by(nome=nome).first() is not None
    
    @classmethod
    def get(cls, user_id):
        user = db_session.query(cls).filter_by(id=user_id).first()
        return user
    
    @classmethod
    def get_id_by_name(cls, nome):
        user = db_session.query(cls).filter_by(nome=nome).first()
        return user.id if user else None
