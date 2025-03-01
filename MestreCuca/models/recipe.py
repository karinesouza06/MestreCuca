from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, ForeignKey, delete, update
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

    @classmethod
    def get_receitas_usuario(cls, nome):
        Session = sessionmaker(bind=engine)
        session = Session()

        receitas = session.query(Receita).filter(Receita.nome_user == nome).all()
        
        returns receitas
        session.commit()

    @classmethod
    def get_receitas(cls):
        Session = sessionmaker(bind=engine)
        session = Session()

        receitas = session.query(Receita).all()
        
        returns receitas
        session.commit()
        
    @classmethod
    def delet(cls, id):
        Session = sessionmaker(bind=engine)
        session = Session()

        delet = (delete(Receita).where(Receita.id == id))
        
        session.execute(delet)
        session.commit()

    @classmethod
    def update(cls, id, nome_receita, nome_user, ingredientes, modo_preparo, categoria):
        Session = sessionmaker(bind=engine)
        session = Session()

        smt = (update(Receita).where(Receita.id == id).values(nome_receita=nome_receita, nome_user=nome_user, ingredientes=ingredientes, modo_preparo=modo_preparo, categoria=categoria))

        session.execute(smt)
        session.commit()
    
