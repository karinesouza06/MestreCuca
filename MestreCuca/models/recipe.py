from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, ForeignKey
from database.db import Base, db_session
from flask_login import UserMixin

class Receita(Base, UserMixin):
    __tablename__ = 'receitas'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome_receita: Mapped[str] = mapped_column(Text, nullable=False)
    nome_user: Mapped[int] = mapped_column(ForeignKey('usuarios.id'), nullable=False)
    ingredientes: Mapped[str] = mapped_column(Text, nullable=False)
    modo_preparo: Mapped[str] = mapped_column(Text, nullable=False)
    categoria: Mapped[str] = mapped_column(Text, nullable=False)

    @classmethod
    def exists(cls, nome_receita):
        return db_session.query(cls).filter_by(nome_receita=nome_receita).first() is not None
    

    